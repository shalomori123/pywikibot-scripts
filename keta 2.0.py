#!/usr/bin/python
"""
A bot to add 'keta' (section) tags to list of pages, according to the paragraphs of the pages, given by regex.

&params;

Furthermore, the following command line parameters are supported:

generators
general params
-minor (default) / -major
-always

-regex:X (can be non-title, and can be title with the prev param, to give newline)
-group:X (1(default)/2/3/1,2/2,3/1,2,3 e.t.c..., group of regex to define as keta name)
-remove_empty 
not implemented: -titles (check if it works auto)

* places to add argument: documentation, DEFAULT_ARGS, local_args in main(), the functionality in the bot class.
	
"""
import pywikibot
import re
from pywikibot.bot import (SingleSiteBot, ExistingPageBot)
from pywikibot import textlib
from pywikibot import pagegenerators

docuReplacements = {'&params;': pagegenerators.parameterHelp}  # noqa: N816

DEFAULT_ARGS = {
    'summary': '',
    'always': False,
    'minor': True,
    'titles': False, #not implemented
    'regex': '',
    'group': '1',
    'remove_empty': False
}

class KetaTagsBot(SingleSiteBot, ExistingPageBot):
	"""A bot for adding 'keta' (קטע, section) tags to pages.
	including 4 functions:
		remove_empty_sections - to delete titles that hasn't content.
		page_sections - parses the given regex, and gives the titles in the page, and the name of the section to write inside the tags.
		add_tags - the main function that changes the page content.
		treat - to implement the above functions.
	
	The class must get a regex to parse the page sections by, and any generator.
	these given as args in the command prompt."""
	def __init__(self, **kwargs):
		super().__init__(generator=kwargs['gen'])
		self.opt.update(kwargs)
		
		if not self.opt.summary:
			self.opt.summary = 'הוספת תגי קטע'
		if not self.opt.regex:
			raise ValueError('The bot must get any regex to parse the page sections by.')
	
	
	def remove_empty_sections(self, text):
		oldtext = text
		while re.search('===.*?===\s+?===?[^=]', text):
			text = re.sub('===.*?===\s+?(===?[^=])', '\\1', text)
		while re.search('==.*?==\s+?==[^=]', text):
			text = re.sub('==.*?==\s+?(==[^=])', '\\1', text)
		
		if text != oldtext:
			self.opt.summary = 'הסרת פסקאות ריקות, ' +self.opt.summary
		return text
		
	
	def page_sections(self, text):
		regex = self.opt.regex
		title_iter = re.finditer(regex, text)
		titles = [x.group() for x in title_iter] # get all the matches
		titles = list(dict.fromkeys(titles)) # remove duplicates. in testing todo
		
		groups = self.opt.group.split(',')
		groups = '\\' + ' \\'.join(groups)
		keta_names = [re.sub(regex, groups, title) for title in titles] # get the group
		return titles, keta_names
	
	
	def add_tags(self, text, titles, keta_names):
		'''the main purpose of the bot'''
		for i,title in enumerate(titles):
			keta_start = '<קטע התחלה=%s/>' % keta_names[i]
			prev_end = '<קטע סוף=%s/>' % keta_names[i-1]
			
			if keta_start in text:
				if i == 0 or prev_end in text:
					continue
				else:
					text = text.replace(title, prev_end + '\n' + title, 1)
			elif i == 0 or prev_end in text:
				text = text.replace(title, title + '\n' + keta_start, 1)
			else:
				text = text.replace(title, prev_end + '\n' + title + '\n' + keta_start, 1)
		
		if len(keta_names) >= 1 and '<קטע סוף=%s/>' % keta_names[-1] not in text:
			text = textlib.add_text(text, '<קטע סוף=%s/>' % keta_names[-1])
		
		while re.search('[^=]\n<קטע סוף', text):
			text = re.sub('([^=])\n(<קטע סוף=.*?/>)', '\\1\\2\n', text)
		
		return text
	
	
	def treat(self, page):
		if page.isRedirectPage():
			page = page.getRedirectTarget()
		
		oldtext = page.text
		
		if self.opt.remove_empty:
			page.text = self.remove_empty_sections(page.text)
		
		titles, keta_names = self.page_sections(page.text)
		page.text = self.add_tags(page.text, titles, keta_names)
		
		newtext = page.text
		self.userPut(page, oldtext, newtext, summary = self.opt.summary, minor = self.opt.minor)



def main(*args: str) -> None:
    """
    Process command line arguments and invoke bot.

    If args is an empty list, sys.argv is used.

    :param args: command line arguments
    """
    options = DEFAULT_ARGS
    
    local_args = pywikibot.handle_args(args)
    gen_factory = pagegenerators.GeneratorFactory()
    local_args = gen_factory.handle_args(local_args)
    gen = gen_factory.getCombinedGenerator(preload=True)
    if not gen:
    	pywikibot.bot.suggest_help(missing_generator=True)
    	return
    
    for arg in local_args:
        arg, sep, value = arg.partition(':')
        option = arg[1:]
        if option in ('regex', 'group'):
            options[option] = value
        elif option in ('titles', 'remove_empty', 'minor', 'always'):
            options[option] = True
        elif option == 'major':
        	options['minor'] = False
        else:
        	raise ValueError(f'"{option}" is invalid arg.')
    
    bot = KetaTagsBot(gen=gen, **options)
    bot.run()

if __name__ == '__main__':
    main()
