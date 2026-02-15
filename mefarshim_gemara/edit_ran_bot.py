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
		while '\n ' in page.text:
			page.text = page.text.replace('\n ', '\n')
		
		page.text = re.sub('הר"ן על הרי"ף מסכת (.*?) (דף [ט-צ]?[א-י]? עמוד [אב])', '===[[רי"ף על הש"ס/\\1/\\2|\\2]]===', page.text)
		
		title_list = page.title().split('/')
		page.text = '{{מפרשים למסכת %s|ר"ן על הרי"ף|%s}}\n{{תוכן עניינים שטוח}}\n\n' % (title_list[1], title_list[2].replace('פרק ', '')) + page.text
		
		newtext = page.text
		summary = 'עריכת הר"ן, כותרות, תבניות ועוד'
		self.userPut(page, oldtext, newtext, summary = summary)

bot = RanEditBot()
bot.run()
