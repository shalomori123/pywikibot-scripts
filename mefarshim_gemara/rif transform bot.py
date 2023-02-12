import pywikibot
import re
from pywikibot.bot import (SingleSiteBot, CurrentPageBot, ExistingPageBot, FollowRedirectPageBot)
from pywikibot.pagegenerators import PrefixingPageGenerator

class RifTransformBot(SingleSiteBot, ExistingPageBot):
	def __init__(self):
		super().__init__()
		self.generator = PrefixingPageGenerator('רי"ף')
	
	def treat(self, page):
		if page.isRedirectPage():
			return
		if re.match('רי"ף .*? מהדורת ש"ס ווילנא דף [ט-צ]?[א-י]? ע"[אב]', page.title()):
			new_title = re.sub('רי"ף (.*?) מהדורת ש"ס ווילנא דף ([ט-צ]?[א-י]?) ע"([אב])', 'רי"ף על הש"ס/\\1/דף \\2 עמוד \\3', page.title())
			pywikibot.output('Moving page {} to [[{}]]'.format(page, new_title))
			page.move(new_title, reason='התאמה לפורמט דפי משנה')

bot = RifTransformBot()
bot.run()