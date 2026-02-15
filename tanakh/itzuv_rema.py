import pywikibot
import pywikibot.pagegenerators
import re

list = []
site = pywikibot.Site()
user_page = pywikibot.Page(site, 'משתמש:Shalomori123/דפי שו"ע עם רמ"א לא מעוצב')
for tur in ['אורח חיים', 'יורה דעה', 'אבן העזר', 'חושן משפט']:
	cat = pywikibot.Category(site, 'קטגוריה:שולחן ערוך ' + tur)
	pages = pywikibot.pagegenerators.CategorizedPageGenerator(cat, content=True)
	for page in pages:
		content = page.text
		page_title = page.title()
		if re.search('\n:[^\{][^\{]', content):
			list.append(page_title)
			print(page_title, 'נוסף לרשימה')
	user_page.text += '==' + tur + '==' + '\n[[' + ']], [['.join(list) + ']]'
	print('רשימת' + tur + 'נוספה בהצלחה')
	list = []
user_page.save()