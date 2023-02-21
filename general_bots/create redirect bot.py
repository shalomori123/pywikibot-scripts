#!/usr/bin/python
"""
A bot for massive creation of redirects to specific pages, given by regex or simple replacing of text, by manipulating the original page name.

&params;

Furthermore, the following command line parameters are supported:

generators
general params

-change:X - current names of orginal page
-to:X - new names for redirect
-always
-regex

* places to add argument: documentation, DEFAULT_ARGS, local_args in main(), the functionality in the bot class.
"""
import pywikibot
import re
from pywikibot.bot import SingleSiteBot, ExistingPageBot
from pywikibot import pagegenerators

docuReplacements = {'&params;': pagegenerators.parameterHelp}  # noqa: N816

DEFAULT_ARGS = {
    'summary': '',
    'always': False,
    'regex': False,
    'change': '',
    'to': ''
}


class CreateRedirectsBot(SingleSiteBot, ExistingPageBot):
	def __init__(self, **kwargs):
		self.use_redirects = False
		
		super().__init__(generator=kwargs['gen'])
		self.opt.update(kwargs)
		
		if not self.opt.change or not self.opt.to or self.opt.change == self.opt.to:
			raise ValueError("The bot must get '-change:X' and '-to:X' params, "
			"to move the pages by.")
		if not self.opt.summary:
			self.opt.summary = input('insert a summary: ')
		
	def newname(self, page):
		if self.opt.regex:
			title = re.sub(self.opt.change, self.opt.to, page.title())
		else:
			title = page.title().replace(self.opt.change, self.opt.to)
		return title
		
	def treat(self, page):
		new_title = self.newname(page)
		if new_title == page.title():
			pywikibot.output('Skipping page {}, redirect name is the same.'.format(page))
			self.counter['skip'] += 1
			return
		
		redir = pywikibot.Page(page.site, new_title)
		
		if redir.exists():
			pywikibot.output('Skipping page {}, page [[{}]] already exists!'.format(page, new_title))
			self.counter['exists'] += 1
			return
		
		print('\nAbout to create redirect:')
		pywikibot.showDiff(page.title(), new_title)
		if not self.user_confirm('Do you want to create this redirect?'):
			pywikibot.output('Skipping page {}'.format(page))
			self.counter['skip'] += 1
			return
		
		redir.text = '#הפניה [[' + page.title() + ']]'
		redir.save(summary=self.opt.summary)
		self.counter['create'] += 1


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
        if option in ('change', 'to', 'summary'):
            options[option] = value
        elif option in ('regex', 'always'):
            options[option] = True
        else:
        	raise ValueError(f'"{arg}" is invalid arg.')
    
    bot = CreateRedirectsBot(gen=gen, **options)
    bot.run()

if __name__ == '__main__':
    main()
