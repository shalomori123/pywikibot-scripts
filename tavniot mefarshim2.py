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
	
	content = content.replace('{{#שווה:{{שם דף הבסיס}}|בבלי %s פרק||' % masechet, '{{#תנאי:{{#invoke:String|match|{{שם הדף}}|בבלי %s פרק|nomatch=}}||' % masechet)
	
	page.text = content
	page.save(summary='תיקון. כך כנראה יעבוד')
	print(page.title(), 'נערך')