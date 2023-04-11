import re
import pywikibot

site = pywikibot.Site()
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

BOOKS = {'בראשית': ['בראשית'], 'שמות': ['שמות'], 'ויקרא': ['ויקרא'], 'במדבר': ['במדבר'], 'דברים': ['דברים'], 'יהושע': ['יהושע'], 'שופטים': ['שופטים'], 'שמואל א': ['שמואל א', 'ש"א', "שמואל א'"], 'שמואל ב': ['שמואל ב', 'ש"ב', "שמואל ב'"], 'מלכים א': ['מלכים א', 'מ"א', "מלכים א'"], 'מלכים ב': ['מלכים ב', 'מ"ב', "מלכים ב'"],
'ישעיהו': ['ישעיהו', 'ישעיה'], 'ירמיהו': ['ירמיהו', 'ירמיה'], 'יחזקאל': ['יחזקאל'], 'הושע': ['הושע'], 'יואל': ['יואל'], 'עמוס': ['עמוס'], 'עובדיה': ['עובדיה'], 'יונה': ['יונה'], 'מיכה': ['מיכה'], 'נחום': ['נחום'], 'חבקוק': ['חבקוק'], 'צפניה': ['צפניה'], 'חגי': ['חגי'], 'זכריה': ['זכריה'], 'מלאכי': ['מלאכי'],
'תהלים': ['תהלים', 'תהילים'], 'משלי': ['משלי'], 'איוב': ['איוב'], 'שיר השירים': ['שיר השירים', 'שה"ש'], 'רות': ['רות'], 'אסתר': ['אסתר'], 'קהלת': ['קהלת', 'קוהלת'], 'איכה': ['איכה'], 'דניאל': ['דניאל'], 'עזרא': ['עזרא'], 'נחמיה': ['נחמיה'], 'דברי הימים א': ['דברי הימים א', 'דה"א', "דברי הימים א'"], 'דברי הימים ב': ['דברי הימים ב', 'דה"ב', "דברי הימים ב'"]}

def gershaim(letter):
	lst = letter.split(' ')
	if len(lst[-1]) > 1:
		lst[-1] = lst[-1][:-1] + '"' + lst[-1][-1]
	elif len(lst[-1]) == 1:
		lst[-1] += "'"
	else:
		print(f'can\'t add gershaim to "{letter}"')
	return ' '.join(lst)

def o_gershaim(letter):
	'''other gershaim marks.'''
	lst = letter.split(' ')
	if len(lst[-1]) > 1:
		lst[-1] = lst[-1][:-1] + '״' + lst[-1][-1]
	elif len(lst[-1]) == 1:
		lst[-1] += '׳'
	else:
		print(f'can\'t add o_gershaim to "{letter}"')
	return ' '.join(lst)
	
	
class Pasuk:
	def __init__(self, page):
		self.main_cat = page
		self.regex = re.match('^קטגוריה:(' + '|'.join(BOOKS.keys()) + ') '
		'(' + '|'.join(ALEPHBET[1:]) + ') (' + '|'.join(ALEPHBET[1:]) + ')$', self.main_cat.title())
		if not self.regex:
			raise Exception('can\'t parse title {} as regex.'.format(self.main_cat.title()))
		self.origin_book = self.regex.group(1)
		self.book = self.origin_book
		self.perek = self.regex.group(2)
		self.pasuk = self.regex.group(3)
		self.perek_num = str(ALEPHBET.index(self.perek))
		self.pasuk_num = str(ALEPHBET.index(self.pasuk))
		self.mg = 'מ"ג ' + self.book + ' ' + self.perek + ' ' + self.pasuk
		self.perek_title = self.book + ' ' + self.perek
		
		self.pasuk_formats = [self.format_simple, self.format_comma, self.format_semi_comma, self.format_gershaim, self.format_comma_gershaim, self.format_semi_comma_gershaim, self.format_o_gershaim, self.format_comma_o_gershaim, self.format_semi_comma_o_gershaim, self.format_colon, self.format_colon_gershaim, self.format_colon_o_gershaim, self.format_descrip, self.format_comma_descrip, self.format_semi_comma_descrip, self.format_gershaim_descrip, self.format_semi_comma_gershaim_descrip, self.format_o_gershaim_descrip, self.format_semi_comma_o_gershaim_descrip, self.format_num, self.format_comma_num, self.format_colon_num, self.format_nums, self.format_colon_nums, self.format_semi_comma_num, self.format_semi_comma_gershaim_num, self.format_semi_comma_o_gershaim_num, self.format_slash]
		self.mg_formats = [self.format_mg, self.format_mg_gershaim, self.format_mg_o_gershaim, self.format_mg_slash]
		self.perek_formats = [self.format_perek_comma, self.format_perek_gershaim, self.format_perek_comma_gershaim, self.format_perek_o_gershaim, self.format_perek_comma_o_gershaim, self.format_perek_descrip, self.format_perek_comma_descrip, self.format_perek_gershaim_descrip, self.format_perek_o_gershaim_descrip, self.format_perek_num, self.format_perek_slash]
	
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
	
	def format_o_gershaim(self):
		return self.book + ' ' + o_gershaim(self.perek) + ' ' + o_gershaim(self.pasuk)
	
	def format_comma_o_gershaim(self):
		return self.book + ', ' + o_gershaim(self.perek) + ', ' + o_gershaim(self.pasuk)
	
	def format_semi_comma_o_gershaim(self):
		return self.book + ' ' + o_gershaim(self.perek) + ', ' + o_gershaim(self.pasuk)
	
	def format_colon(self):
		return self.book + ' ' + self.perek + ':' + self.pasuk
	
	def format_colon_gershaim(self):
		return self.book + ' ' + gershaim(self.perek) + ':' + gershaim(self.pasuk)
	
	def format_colon_o_gershaim(self):
		return self.book + ' ' + o_gershaim(self.perek) + ':' + o_gershaim(self.pasuk)
	
	def format_descrip(self):
		return self.book + ' פרק ' + self.perek + ' פסוק ' + self.pasuk
	
	def format_comma_descrip(self):
		return self.book + ', פרק ' + self.perek + ', פסוק ' + self.pasuk
	
	def format_semi_comma_descrip(self):
		return self.book + ' פרק ' + self.perek + ', פסוק ' + self.pasuk
	
	def format_gershaim_descrip(self):
		return self.book + ' פרק ' + gershaim(self.perek) + ' פסוק ' + gershaim(self.pasuk)
	
	def format_semi_comma_gershaim_descrip(self):
		return self.book + ' פרק ' + gershaim(self.perek) + ', פסוק ' + gershaim(self.pasuk)
	
	def format_o_gershaim_descrip(self):
		return self.book + ' פרק ' + o_gershaim(self.perek) + ' פסוק ' + o_gershaim(self.pasuk)
	
	def format_semi_comma_o_gershaim_descrip(self):
		return self.book + ' פרק ' + o_gershaim(self.perek) + ', פסוק ' + o_gershaim(self.pasuk)
	
	def format_num(self):
		return self.book + ' ' + self.perek + ' ' + self.pasuk_num
	
	def format_comma_num(self):
		return self.book + ', ' + self.perek + ', ' + self.pasuk_num
	
	def format_semi_comma_num(self):
		return self.book + ' ' + self.perek + ', ' + self.pasuk_num
	
	def format_colon_num(self):
		return self.book + ' ' + self.perek + ':' + self.pasuk_num
	
	def format_nums(self):
		return self.book + ' ' + self.perek_num + ' ' + self.pasuk_num
	
	def format_colon_nums(self):
		return self.book + ' ' + self.perek_num + ':' + self.pasuk_num
	
	def format_semi_comma_gershaim_num(self):
		return self.book + ' ' + gershaim(self.perek) + ', ' + self.pasuk_num
	
	def format_semi_comma_o_gershaim_num(self):
		return self.book + ' ' + o_gershaim(self.perek) + ', ' + self.pasuk_num
	
	def format_slash(self):
		return 'מקרא/' + self.book + '/' + self.perek + '/' + self.pasuk
	
	def format_mg(self):
		return 'מקראות גדולות ' + self.book + ' ' + self.perek + ' ' + self.pasuk
	
	def format_mg_gershaim(self):
		return 'מקראות גדולות ' + self.book + ' ' + gershaim(self.perek) + ' ' + gershaim(self.pasuk)
	
	def format_mg_o_gershaim(self):
		return 'מקראות גדולות ' + self.book + ' ' + o_gershaim(self.perek) + ' ' + o_gershaim(self.pasuk)
	
	def format_mg_slash(self):
		return 'מקראות גדולות/' + self.book + '/' + self.perek + '/' + self.pasuk
	
	def format_perek_comma(self):
		return self.book + ', ' + self.perek
	
	def format_perek_gershaim(self):
		return self.book + ' ' + gershaim(self.perek)
	
	def format_perek_comma_gershaim(self):
		return self.book + ', ' + gershaim(self.perek)
	
	def format_perek_o_gershaim(self):
		return self.book + ' ' + o_gershaim(self.perek)
	
	def format_perek_comma_o_gershaim(self):
		return self.book + ', ' + o_gershaim(self.perek)
	
	def format_perek_descrip(self):
		return self.book + ' פרק ' + self.perek
	
	def format_perek_comma_descrip(self):
		return self.book + ', פרק ' + self.perek
	
	def format_perek_gershaim_descrip(self):
		return self.book + ' פרק ' + gershaim(self.perek)
		
	def format_perek_o_gershaim_descrip(self):
		return self.book + ' פרק ' + o_gershaim(self.perek)
	
	def format_perek_num(self):
		return self.book + ' ' + self.perek_num
	
	def format_perek_slash(self):
		return 'מקרא/'+ self.book + '/' + self.perek
	
	def text_redirect(self):
		return '#הפניה [[:' + self.main_cat.title() + ']]'
	
	def text_redirect_mg(self):
		return '#הפניה [[' + self.mg + ']]'
	
	def text_redirect_perek(self):
		return '#הפניה [[' + self.origin_book + ' ' + self.perek + ']]'
	
	def check_created(self):
		title = self.format_comma_descrip()
		format1 = pywikibot.Page(site, title)
		title = self.format_semi_comma_gershaim()
		format2 = pywikibot.Page(site, title)
		return format1.exists() and format2.exists()
	
	def create_redirects(self):
		pages = []
		for book_name in BOOKS[self.book]:
			self.book = book_name
			for format in self.pasuk_formats:
				title = format()
				page = pywikibot.Page(site, title)
				page.text = self.text_redirect()
				pages.append(page)
			for format in self.mg_formats:
				title = format()
				page = pywikibot.Page(site, title)
				page.text = self.text_redirect_mg()
				pages.append(page)
			for format in self.perek_formats:
				title = format()
				page = pywikibot.Page(site, title)
				page.text = self.text_redirect_perek()
				pages.append(page)
		return pages


def old_print_formats(pasuk):
	print('"'+pasuk.main_cat.title()+'" הפניות:')
	print(pasuk.format_simple())
	print(pasuk.format_comma())
	print(pasuk.format_semi_comma())
	print(pasuk.format_gershaim())
	print(pasuk.format_comma_gershaim())
	print(pasuk.format_semi_comma_gershaim())
	print(pasuk.format_o_gershaim())
	print(pasuk.format_comma_o_gershaim())
	print(pasuk.format_semi_comma_o_gershaim())
	print(pasuk.format_colon())
	print(pasuk.format_colon_gershaim())
	print(pasuk.format_colon_o_gershaim())
	print(pasuk.format_descrip())
	print(pasuk.format_comma_descrip())
	print(pasuk.format_semi_comma_descrip())
	print(pasuk.format_gershaim_descrip())
	print(pasuk.format_semi_comma_gershaim_descrip())
	print(pasuk.format_o_gershaim_descrip())
	print(pasuk.format_semi_comma_o_gershaim_descrip())
	print(pasuk.format_num())
	print(pasuk.format_comma_num())
	print(pasuk.format_colon_num())
	print(pasuk.format_nums())
	print(pasuk.format_colon_nums())
	print(pasuk.format_semi_comma_num())
	print(pasuk.format_semi_comma_gershaim_num())
	print(pasuk.format_semi_comma_o_gershaim_num())
	print(pasuk.format_slash())
	print()
	print('"'+pasuk.mg+'" הפניות:')
	print(pasuk.format_mg())
	print(pasuk.format_mg_gershaim())
	print(pasuk.format_mg_o_gershaim())
	print(pasuk.format_mg_slash())
	print()
	print('"'+pasuk.perek_title+'" הפניות:')
	print(pasuk.format_perek_comma())
	print(pasuk.format_perek_gershaim())
	print(pasuk.format_perek_comma_gershaim())
	print(pasuk.format_perek_o_gershaim())
	print(pasuk.format_perek_comma_o_gershaim())
	print(pasuk.format_perek_descrip())
	print(pasuk.format_perek_comma_descrip())
	print(pasuk.format_perek_gershaim_descrip())
	print(pasuk.format_perek_o_gershaim_descrip())
	print(pasuk.format_perek_num())
	print(pasuk.format_perek_slash())
	print()

def new_print_formats(pasuk):
	for book_name in BOOKS[pasuk.book]:
		pasuk.book = book_name
		print('"'+pasuk.main_cat.title()+'" הפניות:')
		for format in pasuk.pasuk_formats:
			print(format())
		print()
		print('"'+pasuk.mg+'" הפניות:')
		for format in pasuk.mg_formats:
			print(format())
		print()
		print('"'+pasuk.perek_title+'" הפניות:')
		for format in pasuk.perek_formats:
			print(format())

def test():
	page = pywikibot.Page(site, 'קטגוריה:שמות יח כג')
	pasuk = Pasuk(page)
	#old_print_formats(pasuk)
	new_print_formats(pasuk)
	
	page = pywikibot.Page(site, 'קטגוריה:דברי הימים א א א')
	pasuk = Pasuk(page)
	#old_print_formats(pasuk)
	new_print_formats(pasuk)
	
	page = pywikibot.Page(site, 'קטגוריה:תהלים קיט קעו')
	pasuk = Pasuk(page)
	#old_print_formats(pasuk)
	new_print_formats(pasuk)


class TheBot(pywikibot.bot.BaseBot):
	#generator = [pywikibot.Page(site, 'קטגוריה:שמות יח כג')]
	_temp = pywikibot.Page(site, 'תבנית:דף של פסוק')
	generator = _temp.getReferences(only_template_inclusion=True)
	
	def skip_page(self, page):
		if page.namespace != 14:
			return False
		return super().skip_page(page)
	
	def treat(self, page):
		pasuk = Pasuk(page)
		#if pasuk.check_created():
			#return
		redirs = pasuk.create_redirects()
		for redir in redirs:
			if redir.exists():
				if redir.isRedirectPage():
					print(redir, 'exists and redirect. skipping.')
					self.counter['skip'] += 1
					continue
				else:
					print(redir, 'exists and non-redirect. add category:להסב להפניות זמני')
					redir.text += '[[קטגוריה:להסב להפניות זמני]]'
					self.counter['add_cat'] += 1
			else:
				if not self.user_confirm('Do you want to create redirect {}?'.format(redir)):
					pywikibot.output('Skipping page {}'.format(redir))
					self.counter['skip'] += 1
					continue
				self.counter['create'] += 1
			redir.save(summary='[[ויקיטקסט:הפניות לדפי הפסוקים|הפניה חדשה למקרא]]')

def main():
	#test()
	TheBot().run()

main()