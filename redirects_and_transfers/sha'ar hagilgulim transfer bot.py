import pywikibot
import re
from pywikibot.bot import (SingleSiteBot, CurrentPageBot, ExistingPageBot, FollowRedirectPageBot)


class ShaarHagilgulimTransformBot(SingleSiteBot, ExistingPageBot):
	def __init__(self):
		super().__init__()
		
		self.site = pywikibot.Site()
		mainpage = pywikibot.Page(self.site, 'משתמש:Shalomori123/קישורים לבוט')
		self.generator = mainpage.linkedPages()
	
	def treat(self, page):
		if page.isRedirectPage():
			return
		
		old_title = page.title()
		new_title = old_title.replace('שער הגלגולים הקדמה', 'שער הגלגולים/הקדמה')
		pywikibot.output('Moving page {} to [[{}]]'.format(page, new_title))
		page.move(new_title, reason='התאמה לפורמט דפי משנה')
		
		new_page = pywikibot.Page(self.site, new_title)
		if '{{סרגל ניווט|' in new_page.text:
			re.sub('\{\{סרגל ניווט\|.*\n', '{{שער הגלגולים}}', new_page.text)
		else:
			new_page.text = '{{שער הגלגולים}}\n' + new_page.text
		new_page.save(summary = '{{שער הגלגולים}}')

bot = ShaarHagilgulimTransformBot()
bot.run()