import pywikibot

site = pywikibot.Site()
mainpage_tos = pywikibot.Page(site, 'תוספות על הש"ס')
tos_pages = mainpage_tos.linkedPages()
for page in tos_pages:
	a = page.get()
	b = a.replace('|תוספות', '|רש"י')
	c = b.replace('|ת}}', '|ר}}')
	rashi_title = page.title().replace('תוספות', 'רש"י')
	print(rashi_title)
	if 'בבא בתרא' not in page.title():
		rashi_page = pywikibot.page.Page(site, rashi_title)
		rashi_page.text = c
		rashi_page.save()
		print(page.title(), 'הועתק')