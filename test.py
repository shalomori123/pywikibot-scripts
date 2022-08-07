import pywikibot
from pywikibot import textlib

#class TestBot(pywikibot.Bot):
#	def __init__(self, **kwargs):
#		self.generator = site.allpages()
#		super().__init__(**kwargs)
#	
#	def treat(self, page):
#		textlib.extract_sections(page.text)

site = pywikibot.Site()
#bot = TestBot(site=site)
#bot.run()

#for page in site.allpages():
print(textlib.extract_sections('', site))