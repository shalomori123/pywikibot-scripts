import re
import pywikibot

ALEPHBET = ('', 'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
'ל', 'לא', 'לב', 'לג', 'לד', 'לה', 'לו', 'לז', 'לח', 'לט',
'מ', 'מא', 'מב', 'מג', 'מד', 'מה', 'מו', 'מז', 'מח', 'מט',
'נ', 'נא', 'נב', 'נג', 'נד', 'נה', 'נו', 'נז', 'נח', 'נט',
'ס', 'סא', 'סב', 'סג', 'סד', 'סה', 'סו', 'סז', 'סח', 'סט',
'ע', 'עא', 'עב', 'עג', 'עד', 'עה', 'עו', 'עז', 'עח', 'עט',
'פ', 'פא', 'פב', 'פג', 'פד', 'פה', 'פו', 'פז', 'פח', 'פט',
'צ', 'צא', 'צב', 'צג', 'צד', 'צה', 'צו', 'צז', 'צח', 'צט',
'ק', 'קא', 'קב', 'קג', 'קד', 'קה', 'קו', 'קז', 'קח', 'קט',
'קי', 'קיא', 'קיב', 'קיג', 'קיד', 'קטו', 'קטז', 'קיז', 'קיח', 'קיט',
'קכ', 'קכא', 'קכב', 'קכג', 'קכד', 'קכה', 'קכו', 'קכז', 'קכח', 'קכט',
'קל', 'קלא', 'קלב', 'קלג', 'קלד', 'קלה', 'קלו', 'קלז', 'קלח', 'קלט',
'קמ', 'קמא', 'קמב', 'קמג', 'קמד', 'קמה', 'קמו', 'קמז', 'קמח', 'קמט',
'קנ', 'קנא', 'קנב', 'קנג', 'קנד', 'קנה', 'קנו', 'קנז', 'קנח', 'קנט',
'קס', 'קסא', 'קסב', 'קסג', 'קסד', 'קסה', 'קסו', 'קסז', 'קסח', 'קסט',
'קע', 'קעא', 'קעב', 'קעג', 'קעד', 'קעה', 'קעו', 'קעז', 'קעח', 'קעט')

BOOKS = ['בראשית', 'שמות', 'ויקרא', 'במדבר', 'דברים', 'יהושע', 'שופטים', 'שמואל א', 'שמואל ב', 'מלכים א', 'מלכים ב',
'ישעיהו', 'ירמיהו', 'יחזקאל', 'הושע', 'יואל', 'עמוס', 'עובדיה', 'יונה', 'מיכה', 'נחום', 'חבקוק', 'צפניה', 'חגי', 'זכריה', 'מלאכי',
'תהלים', 'משלי', 'איוב', 'שיר השירים', 'רות', 'אסתר', 'קהלת', 'איכה', 'דניאל', 'עזרא', 'נחמיה', 'דברי הימים א', 'דברי הימים ב']

def gershaim(letter):
	lst = letter.split(' ')
	if len(lst[-1]) > 1:
		lst[-1] = lst[-1][:-1] + '"' + lst[-1][-1]
	elif len(lst[-1]) == 1:
		lst[-1] += "'"
	else:
		print(f'can\'t add gershaim to "{letter}"')
	return ' '.join(lst)
	
class Pasuk:
	def __init__(self, page):
		self.main_cat = page
		self.regex = re.match('קטגוריה:(' + '|'.join(BOOKS) + ')'
		' (ק?[ט-צ][א-ט]?|ק?[א-ט]) (ק?[ט-צ][א-ט]?|ק?[א-ט])', self.main_cat.title())
		self.book = self.regex.group(1)
		self.perek = self.regex.group(2)
		self.pasuk = self.regex.group(3)
		self.pasuk_num = str(ALEPHBET.index(self.pasuk))
		self.mg = 'מ"ג ' + self.book + ' ' + self.perek + ' ' + self.pasuk
		self.perek_title = self.book + ' ' + self.perek
	
	def format_simple(self):
		return self.book + ' ' + self.perek + ' ' + self.pasuk
	
	def format_comma(self):
		return self.book + ', ' + self.perek + ', ' + self.pasuk
	
	def format_semi_comma(self):
		return self.book + ' ' + self.perek + ', ' + self.pasuk
	
	def format_gershaim(self):
		return self.book + ' ' + gershaim(self.perek) + ' ' + gershaim(self.pasuk)
	
	def format_comma_gershaim(self):
		return self.book + ', ' + gershaim(self.perek) + ', ' + gershaim(self.pasuk)
	
	def format_semi_comma_gershaim(self):
		return self.book + ' ' + gershaim(self.perek) + ', ' + gershaim(self.pasuk)
	
	def format_descrip(self):
		return self.book + ' פרק ' + self.perek + ' פסוק ' + self.pasuk
	
	def format_comma_descrip(self):
		return self.book + ', פרק ' + self.perek + ', פסוק ' + self.pasuk
	
	def format_semi_comma_descrip(self):
		return self.book + ' פרק ' + self.perek + ', פסוק ' + self.pasuk
	
	def format_gershaim_descrip(self):
		return self.book + ' פרק ' + gershaim(self.perek) + ' פסוק ' + gershaim(self.pasuk)
	
	def format_num(self):
		return self.book + ' ' + self.perek + ' ' + self.pasuk_num
	
	def format_comma_num(self):
		return self.book + ', ' + self.perek + ', ' + self.pasuk_num
	
	def format_semi_comma_num(self):
		return self.book + ' ' + self.perek + ', ' + self.pasuk_num
	
	def format_semi_comma_gershaim_num(self):
		return self.book + ' ' + gershaim(self.perek) + ', ' + self.pasuk_num
	
	def format_mg(self):
		return 'מקראות גדולות ' + self.book + ' ' + self.perek + ' ' + self.pasuk
	
	def format_mg_gershaim(self):
		return 'מקראות גדולות ' + self.book + ' ' + gershaim(self.perek) + ' ' + gershaim(self.pasuk)
	
	def format_perek_comma(self):
		return self.book + ', ' + self.perek
	
	def format_perek_gershaim(self):
		return self.book + ' ' + gershaim(self.perek)
	
	def format_perek_comma_gershaim(self):
		return self.book + ', ' + gershaim(self.perek)
	
	def format_perek_descrip(self):
		return self.book + ' פרק ' + self.perek
	
	def format_perek_comma_descrip(self):
		return self.book + ', פרק ' + self.perek
	
	def format_perek_gershaim_descrip(self):
		return self.book + ' פרק ' + gershaim(self.perek)
	
	def text_redirect(self):
		return '#הפניה [[:' + self.main_cat.title() + ']]'
	
	def text_redirect_mg(self):
		return '#הפניה [[' + self.mg + ']]'


def print_formats(pasuk):
	print('"'+pasuk.main_cat.title()+'" הפניות:')
	print(pasuk.format_simple())
	print(pasuk.format_comma())
	print(pasuk.format_semi_comma())
	print(pasuk.format_gershaim())
	print(pasuk.format_comma_gershaim())
	print(pasuk.format_semi_comma_gershaim())
	print(pasuk.format_descrip())
	print(pasuk.format_comma_descrip())
	print(pasuk.format_semi_comma_descrip())
	print(pasuk.format_gershaim_descrip())
	print(pasuk.format_num())
	print(pasuk.format_comma_num())
	print(pasuk.format_semi_comma_num())
	print(pasuk.format_semi_comma_gershaim_num())
	print()
	print('"'+pasuk.mg+'" הפניות:')
	print(pasuk.format_mg())
	print(pasuk.format_mg_gershaim())
	print()
	print('"'+pasuk.perek_title+'" הפניות:')
	print(pasuk.format_perek_comma())
	print(pasuk.format_perek_gershaim())
	print(pasuk.format_perek_comma_gershaim())
	print(pasuk.format_perek_descrip())
	print(pasuk.format_perek_comma_descrip())
	print(pasuk.format_perek_gershaim_descrip())
	print()

def main():
	site = pywikibot.Site()
	page = pywikibot.Page(site, 'קטגוריה:שמות יח כג')
	pasuk = Pasuk(page)
	print_formats(pasuk)
	
	page = pywikibot.Page(site, 'קטגוריה:דברי הימים א א א')
	pasuk = Pasuk(page)
	print_formats(pasuk)
	
	page = pywikibot.Page(site, 'קטגוריה:תהלים קיט קעו')
	pasuk = Pasuk(page)
	print_formats(pasuk)

main()