import pywikibot
from pywikibot.pagegenerators import PrefixingPageGenerator

site = pywikibot.Site()
for page in PrefixingPageGenerator('רש"י מנוקד על המקרא/ספר '):
	new_title = page.title().replace(' על המקרא/ספר ', ' על ', 1).replace('/', ' ')
	new_page = pywikibot.Page(site, new_title)
	new_page.text = '#הפניה [[%s]]'  % page.title()
	new_page.save('הפניה')
print('mission comleted!')