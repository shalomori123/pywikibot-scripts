import pywikibot
from pywikibot.bot import (SingleSiteBot, ExistingPageBot)
from pywikibot.pagegenerators import CategorizedPageGenerator

class ShvilTransformBot(SingleSiteBot, ExistingPageBot):
	def __init__(self):
		super().__init__()
		self.site = pywikibot.Site()
		cat = pywikibot.Category(self.site, 'קטגוריה:ספר המילים של שבי"ל')
		self.generator = CategorizedPageGenerator(cat, namespaces=0)
	
	def treat(self, page):
		if page.isRedirectPage():
			return
		new_title = 'ביאור:' + page.title()
		counter = 0
		if pywikibot.Page(self.site, new_title).exists():
			counter += 1
			print(counter, page)
			return
		pywikibot.output('Moving page {} to [[{}]]'.format(page, new_title))
		page.move(new_title, reason='העברה למרחב ביאור')

bot = ShvilTransformBot()
bot.run()