import re
import pywikibot
from pywikibot.pagegenerators import PrefixingPageGenerator

site = pywikibot.Site()
for page in PrefixingPageGenerator('קטגוריה:תהלים '):
	if not re.match('קטגוריה:תהלים( ק?[ט-צ]?[א-י]?){2}', page.title()):
		continue
	new_title = page.title().replace('קטגוריה:תהלים', 'תהילים')
	new_page = pywikibot.Page(site, new_title)
	new_page.text = '#הפניה [[%s]]'  % page.title()
	new_page.save('new redirect')
print('mission comleted!')