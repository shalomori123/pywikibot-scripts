import pywikibot
import pywikibot.pagegenerators

site = pywikibot.Site()
cat = pywikibot.Category(site, 'קטגוריה:תבניות מפרשים למסכת')
pages = pywikibot.pagegenerators.CategorizedPageGenerator(cat, content=True)
for page in pages:
	content = page.text
	page_title = page.title()
	list_page = page_title.split(' ', 2)
	masechet = list_page[-1]
	print(page_title)
	
	content = content.replace('{{#תנאי:{{התאמת מחרוזות|{{שם הדף}}|בבלי %s פרק}}||' % masechet, '{{#שווה:{{{מפרשים בלבד|}}}|כן||')
	
	page.text = content
	page.save(summary='שימוש בפרמטר')
print('mission completed!')