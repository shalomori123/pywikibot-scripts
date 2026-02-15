import re
import pywikibot
from pywikibot.pagegenerators import PrefixingPageGenerator

counter = 0
for page in PrefixingPageGenerator('רי"ף על הש"ס/'):
	if not page.text:
		page.text = '{{מחק|נוצר בטעות}}'
		page.save()
	if '{{דרוש שילוב}}' not in page.text:
		continue
	if page.text.endswith('{{דרוש שילוב}}') or \
	page.text.endswith('{{דרוש שילוב}}\n') or \
	page.text.endswith('{{דרוש שילוב}} \n'):
		page.text = page.text.replace('{{דרוש שילוב}}', '')
		page.save(summary='הסרת {{דרוש שילוב}}')
		continue
		
	realtext = re.sub('\<center\>[\S\s]*?\<\/center\>', '', page.text)
	realtext = re.sub('\{\{.*?\}\}', '', realtext)
	realtext = re.sub('\=\=.*?\=\=', '', realtext)
	realtext = re.sub('\[\[.*?\]\]', '', realtext)
	if re.search('[א-ת]', realtext):
		continue
		print(page, 'really need to fix...')
		counter += 1
	page.text = re.match('\{\{דף של רי"ף\|.*?\}\}', page.text).group(0)
	page.save(summary='הסרת תוכן ישן כפול')
print(counter, 'pages stay there')