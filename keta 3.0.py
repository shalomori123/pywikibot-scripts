#!/usr/bin/python
"""
A bot to add 'keta' (section) tags to list of pages, according to the paragraphs of the pages, given by regex or automatically.

&params;

Furthermore, the following command line parameters are supported:

generators
general params
-minor (default) / -major
-always

-regex:X (can be non-title, and can be title. must contain group.)
-group:X (1(default)/2/3/1,2/2,3/1,2,3 e.t.c..., group of regex to define as keta name)
-remove_empty (deleting empty sections)
-titles (working auto without regex. the keta name is the title name)

* places to add argument: documentation, DEFAULT_ARGS, local_args in main(), the functionality in the bot class.
"""
import pywikibot
import re
from pywikibot.bot import SingleSiteBot, ExistingPageBot
from pywikibot import textlib
from pywikibot import pagegenerators
#from pywikibot.cosmetic_changes import CosmeticChangesToolkit

docuReplacements = {'&params;': pagegenerators.parameterHelp}  # noqa: N816

DEFAULT_ARGS = {
    'summary': '',
    'always': False,
    'minor': True,
    'titles': False,
    'regex': '',
    'group': '1',
    'remove_empty': False
}

def multistrip(string, *args, left=False, right=False):
	while string[0] in args and not right:
		string = string[1:]
	while string[-1] in args and not left:
		string = string[:-1]
	return string


class KetaTagsBot(SingleSiteBot, ExistingPageBot):
	"""A bot for adding 'keta' (קטע, section) tags to pages.
	including 5 functions:
		remove_empty_sections - to delete titles that hasn't content.
		extract_sections - parses the given regex, and returns the page in a format of sections that defined in textlib.
		keta_names - makes list that contain names for each section, to write inside the tags.
		add_tags - the main function that changes the page content.
		treat - to implement the above functions.
		"""
	def __init__(self, **kwargs):
		super().__init__(generator=kwargs['gen'])
		self.opt.update(kwargs)
		
		if not self.opt.summary:
			self.opt.summary = 'הוספת תגי קטע'
		if not self.opt.regex and not self.opt.titles:
			raise ValueError("The bot must get '-regex:X' or '-titles' param, \
			to parse the page sections by.")
	
	
	def remove_empty_sections(self, page):
		oldtext = page.text
		text = oldtext
		if not self.opt.remove_empty:
			return text
		
		#can be replaced by: (but not working)
		#cctk = CosmeticChangesToolkit(page)
		#text = cctk.removeEmptySections(page.text)
		while re.search('===.*?===\s+?===?[^=]', text):
			text = re.sub('===.*?===\s+?(===?[^=])', '\\1', text)
		while re.search('==.*?==\s+?==[^=]', text):
			text = re.sub('==.*?==\s+?(==[^=])', '\\1', text)
		
		if text != oldtext:
			self.opt.summary = 'הסרת פסקאות ריקות, ' +self.opt.summary
		return text
	
		
	def extract_sections(self, text):
		if not self.opt.titles:
			textlib._create_default_regexes()
			textlib._regex_cache['header'] = re.compile(self.opt.regex)
		return textlib.extract_sections(text, self.site)
	
	
	def keta_names(self, sections):
		titles = [section[0] for section in sections]
		
		if self.opt.titles:
			names = [multistrip(title, ' ', '=') for title in titles]
			return names
		
		groups = self.opt.group.split(',')
		groups = '\\' + ' \\'.join(groups)
		names = [re.sub(self.opt.regex, groups, title) for title in titles] # get the group
		return names
	
	
	def add_tags(self, sections, keta_names):
		'''the main purpose of the bot'''
		new_sections = []
		for i, section in enumerate(sections):
			keta_start = '<קטע התחלה=%s/>' % keta_names[i]
			keta_end = '<קטע סוף=%s/>' % keta_names[i]
			
			#put the tags
			content = section.content
			if keta_start not in content:
				content = keta_start + content
			if keta_end not in content:
				content += keta_end
			
			#reposition the tags
			while '\n'+keta_end in content:
				content = content.replace('\n'+keta_end, keta_end+'\n')
			while keta_start+'\n' in content:
				content = content.replace(keta_start+'\n', '\n'+keta_start)
			while ' '+keta_end in content:
				content = content.replace(' '+keta_end, keta_end+' ')
			while keta_start+' ' in content:
				content = content.replace(keta_start+' ', ' '+keta_start)
			#to avoid damage from titles
			content = content.replace(keta_start+'==', keta_start+'\n==')
			content = content.replace('=='+keta_end, '==\n'+keta_end)
			
			new_section = textlib._Section(section.title, content)
			new_sections.append(new_section)
		return new_sections
	
	
	def treat(self, page):
		if page.isRedirectPage():
			page = page.getRedirectTarget()
		
		oldsummary = self.opt.summary
		oldtext = page.text
		newtext = self.remove_empty_sections(page)
		
		header, sections, footer = self.extract_sections(newtext)
		keta_names = self.keta_names(sections)
		new_sections = self.add_tags(sections, keta_names)
		
		newtext = header + ''.join([x.title + x.content for x in new_sections]) + footer
		self.userPut(page, oldtext, newtext, summary = self.opt.summary, minor = self.opt.minor)
		self.opt.summary = oldsummary


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
    
    bot = KetaTagsBot(gen=gen, **options)
    bot.run()

if __name__ == '__main__':
    main()
