import pywikibot
from pywikibot.pagegenerators import PrefixingPageGenerator
import re

temp = 'תבנית:דגל'
head = '{{#בחר:{{{1}}}\n'
tail = '}}'
target_page_title = 'טיוטה:דגל/שם הקובץ'

sub_name = lambda p: p.title().replace(temp + '/', '')
format_key = lambda k: '|' + k + ' = '

content = head
references = dict() # target: [refs,]

for page in PrefixingPageGenerator(prefix=temp + '/'):
    name = sub_name(page)
    
    if page.isRedirectPage():
        target = sub_name(page.getRedirectTarget())
        if target in references:
            references[target].append(name)
        else:
            references[target] = [name]
        continue
        
    text = page.text
    text = re.sub('<noinclude>[\s\S]*?(</noinclude>)?', '', text).strip()
    
    if len(text) > 2000:
        print('skipping', name)
        continue
        
    content += format_key(name) + text + '\n'
    
content += tail

for tar, refs in references.items():
    content = content.replace(format_key(tar), '|' + '|'.join(refs) + format_key(tar))


site = pywikibot.Site()
target_page = pywikibot.Page(site, target_page_title)
target_page.text = content
target_page.save(summary="תוכן דפי משנה של [["+temp+"]]")

print(f"Successfully saved to {target_page_title}")