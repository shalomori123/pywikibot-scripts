import pywikibot
import re
from pywikibot.bot import (SingleSiteBot, CurrentPageBot, ExistingPageBot, FollowRedirectPageBot)
from pywikibot.pagegenerators import AllpagesPageGenerator

class KetaTransformBot(SingleSiteBot, ExistingPageBot):
	def __init__(self):
		super().__init__()
		self.site = pywikibot.Site()
		self.generator = self.site.allpages(namespace=100, start='עק')
		self.edit_page = pywikibot.Page(self.site, 'טיוטה:דפים כפולים בין המרחבים')
	
	def treat(self, page):
		if not re.match('קטע:(מסורה קטנה|תרגום שני|מסורה גדולה|רש"י|מיוחס לרש\"י|שפ\"ח|רשב\"ם|אבן עזרא|תשובות דונש בן לברט לרב סעדיה גאון|שפת יתר|רד\"ק|רמב\"ן|רבינו בחיי|רלב\"ג|ספורנו|חזקוני|בכור שור|רבנו יונה|אברבנאל|רבי ישעיה די טראני|מלבי\"ם|אלשיך|חיד\"א|כלי יקר|אור החיים|הגאון מווילנה|רבי יוסף אבן כספי|רבי יוסף קרא|מגילת סתרים|מצודות|מצודת ציון|מצודת דוד|העמק דבר|משה דוד ואלי|תו\"א|תולדות אהרן|מכילתא|ספרא|ספרי|התורה והמצוה|ילקוט שמעוני|מנחת שי|בעל הטורים|נחמיאש) על (בראשית|שמות|ויקרא|במדבר|דברים|יהושע|שופטים|שמואל א|שמואל ב|מלכים א|מלכים ב|ישעיהו|ירמיהו|יחזקאל|תרי עשר|הושע|יואל|עמוס|עובדיה|יונה|מיכה|נחום|חבקוק|צפניה|חגי|זכריה|מלאכי|תהלים|משלי|איוב|שיר השירים|רות|אסתר|קהלת|איכה|דניאל|עזרא|נחמיה|דברי הימים א|דברי הימים ב|ישעיה|ירמיה|תהילים)( ק?[ט-צ]?[א-י]?){2}', page.title()) \
		and not re.match('קטע:(יפה תואר|עץ יוסף|רש"י) על בראשית רבה(/[ט-ק]?[א-י]?){2}', page.title()):
			print(page.title(), 'skipped')
			return
		
		new_title = page.title().replace('קטע:', '')
		
		if page.isRedirectPage():
			redirect_to = page.getRedirectTarget()
			if redirect_to.title() == new_title:
				print(page.title(), 'already moved')
				return
		
		if pywikibot.Page(self.site, new_title).exists():
			pywikibot.output('New title: "{}" is already exists!'.format(new_title))
			if new_title in self.edit_page.text:
				return
			self.edit_page.text += '\n* [[קטע:{}]] ← [[{}]]'.format(new_title, new_title)
			self.edit_page.save()
			return

		pywikibot.output('Moving page {} to [[{}]]'.format(page, new_title))
		page.move(new_title, reason='העברה בעקבות ביטול מרחב השם "קטע"')

bot = KetaTransformBot()
bot.run()