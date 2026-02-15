import pywikibot

site = pywikibot.Site('he', 'wikisource')

for i in range(15, 74):
	page = pywikibot.Page(site, 'תבנית:שה/מחלקה חמישית/מדור ב/'+str(i))
	if page.exists() and not page.isRedirectPage():
		new = page.title().replace('תבנית:שה', 'שרי האלף')
		page.move(new, reason='')
		print(i)