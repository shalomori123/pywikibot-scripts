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
	
	content = content.replace('פרקים:{{ררר}}', '{{#שווה:{{שם דף הבסיס}}|בבלי %s פרק||פרקים:{{ררר}}' % masechet)
	content = content.replace('|גמרא על הפרק]]{{ש}}', '|גמרא על הפרק]]{{ש}}}}')
	content = content.replace(' | ', ' {{!}} ')
	content = content.replace(' |\n', ' {{!}}\n')
	content = content.replace('על ש"ס: [[{{{1}}}', '{{#שווה:{{שם דף הבסיס}}|בבלי %s פרק||על ש"ס: [[{{{1}}}' % masechet)
	content = content.replace('קטגוריה:אחרונים על ש"ס בבלי|אחרונים]]', 'קטגוריה:אחרונים על ש"ס בבלי|אחרונים]]}}')
	
	page.text = content
	page.save(summary='התאמה עבור פרקי הגמרא באמצעות בוט')
	print(page.title(), 'נערך')