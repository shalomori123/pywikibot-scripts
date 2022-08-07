import pywikibot
import re

site = pywikibot.Site()
prakim = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יט', 'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט', 'ל', 'לא', 'לב', 'לג', 'לד', 'לה', 'לו', 'לז', 'לח', 'לט', 'מ', 'מא']

for perek in prakim:
	page = pywikibot.Page(site, 'רד"ק על תהלים/'+ perek)
	page.text = page.text.replace('.', '.\n\n')
	
	while re.search('\(([א-ת\s]*)[׳״]([א-ת]?):([א-ת]+)[׳״]([א-ת]?)([\)-])', page.text):
		page.text = re.sub('\(([א-ת\s]*)[׳״]([א-ת]?):([א-ת]+)[׳״]([א-ת]?)([\)-])', r'([[\1\2 \3\4]]\5', page.text)
	
	while '\n ' in page.text:
		page.text = page.text.replace('\n ', '\n')
	while ' \n' in page.text:
		page.text = page.text.replace(' \n', '\n')
	
	if '<br>' in page.text:
		page.text = page.text.replace('<br>', '\n\n')
	if '<b>' in page.text:
		page.text = page.text.replace('<b>', "'''")
		page.text = page.text.replace('</b>', "'''")
	
	while ' )' in page.text:
		page.text = page.text.replace(' )', ')')
	while '( ' in page.text:
		page.text = page.text.replace('( ', '(')
	while re.search('[^\s\(]\(', page.text):
		page.text = re.sub('([^\s\(])\(', r'\1 (',page.text)
	while re.search('\)[^\s\)]', page.text):
		page.text = re.sub('\)([^\s\)])', r') \1', page.text)
	
	while '׃' in page.text:
		page.text = page.text.replace('׃', ':')
	while ' :' in page.text:
		page.text = page.text.replace(' :', ':')
	while '  ' in page.text:
		page.text = page.text.replace('  ', ' ')
	while ' .' in page.text:
		page.text = page.text.replace(' .', '.')
	while ' ,' in page.text:
		page.text = page.text.replace(' ,', ',')
		
	while '<sup>' in page.text and '<i' in page.text:
		page.text = page.text.replace('<sup>', ' {{הערה|')
		page.text = page.text.replace('</sup>', '')
		page.text = page.text.replace('<i class="footnote">', '\'\'\'הערת המדפיס:\'\'\' ')
		page.text = page.text.replace('</i>', '}}')
	
	page.save(summary='עריכה בטקסט')
	
	redirect = pywikibot.Page(site, 'רד"ק על תהלים '+ perek)
	redirect.text = '#הפניה [[%s]]'  % page.title()
	redirect.save(summary='הפניה חדשה')