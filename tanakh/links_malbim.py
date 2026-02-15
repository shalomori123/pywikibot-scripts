import pywikibot
import re
from pywikibot.pagegenerators import PrefixingPageGenerator

site = pywikibot.Site()
edit_page = pywikibot.Page(site, 'משתמש:Shalomori123/קישורים לבוט')
for page in PrefixingPageGenerator('מלבי"ם על '):
	if re.fullmatch('מלבי"ם על (בראשית|שמות|ויקרא|במדבר|דברים|יהושע|שופטים|שמואל א|שמואל ב|מלכים א|מלכים ב|ישעיהו|ירמיהו|יחזקאל|תרי עשר|הושע|יואל|עמוס|עובדיה|יונה|מיכה|נחום|חבקוק|צפניה|חגי|זכריה|מלאכי|תהלים|משלי|איוב|שיר השירים|רות|אסתר|קהלת|איכה|דניאל|עזרא|נחמיה|דברי הימים א|דברי הימים ב) ק?[ט-צ]?[א-י]?', page.title()):
		edit_page.text += str(page)
		print(page, 'added')
edit_page.save()