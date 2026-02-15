import mwparserfromhell
import pywikibot
from pywikibot.pagegenerators import LinkedPageGenerator
from pywikibot.exceptions import NoPageError

src = pywikibot.Site('he', 'wikisource')
pedia = pywikibot.Site('he', 'wikipedia')
#gen = [pywikibot.Page(pedia, 'רבן יוחנן בן זכאי')]
tana = pywikibot.Page(pedia, 'תבנית:תנאים')
gen = LinkedPageGenerator(tana)

def set_key_of_param(data, temp, wanted_key, original_param):
	if temp.has(original_param, ignore_empty=True):
		data[wanted_key] = str(temp.get(original_param).value).strip()

def temp_to_data(temp):
	data = {}
	set_key_of_param(data, temp, 'לידה', 'תאריך לידה')
	set_key_of_param(data, temp, 'פטירה', 'תאריך פטירה')
	
	tkufa = ''
	if temp.has('התחלת פעילות', True):
		tkufa += str(temp.get('התחלת פעילות', '').value).strip() + ' - '
	if temp.has('סיום פעילות', True):
		tkufa += str(temp.get('סיום פעילות', '').value).strip()
	if tkufa:
		data['תקופה'] = tkufa
	
	set_key_of_param(data, temp, 'אביו', 'אב')
	set_key_of_param(data, temp, 'מקומו', 'מקום פעילות')
	if 'מקומו' in data:
		data['מקומו'] = data['מקומו'].replace('[[', '[[w:')
	set_key_of_param(data, temp, 'רבותיו', 'רבותיו')
	set_key_of_param(data, temp, 'תלמידיו', 'תלמידיו')
	set_key_of_param(data, temp, 'בניו', 'צאצאים')
	set_key_of_param(data, temp,'בני דורו', 'בני דורו')
	return data

def each_page(page):
	wikicode = mwparserfromhell.parse(page.text)
	temps = wikicode.filter_templates()
	for temp in temps:
		if temp.name.strip() == 'אישיות רבנית':
			data = temp_to_data(temp)
			break
	else:
		return
	
	src_name = ''
	try:
		item = pywikibot.ItemPage.fromPage(page)
		src_name = item.getSitelink(src.dbName()).title()
	except NoPageError:
		pass
	name = src_name.replace('קטגוריה:', '') or page.title()
	return name, data

data = {}
for page in gen:
	result = each_page(page)
	if result is None:
		continue
	name, table = result
	print(name, table)
	data[name] = table
print(data)