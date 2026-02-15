import pywikibot
import re
from pywikibot.bot import (SingleSiteBot, ExistingPageBot)
from pywikibot import textlib
from pywikibot.pagegenerators import PrefixingPageGenerator

class KetaTagsBot(SingleSiteBot, ExistingPageBot):
	"""A bot to add 'keta' (section) tags to pages that linked from mainpage of any book, or according to prefix.
	
	:param mainpage: the title name of the main page of the books.
	:type mainpage: string
	:param prefix: instead of main page you can use prefix index in the site.
	:type prefix: string
	"""
	
	def __init__(self, mainpage, prefix='', site=pywikibot.Site()):
		super().__init__(site=site)
		
		if prefix:
			self.generator = PrefixingPageGenerator(prefix)
		else:
			self._mainpage = mainpage
			self.mainpage = pywikibot.Page(site, mainpage)
			self.generator = self.mainpage.linkedPages()
	
	
	def append_bottom(self, page, addtext, site=pywikibot.Site()):
		"""to add text before the Categories and interwiki. copied from scripts/add_text.
		
		params:
		:param page: the page to append to.
		:param addtext: the text to add."""
		
		# Getting the categories
		categoriesInside = textlib.getCategoryLinks(page.text, site)
		# Deleting the categories
		page.text = textlib.removeCategoryLinks(page.text, site)
		# Getting the interwiki
		interwikiInside = textlib.getLanguageLinks(page.text, site)
		# Removing the interwiki
		page.text = textlib.removeLanguageLinks(page.text, site)
		# Adding the text
		page.text += addtext
		# Reputting the categories
		page.text = textlib.replaceCategoryLinks(page.text, categoriesInside, site, True)
		# Adding the interwiki
		page.text = textlib.replaceLanguageLinks(page.text, interwikiInside, site)
	
	
	def page_sections(self, page):
		'''returns tuple includes two lists. the first list includes the relevant titles that need tags, and the second includes the names of tags for each title'''
		
		#titles = re.findall('==[א-ת \[\]\|=]*?דף ק?[ט-צ]?[א-י]? עמוד [אב][ \[\]]*?===?', page.text)
		#keta_names = [re.sub('==[א-ת \[\]\|=]*?דף (ק?[ט-צ]?[א-י]?) עמוד ([אב])[ \[\]]*?===?', '\\1 \\2', title) for title in titles] # for gemara's mefaresh
			
		#titles = re.findall('==[א-ת \/\"\[\]\|=]*?דף ק?[ט-צ]?[א-י]? עמוד [אב][ \[\]]*?===?', page.text)
		#keta_names = [re.sub('==[א-ת \/\"\[\]\|=]*?דף (ק?[ט-צ]?[א-י]?) עמוד ([אב])[ \[\]]*?===?', '\\1 \\2', title) for title in titles] # for ran on rif
		
		# regex with group that means the keta name
		
		#regex = '=== ?סעיף (ק?[ט-צ]?[א-ט]?) ?===' # for taz on shulhan aruch
		#regex = '== ?(ק?[ט-צ]?[א-ט]?) ?==' # for seforno and more
		#regex = "\n'''\(([ט-פ]?[א-ט]?)\)\. " # for rashbam
		#regex = "\n(<קטע התחלה ?= ?פרשת [א-ת ]*/>|)\(([ט-פ]?[א-ט]?)\) " # for or hachaim
		#regex = '== ?פסוק ([ט-פ]?[א-ט]?) ?==' # for kli yakar
		#regex = '==[א-ת \/\"\[\]\|=]*?פסוק ([ט-פ]?[א-ט]?)[ \[\]]*?===?' # for rabeinu behaye
		#regex = "\n\(([ט-פ]?[א-ט]?)\) " # for baal haturim
		#regex = "\n[\(\{]([ט-פ]?[א-ט]?).*?[\)\}] " # for malbim
		#regex = '=== ?משנה ([ט-צ]?[א-ט]?) ?===' # for magen avot
		#regex = '==[א-ת \[\]\|\/"=]*?דף (ק?[ט-צ]?[א-י]?) עמוד ([אב])[ \[\]]*?===?' # for gemara's mefaresh
		#regex = ' ?\{\{דף רי"ף\|([ט-צ]?[א-ט]?)\|([אב])\}\} ?' # rif
		#regex = '==[א-ת \/\"\[\]\|=]*?דף (ק?[ט-צ]?[א-י]?) עמוד ([אב])[ \[\]]*?===?' # ran on rif
		regex = '===? ?([ק-ת]?[ט-צ]?[א-ט]?) ?===?' #sikhot haran
		#regex = '(\(.*?\)\n\n)*(\(.*?\) )?\[[ט-צ]?[א-ט]?, ([ט-צ]?[א-ט]?)\] '#ben sira
		#regex = '=== ?פסוק (ק?[ט-צ]?[א-ט]?) ?===' #ibn ezra
		
		title_iter = re.finditer(regex, page.text)
		titles = [x.group() for x in title_iter] # get all the matches
		keta_names = [re.sub(regex, '\\1', title) for title in titles] # get the group
		#keta_names = [re.sub(regex, '\\2', title) for title in titles]
		#keta_names = [re.sub(regex, '\\1 \\2', title) for title in titles]
		
		return titles, keta_names
	
	
	def treat(self, page):
		if page.isRedirectPage():
			page = page.getRedirectTarget()
		#if not page.title().startswith(self._mainpage) \
		#and not page.title().startswith(self._mainpage.replace(' על הש"ס', '')) \
		#and not page.title().startswith(self._mainpage + ' על הש"ס'):
			#print(page, 'is not subpage of the main page. skipping')
			#return  #only subpages
		
		summary = ''
		oldtext = page.text
		
		# remove empty titles
		while re.search('===.*?===\s+?===?[^=]', page.text):
			page.text = re.sub('===.*?===\s+?(===?[^=])', '\\1', page.text)
		while re.search('==.*?==\s+?==[^=]', page.text):
			page.text = re.sub('==.*?==\s+?(==[^=])', '\\1', page.text)
		if page.text != oldtext:
			summary += 'הסרת פסקאות ריקות, '
		
		# add keta tags
		titles, keta_names = self.page_sections(page)
			
		for i,title in enumerate(titles):
			#print(title)
			if '<קטע התחלה=%s/>' % keta_names[i] in page.text:
				if i == 0 or '<קטע סוף=%s/>' % keta_names[i-1] in page.text:
					continue
				else:
					page.text = page.text.replace(title, 
					'<קטע סוף=%s/>%s\n' % (keta_names[i-1], title))
					continue
			
			if i == 0 or '<קטע סוף=%s/>' % keta_names[i-1] in page.text:
				page.text = page.text.replace(title, '%s\n<קטע התחלה=%s/>' % (title, keta_names[i]))
			else:
				page.text = page.text.replace(title, 
				'<קטע סוף=%s/>%s\n<קטע התחלה=%s/>' % (keta_names[i-1], title, keta_names[i]))
		
		if len(keta_names) >= 1 and '<קטע סוף=%s/>' % keta_names[-1] not in page.text:
			self.append_bottom(page, '<קטע סוף=%s/>' % keta_names[-1])
		
		while re.search('[^=]\n<קטע סוף', page.text):
			page.text = re.sub('([^=])\n(<קטע סוף=.*?/>)', '\\1\\2\n', page.text)
		
		newtext = page.text
		summary += 'הוספת תגי קטע'
		self.userPut(page, oldtext, newtext, summary = summary)


mainpage = ''
prefix = ''

# mainpage = 'חידושי הרמב"ן על הש"ס'
# mainpage = 'חידושי הרשב"א על הש"ס'
# mainpage = 'רבינו חננאל על הש"ס'
# mainpage = 'רב ניסים גאון על הש"ס'
# mainpage = 'חידושי רבינו גרשום על הש"ס'
# mainpage = 'רבינו אשר על הש"ס/פירוש הרא"ש/נזיר'
# mainpage = 'חידושי הריטב"א על הש"ס'
# mainpage = 'תוספות הרא"ש על הש"ס'
# mainpage = 'תוספות ר"י הזקן/קידושין'
# mainpage = 'תוספות שאנץ'
# mainpage = 'מאירי על הש"ס'
# mainpage = 'יד רמ"ה על הש"ס'
# mainpage = 'תוספות חד מקמאי על יבמות'
# mainpage = 'שיטה מקובצת על הש"ס'
# mainpage = 'שיטה מקובצת על הש"ס/בבא קמא'
# mainpage = 'שיטה מקובצת על הש"ס/בבא מציעא'
# mainpage = 'שיטה מקובצת על הש"ס/בבא בתרא'
# mainpage = 'שיטה מקובצת על הש"ס/כתובות'
# mainpage = 'תוספות רי"ד'
# mainpage = 'ר"ן על הרי"ף'
# prefix = 'ספורנו/'
# prefix = 'רש"ש על המשנה/'
# prefix = 'אבי עזר/'
# mainpage = 'בעל הטורים על התורה'
# prefix = 'מגן אבות (רשב"ץ)/חלק ד/פרק '
# prefix = 'מדרש שמואל (אוזידא)/'
# prefix = 'חידושי הרמב"ם על ראש השנה'
# prefix = 'עורך מתחיל/נימוקי יוסף'
# prefix = 'רי"ף על הש"ס/'
# prefix = 'ר"ן על הרי"ף/שבועות/פרק'
# prefix = 'שיחות הר"ן/שלם'
# prefix = 'אבן עזרא על תהלים'
# prefix = 'השתפכות הנפש/הכל'
#prefix = 'השגות הראב"ד על הרי"ף/ברכות'
#prefix = 'שלטי הגיבורים על הרי"ף/ברכות'
#prefix = 'רש"י על הרי"ף/ברכות'
#prefix = 'תלמידי רבנו יונה על הרי"ף'
prefix = 'חיי מוהר"ן/ספר שלם'

mainpage = 'משתמש:Shalomori123/קישורים לבוט'

bot = KetaTagsBot(mainpage, prefix=prefix)
bot.run()