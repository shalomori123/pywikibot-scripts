import pywikibot
from pywikibot.pagegenerators import PrefixingPageGenerator
import re

print('{{#בחר:{{{1}}}')

temp = 'תבנית:דגל'
for page in PrefixingPageGenerator(temp+'/'):
	#if page.isRedirectPage():
#		continue
	text = page.text
	text = re.sub('<noinclude>[\s\S]*?</noinclude>', '', text).strip()
	name = page.title().replace(temp+'/', '')
	if page.isRedirectPage():
		print('|' + name + '|' + page.getRedirectTarget().title())
	#if len(text) > 2000:
#		print('skipping', name)
#	else:
#		print('|' + name + ' = ' + text)
print('}}')