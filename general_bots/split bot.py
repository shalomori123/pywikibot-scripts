import re

import pywikibot
from pywikibot import textlib, pagegenerators
from pywikibot.bot import SingleSiteBot, CurrentPageBot, input_yn


DEFAULT_ARGS = {
    'base_name': '', # The prefix in the titles of the new pages, default is the parent page name
    'titles': False, # The bot will work automatically according to the titles of the parent page
    'max_order': 5, # which titles order to split
    'regex': '', # parse the page manually with regex
    'group': '1', # which groups in the regex to use in the new name (seperated by comma, in the result it return spaces between)
    'notitle': False, # don't move the title itself to the new page
    'always': False, # to confirm all the edits
    'minor': False, # consider as a minor edit
}


class SubpagesBot(SingleSiteBot):
    """Subbot to create the subpages."""
    def __init__(self, parent, base_name, sections, notitle=False):
    	self.notitle = notitle
    	self.sections = sections
    	self.titles = {base_name + part.rstrip(): part for part in sections}
    	self.generator = pagegenerators.PagesFromTitlesGenerator(self.titles.keys())
    	self.summary = 'בוט פיצול: פוצל מתוך דף ' + parent.title(as_link=True)
    	self.created = []
    	super().__init__()
    
    def treat(self, page):
    	part = self.titles[page.title()]
    	sec = self.sections[part]
    	new_text = ('' if self.notitle else sec.title) + sec.content
    	page.text = textlib.add_text(page.text, new_text, site=page.site)
    	page.save(self.summary)
    	self.created.append('[[' + page.title() + '|' + part + ']]')
    	

class SplitBot(SingleSiteBot, CurrentPageBot):
    """Implement the split of page to its paragraphs (or by regex)."""
    def __init__(self, generator, **opt):
        self.generator = generator
        super().__init__()
        self.opt.update(opt)
        
        self.opt.summary = 'בוט פיצול: הדף פוצל לדפי משנה'
        if not self.opt.regex and not self.opt.titles:
            raise ValueError("The bot must get '-regex:X' or '-titles' param, "
            "to parse the page sections by.")
        
        if self.opt.base_name:
            self.base_name = self.opt.base_name
        else:
            ask = input_yn("No '-base_name:X' parameter. Do you want to use "
                           "the parent page name as a base name of the new pages?", 
                           default=False)
            if ask:
                self.__class__.base_name = property(lambda self: self.current_page.title() + '/')
            else:
                raise ValueError("No '-base_name:X' parameter.")

    def header_regex(self, max_order=5):
        equals = '='
        equals += '=?' * (max_order-1)
        return re.compile(
                r'(?:(?<=\n)|\A)(?:<!--[\s\S]*?-->)*'
                + equals +
                r'[^=\n](?:[^\n]|<!--[\s\S]*?-->)*='
                r' *(?:<!--[\s\S]*?--> *)*(?=\n|\Z)')
    
    def parse_page(self):
        """Parse the current page by titles or by given regex.
        
        :return: dict of subpages, which every value is textlib._Section
        which contain 'title' and 'content' attributes."""
        textlib._create_default_regexes()
        if self.opt.titles:
            titles = self.header_regex(self.opt.max_order)
        else:
            titles = re.compile(self.opt.regex)

        textlib._regex_cache['header'] = titles
        sections = textlib.extract_sections(self.current_page.text, self.site)

        pages = {}
        for sec in sections.sections:
            if self.opt.titles:
                part = sec.title.strip().strip('=').strip()
            else:
                groups = self.opt.group.split(',')
                groups = '\\' + ' \\'.join(groups)
                part = re.sub(self.opt.regex, groups, sec.title)
                
            i = 2
            while part in pages:
            	part = part + str(i)
            	i += 1
            pages[part] = sec
        return sections.header, pages, sections.footer
    
    def treat_page(self) -> None:
        header, sections, footer = self.parse_page()
        sub_bot = SubpagesBot(parent=self.current_page, base_name=self.base_name,
                          sections=sections, notitle=self.opt.notitle)
        sub_bot.run()
        toc = '==תוכן הספר==\n* ' + '\n* '.join(sub_bot.created)
        self.current_page.text = header + toc + footer
        self.current_page.save(self.opt.summary)


def main(*args: str) -> None:
    """
    Process command line arguments and invoke bot.

    If args is an empty list, sys.argv is used.

    :param args: command line arguments
    """
    local_args = pywikibot.handle_args(args)
    gen_factory = pagegenerators.GeneratorFactory()
    local_args = gen_factory.handle_args(local_args)
    gen = gen_factory.getCombinedGenerator(preload=True)
    if not gen:
        pywikibot.bot.suggest_help(missing_generator=True)
        return
    
    options = DEFAULT_ARGS
    for arg in local_args:
        arg, sep, value = arg.partition(':')
        option = arg[1:]
        if option in ('base_name', 'regex', 'group'):
            options[option] = value
        elif option == 'max_order':
            options[option] = int(value)
        elif option in ('titles', 'notitle', 'always', 'minor'):
            options[option] = True
        elif option == 'major':
            options['minor'] = False
        else:
            raise ValueError(f'"{arg}" is invalid arg.')
    
    bot = SplitBot(generator=gen, **options)
    bot.run()

if __name__ == '__main__':
    main()
