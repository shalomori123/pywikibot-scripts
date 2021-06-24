import pywikibot
from pywikibot.pagegenerators import PrefixingPageGenerator

site = pywikibot.Site()
for page in PrefixingPageGenerator('בעל הטורים על התורה/'):
	new_title = page.title().replace(' על התורה/', ' על ', 1).replace('/', ' ')
	new_page = pywikibot.Page(site, new_title)
	new_page.text = '#הפניה [[%s]]'  % page.title()
	new_page.save()
print('mission comleted!')