import re
import pywikibot
from pywikibot.pagegenerators import CategorizedPageGenerator
from pywikibot.bot import SingleSiteBot

site = pywikibot.Site()
cat = pywikibot.Category(site, 'קטגוריה:הלכה במשנה תורה לרמב"ם')

class HalachaRambamBot(SingleSiteBot):
	def __init__(self):
		self.generator = CategorizedPageGenerator(cat)
		super().__init__()
	
	def treat(self, page):
		oldtext = page.text
		
		shiluv = ''
		already_done = False
		realtext = re.sub('\{\{רמב"ם הלכה\|.*?\}\}', '', oldtext)
		if realtext == '':
			already_done = True
		realtext = re.sub('\{\{.*?דפוס\}\}', '', realtext)
		realtext = realtext.replace('{{תבנית:אין טקסט למפרשי הרמב"ם}}', '')
		realtext = re.sub('\=\=.*?\=\=', '', realtext)
		if re.search('[א-ת]', realtext):
			shiluv = '\n{{דרוש שילוב}}'
		
		cat_toc = ''
		page.text = page.text.replace('|[[#רמב"ם|לשון הרמב"ם]] · [[#מפרשי הרמב"ם|מפרשי הרמב"ם]]', '')
		if page.text == oldtext and not already_done:
			cat_toc = '[[קטגוריה:תוכן עניינים שונה ברמב"ם]]'
		
		reg_page = re.fullmatch('(\{\{רמב"ם הלכה\|.*?\}\})([\s\S]*?)', page.text)
		if reg_page is None:
			page.text += '[[קטגוריה:תבנית לא תקינה ברמב"ם]]'
		elif '\n{{דרוש שילוב}}' in oldtext:
			page.text = oldtext.replace('|[[#רמב"ם|לשון הרמב"ם]] · [[#מפרשי הרמב"ם|מפרשי הרמב"ם]]', '')
		else:
			temp = reg_page.group(1)
			rest = reg_page.group(2)
			if shiluv:
				page.text = temp + shiluv + rest + cat_toc
			else:
				page.text = temp + cat_toc
		self.userPut(page, oldtext, page.text, summary = 'הסרת התוכן שמחוץ לתבנית כדי להעבירו אל תוך התבנית')

HalachaRambamBot().run()