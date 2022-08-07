import pywikibot
import re
from pywikibot.bot import (SingleSiteBot, CurrentPageBot, ExistingPageBot, FollowRedirectPageBot)
from pywikibot.pagegenerators import PrefixingPageGenerator

class CafHahaimTransformBot(SingleSiteBot, ExistingPageBot):
	def __init__(self):
		super().__init__()
		self.generator = PrefixingPageGenerator('כף החיים')
	
	def treat(self, page):
		if page.isRedirectPage():
			return
		if re.match('כף החיים על אורח חיים ת?[ק-ת]?[ט-צ]?[א-י]?', page.title()):
			new_title = re.sub('כף החיים על אורח חיים (ת?[ק-ת]?[ט-צ]?[א-י]?)', 'כף החיים/אורח חיים/\\1', page.title())
			pywikibot.output('Moving page {} to [[{}]]'.format(page, new_title))
			page.move(new_title, reason='התאמה לפורמט דפי משנה')

bot = CafHahaimTransformBot()
bot.run()