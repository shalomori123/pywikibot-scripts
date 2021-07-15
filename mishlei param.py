import pywikibot
from pywikibot.pagegenerators import PrefixingPageGenerator

for page in PrefixingPageGenerator('קטגוריה:משלי '):
	if '|29|משלי}}' in page.text:
		page.text = page.text.replace('|29|משלי}}', '|28|משלי}}')
		page.save('תיקון פרמטר')
print('mission comleted!')
