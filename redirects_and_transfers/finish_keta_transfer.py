import pywikibot

site = pywikibot.Site()
basepage = pywikibot.Page(site, 'משתמש:Shalomori123/טיוטה')
for page in basepage.linkedPages(namespaces=100):
	new_title = page.title().replace('קטע:', '')
	pywikibot.output('Moving page {} to [[{}]]'.format(page, new_title))
	try:
		page.move(new_title, reason='העברה בעקבות ביטול מרחב קטע')
	except:
		print('\n\n\n\n', page.title(), 'faild\n\n')