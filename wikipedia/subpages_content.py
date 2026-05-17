import pywikibot
from pywikibot.pagegenerators import PrefixingPageGenerator
import re

temp = 'תבנית:דגל'
head = '{{#בחר:{{{1}}}\n'
tail = '}}'

content = head
references = dict() # target: [refs,]

for page in PrefixingPageGenerator(prefix=temp + '/'):
    name = page.title().replace(temp + '/', '')
    
    if page.isRedirectPage():
        target = page.getRedirectTarget().title().replace(temp + '/', '')
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
        
    content += '|' + name + ' = ' + text + '\n'
    
content += tail

for tar, refs in references.items():
    content = content.replace('|' + tar + ' = ', '|' + '|'.join(refs) + '|' + tar + ' = ')

print(content)