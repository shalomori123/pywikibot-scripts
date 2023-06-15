import re

import pywikibot
from pywikibot import textlib, pagegenerators
from pywikibot.bot import SingleSiteBot, CurrentPageBot, input_yn


DEFAULT_ARGS = {
    'base_name': '',
    'titles': False,
    'max_order': 5,
    'regex': '',
    'group': '1',
    'noinclude_titles': False,
    'always': False,
    'minor': False,
}

#pagename = 'משתמש:Shalomori123/טיוטה'
#pagename = 'שו"ת רדב"ז/חלק ד'
#pagename = 'אור חדש/6'
#pagename = 'הגהות רבי עקיבא איגר/יורה דעה'
#pagename= 'גור אריה על בראשית/9'
#pagename= 'גור אריה על שמות/8'
#pagename= 'גור אריה על ויקרא/6'
#pagename= 'גור אריה על במדבר/5'
#pagename= 'גור אריה על דברים/4'
#pagename = 'טיוטה:סמ"ק'
pagename = 'טיוטה:הגהות רבינו פרץ'

max_order = 2
notitle = True
basename = 'הגהות רבינו פרץ על סמ"ק/'
if not basename:
    basename = pagename + '/'
summary = 'בוט פיצול: פוצל מתוך דף [[' + pagename + ']]'

site = pywikibot.Site()
page = pywikibot.Page(site, pagename)
textlib._create_default_regexes()
textlib._regex_cache['header'] = header_regex(max_order)
sections = textlib.extract_sections(page.text, site)
links = []
for sec in sections.sections:
    part = sec.title.strip().strip('=').strip()
    new_name = basename + part
    sec_page = pywikibot.Page(site, new_name)
    new_text = ('' if notitle else sec.title) + sec.content
    #if not sec_page.exists():
    sec_page.text = textlib.add_text(sec_page.text, new_text, site=site)
    sec_page.save(summary)
    links.append('[[' + new_name + '|' + part + ']]')

print(links)
toc = '==תוכן הספר==\n* ' + '\n* '.join(links)
page.text = sections.header + toc + sections.footer
page.save('בוט פיצול: הדף פוצל לדפי משנה')
print('completed!')

class SubpagesBot(SingleSiteBot):
    """Subbot to create the subpages."""
    pass
    self.opt.summary = 'בוט פיצול: פוצל מתוך דף [[' + pagename + ']]'
    self.links = []

class SplitBot(SingleSiteBot, CurrentPageBot):
    """Implement the split of page to its paragraphs (or by regex)."""
    def __init__(self, **kwargs):
        super().__init__(generator=kwargs['gen'])
        self.opt.update(kwargs)
        
        self.opt.summary = 'בוט פיצול: הדף פוצל לדפי משנה'
        if not self.opt.regex and not self.opt.titles:
            raise ValueError("The bot must get '-regex:X' or '-titles' param, "
            "to parse the page sections by.")
        
        if not self.opt.base_name:
            ask = input_yn("No '-base_name:' parameter. Do you want to use "
                           "the big page name as the base name of subpages?", 
                           default=False)
            if ask:
                self.opt.base_name = property(lambda self: self.current_page.title())
            else:
                raise ValueError("No '-base_name:' parameter.")

    def header_regex(self, max_order=5):
        equals = '='
        equals += '=?' * (max_order-1)
        return re.compile(
                r'(?:(?<=\n)|\A)(?:<!--[\s\S]*?-->)*'
                + equals +
                r'[^=\n](?:[^\n]|<!--[\s\S]*?-->)*='
                r' *(?:<!--[\s\S]*?--> *)*(?=\n|\Z)')
    
    def parse_page(self):
        pass
    
    def treat_page(self) -> None:
        sections = self.parse_page()
        bot = SubpagesBot(self.current_page.site, base_name=self.opt.base_name,
                          sections=sections, no_title=self.opt.noinclude_titles)
        self.current_page.text = '==תוכן הספר==\n* ' + '\n* '.join(bot.links)
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
        if option in ('regex', 'group', 'summary'):
            options[option] = value
        elif option in ('titles', 'remove_empty', 'minor', 'always'):
            options[option] = True
        elif option == 'major':
            options['minor'] = False
        else:
            raise ValueError(f'"{arg}" is invalid arg.')
    
    bot = SplitBot(gen=gen, **options)
    bot.run()

if __name__ == '__main__':
    main()
