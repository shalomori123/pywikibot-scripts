import pywikibot
from pywikibot.bot import SingleSiteBot
import re

site = pywikibot.Site()
temp = pywikibot.Page(site, 'תבנית:דף קישור')
gen = temp.getReferences(only_template_inclusion=True)

class DeleteLinkBot(SingleSiteBot):
	def __init__(self):
		self.generator = gen
		super().__init__()
	
	def treat(self, page):
		temp = re.search('\{\{דף קישור\|(.*?)(\||\}\})', page.text)
		if temp is not None:
			link = temp.group(1)
		else:
			return
		
		redirs = page.redirects()
		redirs_names = [redir.title().replace('(', '\(').replace(')', '\)') for redir in redirs]
		redirs_names.extend([redir.title().replace('(', '\(').replace(')', '\)').replace(' ', '_') for redir in redirs])
		redirs_names.append(page.title())
		title_regex = '(' + '|'.join(redirs_names) + ')'
		
		refs = page.getReferences(content=True)
		for ref in refs:
			ref.text = re.sub('\[\[' + title_regex + '\|(.*?)\]\]', '['+link+' \\2]', ref.text)
			ref.text = re.sub('\[\[' + title_regex + '\]\]', '['+link+' '+page.title()+']', ref.text)
			ref.save('שינוי קישור פנימי לחיצוני, לדף שנמחק')
		
		page.delete('מחיקת דפי {{דף קישור}}, על פי דיון במזנון')
		print(page, 'deleted!')
		for redir in redirs:
			redir.delete('מחיקת הפניה לדף של {{דף קישור}}, על פי דיון במזנון')
			print(redir, 'deleted!')

bot = DeleteLinkBot()
bot.run()