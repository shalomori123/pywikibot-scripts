import pywikibot
from pywikibot.pagegenerators import PrefixingPageGenerator
import re

temp = 'תבנית:דגל'
head = '{{#בחר:{{{1}}}\n'
tail = '}}'

content = head
references = dict() # target: [refs,]

sub_name = lambda p: p.title().replace(temp + '/', '')
format_key = lambda k: '|' + k + ' = '

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

print(content)