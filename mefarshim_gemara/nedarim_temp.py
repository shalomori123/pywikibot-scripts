import pywikibot
from pywikibot.pagegenerators import PrefixingPageGenerator

site = pywikibot.Site()
for page in PrefixingPageGenerator('נדרים '):
	page.text = page.text.replace('{{כותרת לעמוד בגמרא נדרים|', '{{כותרת לעמוד בגמרא|מפרש2=ר"ן|מפרש3=תוספות|')
	page.save(summary='{{כותרת לעמוד בגמרא נדרים}} ← {{כותרת לעמוד בגמרא}}')
print('mission comleted!')