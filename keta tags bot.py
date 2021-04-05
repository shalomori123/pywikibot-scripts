import pywikibot
import re
from pywikibot.bot import (SingleSiteBot, CurrentPageBot, ExistingPageBot, FollowRedirectPageBot)

class KetaTagsBot(SingleSiteBot, ExistingPageBot):
	"""A bot to add 'keta' tags to pages that linked from mainpage of parshan on the shas.
	
	:param mainpage: the main page of the parshan.
	:type mainpage: pywikibot.Page"""
	
	def __init__(self, mainpage, site=pywikibot.Site()):
		super().__init__(site=site)
		self._mainpage = mainpage.title()
		self.generator = mainpage.linkedPages()
	
	def treat(self, page):
		if page.isRedirectPage():
			page = page.getRedirectTarget()
		if page.title().startswith(self._mainpage) \
		or page.title().startswith(self._mainpage.replace(' על הש"ס', '')) \
		or page.title().startswith(self._mainpage + ' על הש"ס'):  #only subpages
			summary = ''
			oldtext = page.text
			
			page.text = re.sub('===.*?===\s+(==)', '\\1', page.text)  # remove empty sections
			page.text = re.sub('===.*?===\s+(==)', '\\1', page.text)
			page.text = re.sub('===.*?===\s+(==)', '\\1', page.text)
			if page.text != oldtext:
				summary += 'הסרת פסקאות ריקות, '
			
			titles = re.findall('==[א-ת \[\]\|=]*?דף ק?[ט-צ]?[א-י]? עמוד [אב][ \[\]]*?===?', page.text)  # add keta tags
			dafs = [re.sub('==[א-ת \[\]\|=]*?דף (ק?[ט-צ]?[א-י]?) עמוד ([אב])[ \[\]]*?===?', '\\1 \\2', title) for title in titles]
			for i,title in enumerate(titles):
				if '<קטע התחלה=%s/>' % dafs[i] in page.text:
					continue
				if i == 0:
					page.text = page.text.replace(title, '%s\n<קטע התחלה=%s/>' % (title, dafs[i]))
				else:
					page.text = page.text.replace(title, 
					'<קטע סוף=%s/>\n%s\n<קטע התחלה=%s/>' % (dafs[i-1], title, dafs[i]))
			if len(dafs) >= 1 and '<קטע סוף=%s/>' % dafs[-1] not in page.text:
				page.text += '\n<קטע סוף=%s/>' % dafs[-1]
			
			newtext = page.text
			summary += 'הוספת תגי קטע'
			self.userPut(page, oldtext, newtext, summary = summary)

site = pywikibot.Site()
# mainpage = pywikibot.Page(site, 'חידושי הרמב"ן על הש"ס')
# mainpage = pywikibot.Page(site, 'חידושי הרשב"א על הש"ס')
# mainpage = pywikibot.Page(site, 'רבינו חננאל על הש"ס')
# mainpage = pywikibot.Page(site, 'רב ניסים גאון על הש"ס')
# mainpage = pywikibot.Page(site, 'חידושי רבינו גרשום על הש"ס')
# mainpage = pywikibot.Page(site, 'רבינו אשר על הש"ס/פירוש הרא"ש/נזיר')
# mainpage = pywikibot.Page(site, 'חידושי הריטב"א על הש"ס')
# mainpage = pywikibot.Page(site, 'תוספות הרא"ש על הש"ס')
# mainpage = pywikibot.Page(site, 'תוספות ר"י הזקן/קידושין')
# mainpage = pywikibot.Page(site, 'תוספות שאנץ')
# mainpage = pywikibot.Page(site, 'מאירי על הש"ס')
# mainpage = pywikibot.Page(site, 'יד רמ"ה על הש"ס')
# mainpage = pywikibot.Page(site, 'תוספות חד מקמאי על יבמות')
# mainpage = pywikibot.Page(site, 'שיטה מקובצת על הש"ס')
# mainpage = pywikibot.Page(site, 'שיטה מקובצת על הש"ס/בבא קמא')
# mainpage = pywikibot.Page(site, 'שיטה מקובצת על הש"ס/בבא מציעא')
# mainpage = pywikibot.Page(site, 'שיטה מקובצת על הש"ס/בבא בתרא')
# mainpage = pywikibot.Page(site, 'שיטה מקובצת על הש"ס/כתובות')
mainpage = pywikibot.Page(site, 'תוספות רי"ד')

bot = KetaTagsBot(mainpage)
bot.run()