import re
import pywikibot

path = '/sdcard/MyAppSharer/nedarim rashi.txt'
from os.path import isfile
while not isfile(path):
	print('wrong path')
	path = '/sdcard/MyAppSharer/' + input('enter file name: ')
masechet = 'נדרים'
parshan = ''

file = open(path, 'r')
lines = file.readlines()
file.close()
for index, line in enumerate(lines):
	print(index)
	while "''" in lines[index]:
		lines[index] = lines[index].replace("''", '"')
	
	while '\n ' in lines[index]:
		lines[index] = lines[index].replace('\n ', '\n')
	while ' \n' in lines[index]:
		lines[index] = lines[index].replace(' \n', '\n')
	while lines[index].startswith(' '):
		lines[index] = lines[index][1:]
	while lines[index].endswith(' '):
		lines[index] = lines[index][:-1]
	
	if '<br>' in lines[index]:
		lines[index] = lines[index].replace('<br>', '\n\n')
	while '<B>' in lines[index]:
		lines[index] = lines[index].replace('<B> ', "\n\n'''")
		lines[index] = lines[index].replace('<B>', "\n\n'''")
		lines[index] = lines[index].replace('</B>', "'''")
	
	if not re.fullmatch('\s*', lines[index]):
		lines[index] += '\n'
	if index < len(lines) - 2:
		while lines[index] == '\n' and lines[index + 1] == '\n':
			lines[index] = ''
	
	while ' )' in lines[index]:
		lines[index] = lines[index].replace(' )', ')')
	while '( ' in lines[index]:
		lines[index] = lines[index].replace('( ', '(')
	while re.search('[^\s\(]\(', lines[index]):
		lines[index] = re.sub('([^\s\(])\(', r'\1 (',lines[index])
	while re.search('\)[^\s\)]', lines[index]):
		lines[index] = re.sub('\)([^\s\)])', r') \1', lines[index])
	
	while '׃' in lines[index]:
		lines[index] = lines[index].replace('׃', ':')
	while ' :' in lines[index]:
		lines[index] = lines[index].replace(' :', ':')
	while '  ' in lines[index]:
		lines[index] = lines[index].replace('  ', ' ')
	while ' .' in lines[index]:
		lines[index] = lines[index].replace(' .', '.')
	while ' ,' in lines[index]:
		lines[index] = lines[index].replace(' ,', ',')


site = pywikibot.Site('he', 'wikisource')
content = ''.join(lines)
dafs = content.split('~ דף ')
for i,x in enumerate(dafs):
	dafs[i] = dafs[i].split('\n', 3)
	dafs[i][0] = dafs[i][0].replace(' - ', ' ')
	
	if len(dafs[i]) > 3 and dafs[i][0] not in ['יא א', 'ב א']:
		while dafs[i][3].endswith('\n'):
			dafs[i][3] = dafs[i][3][:-1]
		gmara_page = pywikibot.Page(site, 'נדרים %s' % dafs[i][0])
		gmara_page.get()
		gmara_page.text = gmara_page.text.replace('{{להשלים}}', dafs[i][3], 1)
		print(gmara_page.text)
		gmara_page.save('הוספת רש"י')
		
	
	

path = '/sdcard/MyAppSharer/nedarim tos.txt'
while not isfile(path):
	print('wrong path')
	path = '/sdcard/MyAppSharer/' + input('enter file name: ')
masechet = 'נדרים'
parshan = ''

file = open(path, 'r')
lines = file.readlines()
file.close()
for index, line in enumerate(lines):
	print(index)
	while "''" in lines[index]:
		lines[index] = lines[index].replace("''", '"')
	
	while '\n ' in lines[index]:
		lines[index] = lines[index].replace('\n ', '\n')
	while ' \n' in lines[index]:
		lines[index] = lines[index].replace(' \n', '\n')
	while lines[index].startswith(' '):
		lines[index] = lines[index][1:]
	while lines[index].endswith(' '):
		lines[index] = lines[index][:-1]
	
	if '<br>' in lines[index]:
		lines[index] = lines[index].replace('<br>', '\n\n')
	while '<B>' in lines[index]:
		lines[index] = lines[index].replace('<B> ', "\n\n'''")
		lines[index] = lines[index].replace('<B>', "\n\n'''")
		lines[index] = lines[index].replace('</B>', "'''")
	
	if not re.fullmatch('\s*', lines[index]):
		lines[index] += '\n'
	if index < len(lines) - 2:
		while lines[index] == '\n' and lines[index + 1] == '\n':
			lines[index] = ''
	
	while ' )' in lines[index]:
		lines[index] = lines[index].replace(' )', ')')
	while '( ' in lines[index]:
		lines[index] = lines[index].replace('( ', '(')
	while re.search('[^\s\(]\(', lines[index]):
		lines[index] = re.sub('([^\s\(])\(', r'\1 (',lines[index])
	while re.search('\)[^\s\)]', lines[index]):
		lines[index] = re.sub('\)([^\s\)])', r') \1', lines[index])
	
	while '׃' in lines[index]:
		lines[index] = lines[index].replace('׃', ':')
	while ' :' in lines[index]:
		lines[index] = lines[index].replace(' :', ':')
	while '  ' in lines[index]:
		lines[index] = lines[index].replace('  ', ' ')
	while ' .' in lines[index]:
		lines[index] = lines[index].replace(' .', '.')
	while ' ,' in lines[index]:
		lines[index] = lines[index].replace(' ,', ',')


site = pywikibot.Site('he', 'wikisource')
content = ''.join(lines)
dafs = content.split('~ דף ')
for i,x in enumerate(dafs):
	dafs[i] = dafs[i].split('\n', 3)
	dafs[i][0] = dafs[i][0].replace(' - ', ' ')
	
	if len(dafs[i]) > 3:
		while dafs[i][3].endswith('\n'):
			dafs[i][3] = dafs[i][3][:-1]
		gmara_page = pywikibot.Page(site, 'נדרים %s' % dafs[i][0])
		gmara_page.get()
		gmara_page.text = gmara_page.text.replace('{{להשלים}}', dafs[i][3], 1)
		print(gmara_page.text)
		gmara_page.save('הוספת תוספות')

#fixed_parshan = parshan
#if '"' in parshan:
#	fixed_parshan = parshan.replace('"', '')
#new_file = open('/sdcard/MyAppSharer/' + fixed_parshan + ' ' + masechet + '.txt', 'w+')
#new_file.writelines(lines)

#new_file.seek(0)
#content = new_file.readlines()
#for i, line in enumerate(content):
#	if i < len(content) - 2:
#		while content[i] == '\n' and content[i + 1] == '\n':
#			content[i] = ''
#new_file.seek(0)
#new_file.writelines(content)
#new_file.truncate(new_file.tell())
#new_file.close()
#print('completed')
