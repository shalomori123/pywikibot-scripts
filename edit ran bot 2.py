import pywikibot
import re
from pywikibot.bot import (SingleSiteBot, CurrentPageBot, ExistingPageBot, FollowRedirectPageBot)
from pywikibot.pagegenerators import PrefixingPageGenerator

class RanEditBot(SingleSiteBot, ExistingPageBot):
	def __init__(self):
		super().__init__()
		self.generator = PrefixingPageGenerator('ר"ן על הרי"ף')
	
	def treat(self, page):
		if page.isRedirectPage():
			return
		if not re.match('.*?/.*?/.*?', page.title()):
			return
			
		oldtext = page.text
		
		page.text = re.sub('\n ([\S ]*?)\.', '\n{{דה מפרש2|\\1}}', page.text)
		page.text = page.text.replace(' ', ' ')
		while '\n ' in page.text:
			page.text = page.text.replace('\n ', '\n')
		
		newtext = page.text
		summary = '{{דה מפרש2}}'
		self.userPut(page, oldtext, newtext, summary = summary)

bot = RanEditBot()
bot.run()
