import pywikibot

site = pywikibot.Site()
mainpage = pywikibot.Page(site, 'תוספות על הש"ס')
pages = mainpage.linkedPages()
for page in pages:
	content = page.text
	if '{{מפרשים למסכת' not in content:
		page_title = page.title()
		list_page = page_title.split('/')
		masechet = list_page[1]
		perek = list_page[2].split(' ')[1]
		print(page_title)
		
		page.text = '{{מפרשים למסכת %s|תוספות|%s}}\n\n' % (masechet, perek) + page.text
		page.save()
		print(page.title(), 'נערך')
	else:
		print(page.title(), 'היה בסדר')