import re
import pywikibot
from pywikibot import pagegenerators
from sys import argv

gen_factory = pagegenerators.GeneratorFactory()
local_args = gen_factory.handle_args(argv)
gen = gen_factory.getCombinedGenerator(preload=True)

for page in gen:
	name = page.title().replace('/טעמים', '').split()
	if len(name) == 2:
		sefer, perek = name
	else:
		perek = name[-1]
		sefer = ' '.join(name[:-1])
	page.text = re.sub('\{\{(תבנית:)?טעמי המקרא באינטרנט( \(עליון\))?\}\}', '{{ניווט טעמים|%s|%s}}\n{{טעמי המקרא באינטרנט}}' % (sefer, perek), page.text)
	page.save('ניווט')
