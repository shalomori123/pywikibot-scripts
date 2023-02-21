"""This is the new version of "wiki bot text to cmd.txt" which was text file to copy and paste.
This file uses subprocesses to run the bot directly from python."""

from subprocess import run
from os import chdir

paws = False
pwb_dir = '/storage/emulated/0/python/pywikibot'
if paws:
	pwb_dir = '/srv/paws/pwb'

chdir(pwb_dir)

#useful params
call = ['python', 'pwb.py']
user = '-user:ShalomOrobot'
main_user = '-user:shalomori123'
site = '-site:wikisource:he'
pt = '-pt:0'
all_pages = '-start:!'
draft = '-page:משתמש:Shalomori123/טיוטה'


#init scripts
#run(call + ['login'])
#run(call + ['generate_user_files'])
#run(call + ['version'])
#run(call + ['replace', '-help'])


#frequent scripts
#run(call + ['keta tags bot'])
#run(call + ['empty draft'])
#run(call + ['redirect', 'double', '-ns:0', '-fullscan'])
#run(call + ['redirect', 'both'])
#run(call + ['test'])
#run(call + ['split bot'])
#run(call + [pt, 'wikidata sitelinks'])

#interesting scripts:
	#revertbot
	#listpages
	#category_redirect
	#movepages

#useful one-time temp
#run(call + ['keta 3.0', '-page:', '-regex:'])
#run(call + ['replace', '', '', '-prefixindex:', '-summary:'])
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=name|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}'
#'\n{{קטע עם כותרת|big page|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}'
#'\n[[קטגוריה:name|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]',
#'-links:name', '-titleregexnot:big page', '-create', '-up', '-summary:הכללה מהדף הכולל', pt])
#run(call + ['sources bot', '-prefixindex:'])
#run(call + ['touch', '-transcludes:temp'])
#run(call + ['rename bot', '-change:', '-to:', '-prefixindex:', '-summary:שינוי שם למהדורה'])
#run(call + ['create redirect bot', '-change:', '-to:', '-prefixindex:', '-summary:שינוי שם למהדורה'])
#run(call + ['delete', '-prefixindex:', main_user, '-summary:נוצר בטעות'])


# in work: (bots that i want to run but need more improve)
#run(call + ['replace', '<קטע (התחלה|סוף) ?= ?"([^>\s].*?)" />', '<קטע \\1=\\2/>', '<קטע (התחלה|סוף) ?= ?"([^>\s].*?)" ([^>\s].*?)="" />', '<קטע \\1=\\2 \\3/>', "'''<קטע התחלה ?= ?([^>\s].*?)/>", "<קטע התחלה=\\1/>'''", "<קטע סוף ?= ?([^>\s].*?)/>'''", "'''<קטע סוף=\\1/>", '-regex', '-summary:תיקון נזקי העורך החזותי לתגי קטע'])
#run(call + ['add_text', '-text:\n[[קטגוריה:הפניות מהמרחב הראשי למרחב ביאור]]', '-start:!', '-ns:0', '-grep:# ?הפניה \[\[ביאור:'])
#run(call + ['replace', '\{\{(מ"מ|ממ)\|([^\}].+)\|ק=\{\{שם הדף\}\}\}\}', '{{הפ|\\2}}', '-regex', '-start:!'])

#one-time scripts (newest first)
#run(call + [])
#run(call + [])
#run(call + [])
#run(call + [])
#run(call + [])
#run(call + ['rename bot', '-change:אלון בכות על איכה', '-to:אלון בכות (אייבשיץ) על איכה', '-prefixindex:אלון בכות על איכה', '-summary:שינוי שם למהדורה'])
#run(call + ['replace', '(ספרי הרמב"ם.*)', '\n==\\1==', '-regex', '-prefixindex:אגרות הרמב"ם/'])
#run(call + ['replace', "''", '"', '\n', '\n\n', '-prefixindex:אגרות הרמב"ם/'])
#run(call + ['keta 3.0', '-prefixindex:יריעות שלמה על רש"י/', '-titles'])
#run(call + ['create redirect bot', '-change:/', '-to: ', '-prefixindex:יריעות שלמה על רש"י/', '-summary:הפניה כדי שיכלל בדף מפרשי רש"י'])
#run(call + ['rename bot', '-change:יריעות שלמה על התורה/', '-to:יריעות שלמה על רש"י/', '-prefixindex:יריעות שלמה על התורה/', '-summary:שינוי שם למהדורה'])
#run(call + ['rename bot', '-change:שפ"ח על', '-to:שפתי חכמים על רש"י', '-prefixindex:שפ"ח', '-summary:שינוי שם למהדורה'])
#run(call + ['delete', '-prefixindex:שיטה מקובצת על הש"ס/בבא בתרא/פרק א/דף', main_user, '-summary:נוצר בטעות'])
#run(call + ['rename bot', '-change:שיחות לחג הפסח/', '-to:שיחות לחג הפסח (צמח מורי)/', '-prefixindex:שיחות לחג הפסח/', '-summary:שינוי שם למהדורה'])
#run(call + ['replace', '==פרק ([א-ת]{1,2})\.==\n(.*?)\n', '{{סרגל ניווט|קיצור ספר חרדים||פרק {{אות קודמת|\\1}}|פרק \\1|פרק {{אות הבאה|\\1}}}}\n==\\2==\n', '\n', '\n\n', '-regex', '-prefixindex:קיצור ספר חרדים/', '-summary:עריכה'])
#run(call + ['replace', '(\{\{הפ\|(במדבר|דברים)\|)יו', '\\1טז', '-regex', '-page:טיוטה:סמ"ק'])
#run(call + ['sources bot', '-page:טיוטה:סמ"ק'])
#run(call + ['replace', '(\n)הזנה אוטומטית (.+)', '\\1=\\2=', '-regex', '-page:טיוטה:סמ"ק'])
#run(call + ['add_text', '-text:[[קטגוריה:גור אריה על {{ס:החלף|{{ס:החלף|{{ס:שם הדף}}|גור אריה על רש&#34;י |}}| |{{ס:!}}}}]]', '-prefixindex:גור אריה על רש"י '])
#run(call + ['sources bot', '-prefixindex:יערות דבש/'])
#run(call + ['replace', ' )', '.)', '-prefixindex:יערות דבש/'])
#run(call + ['add_text', '-text:<noinclude>\n[[קטגוריה:עין איה|{{ס:החלף|{{ס:שם הדף}}|עין איה על |}}]]</noinclude>', '-prefixindex:עין איה על', '-summary:קטגוריה'])
#run(call + ['add_text', '-prefixindex:משיבת נפש/', '-text:[[קטגוריה:משיבת נפש|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]', '-summary:קטגוריה'])
#run(call + ['add_text', '-prefixindex:נתיבות המשפט/חידושים/', '-text:[[קטגוריה:נתיבות המשפט/חידושים|{{ס:#titleparts:{{ס:שם הדף}}|1|3}}]]', '-summary:קטגוריה'])
#for letter in ('א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
#'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
#'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
#'ל', 'לא', 'לב', 'לג', 'לד'):
#	run(call + ['add_text', '-text:{{מפרשי רש"י|{{ס:החלף|{{ס:החלף|{{ס:שם הדף}}|מפרשי רש&#34;י על |}}| |{{ס:!}}}}}}', '-links:גור אריה על רש"י דברים '+letter, '-titleregex:מפרשי רש"י', '-createonly', '-always'])
#run(call + ['replace', '=([^=\n].?)=\n', '{{ניווט ספר|שם הספר=גור אריה על רש"י|שם הספר2=דברים|\\1}}\n', '-regex', '-prefixindex:גור אריה על רש"י דברים', '-summary:ניווט'])
#run(call + ['keta 3.0', '-prefixindex:גור אריה על דברים/', '-regex:(=..?=\n)?==.*?\|פסוק (.+?)\]\]==', '-group:2'])
#run(call + ['replace', '==פרק (.{1,2}) פסוק (.{1,2})==\n\[א\]', '=\\1=\n\\0', '==פרק (.{1,2}) פסוק (.{1,2})==', '==[[מפרשי רש"י על דברים \\1 \\2|פסוק \\2]]==', '-regex', '-prefixindex:גור אריה על דברים/', '-summary:התאמה לחלוקה לדפי פרקים'])
#for letter in ('א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
#'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
#'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
#'ל', 'לא', 'לב', 'לג', 'לד', 'לה', 'לו'):
#	run(call + ['add_text', '-text:{{מפרשי רש"י|{{ס:החלף|{{ס:החלף|{{ס:שם הדף}}|מפרשי רש&#34;י על |}}| |{{ס:!}}}}}}', '-links:גור אריה על רש"י במדבר '+letter, '-titleregex:מפרשי רש"י', '-createonly', '-always'])
#run(call + ['replace', '=([^=\n].?)=\n', '{{ניווט ספר|שם הספר=גור אריה על רש"י|שם הספר2=במדבר|\\1}}\n', '-regex', '-prefixindex:גור אריה על רש"י במדבר', '-summary:ניווט'])
#run(call + ['keta 3.0', '-prefixindex:גור אריה על במדבר/', '-regex:(=..?=\n)?==.*?\|פסוק (.+?)\]\]==', '-group:2'])
#run(call + ['replace', '==פרק (.{1,2}) פסוק (.{1,2})==\n\[א\]', '=\\1=\n\\0', '==פרק (.{1,2}) פסוק (.{1,2})==', '==[[מפרשי רש"י על במדבר \\1 \\2|פסוק \\2]]==', '-regex', '-prefixindex:גור אריה על במדבר/', '-summary:התאמה לחלוקה לדפי פרקים'])
#for letter in ('א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
#'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
#'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז'):
#	run(call + ['add_text', '-text:{{מפרשי רש"י|{{ס:החלף|{{ס:החלף|{{ס:שם הדף}}|מפרשי רש&#34;י על |}}| |{{ס:!}}}}}}', '-links:גור אריה על רש"י ויקרא '+letter, '-titleregex:מפרשי רש"י', '-createonly', '-always'])
#run(call + ['replace', '=([^=\n].?)=\n', '{{ניווט ספר|שם הספר=גור אריה על רש"י|שם הספר2=ויקרא|\\1}}\n', '-regex', '-prefixindex:גור אריה על רש"י ויקרא', '-summary:ניווט'])
#run(call + ['keta 3.0', '-prefixindex:גור אריה על ויקרא/', '-regex:(=..?=\n)?==.*?\|פסוק (.+?)\]\]==', '-group:2'])
#run(call + ['replace', '==פרק (.{1,2}) פסוק (.{1,2})==\n\[א\]', '=\\1=\n\\0', '==פרק (.{1,2}) פסוק (.{1,2})==', '==[[מפרשי רש"י על ויקרא \\1 \\2|פסוק \\2]]==', '-regex', '-prefixindex:גור אריה על ויקרא/', '-summary:התאמה לחלוקה לדפי פרקים'])
#for letter in ('א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
#'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
#'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
#'ל', 'לא', 'לב', 'לג', 'לד', 'לה', 'לו', 'לח', 'לט', 'מ'):
#	run(call + ['add_text', '-text:{{מפרשי רש"י|{{ס:החלף|{{ס:החלף|{{ס:שם הדף}}|מפרשי רש&#34;י על |}}| |{{ס:!}}}}}}', '-links:גור אריה על רש"י שמות '+letter, '-titleregex:מפרשי רש"י', '-createonly', '-always'])
#run(call + ['replace', '=([^=\n].?)=\n', '{{ניווט ספר|שם הספר=גור אריה על רש"י|שם הספר2=שמות|\\1}}\n', '-regex', '-prefixindex:גור אריה על רש"י שמות', '-summary:ניווט'])
#run(call + ['keta 3.0', '-prefixindex:גור אריה על שמות/', '-regex:(=..?=\n)?==.*?\|פסוק (.+?)\]\]==', '-group:2'])
#run(call + ['replace', '==[[מפרשי רש"י על בראשית ', '==[[מפרשי רש"י על שמות ', '-prefixindex:גור אריה על שמות/'])
#run(call + ['replace', '==פרק (.{1,2}) פסוק (.{1,2})==\n\[א\]', '=\\1=\n\\0', '==פרק (.{1,2}) פסוק (.{1,2})==', '==[[מפרשי רש"י על בראשית \\1 \\2|פסוק \\2]]==', '-regex', '-prefixindex:גור אריה על שמות/', '-summary:התאמה לחלוקה לדפי פרקים'])
#for letter in ('א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
#'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
#'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
#'ל', 'לא', 'לב', 'לג', 'לד', 'לה', 'לו', 'לז', 'לח', 'לט',
#'מ', 'מא', 'מב', 'מג', 'מד', 'מה', 'מו', 'מז', 'מח', 'מט', 'נ'):
#	run(call + ['add_text', '-text:{{מפרשי רש"י|{{ס:החלף|{{ס:החלף|{{ס:שם הדף}}|מפרשי רש&#34;י על |}}| |{{ס:!}}}}}}', '-links:גור אריה על רש"י בראשית '+letter, '-titleregex:מפרשי רש"י', '-createonly', '-always'])
#run(call + ['replace', '=פרק (.?.?)=\n', '{{ניווט ספר|שם הספר=גור אריה על רש"י|שם הספר2=בראשית|\\1}}\n', '-regex', '-prefixindex:גור אריה על רש"י בראשית', '-summary:ניווט'])
#run(call + ['rename bot', '-change:גור אריה על בראשית/פרק ([א-נ][א-ט]?)', '-to:גור אריה על רש"י בראשית \g<1>', '-regex', '-prefixindex:גור אריה על בראשית/פרק', '-summary:שינוי שם למהדורה'])
#run(call + ['keta 3.0', '-prefixindex:גור אריה על בראשית/', '-regex:(=פרק .?.?=\n)?==.*?\|פסוק (.+?)\]\]==', '-group:2'])
#run(call + ['replace', '==פרק (.{1,2}) פסוק א==', '=פרק \\1=\n\\0', '==פרק (.{1,2}) פסוק (.{1,2})==', '==[[מפרשי רש"י על בראשית \\1 \\2|פסוק \\2]]==', '-regex', '-prefixindex:גור אריה על בראשית/', '-summary:התאמה לחלוקה לדפי פרקים'])
#run(call + ['replace', '#הפניה [[קטע:', '#הפניה [[', '-prefixindex:מצודות על', '-summary:תיקון הפניות למרחב קטע'])
#run(call + ['replace', '#הפניה [[קטע:', '#הפניה [[', '-prefixindex:רש"י על', '-summary:תיקון הפניות למרחב קטע'])
#run(call + ['replace', '\{\{פרשן על פרק\|רש&quot;י\|ישעיה\|.{0,3}\|(.{1,3})\|.{0,3}\}\}', '#הפניה [[רש"י על ישעיהו \\1]]', '-regex', '-prefixindex:רש"י על ישעיה'])
#run(call + ['replace', '\{\{פרשן על פרק\|רש&quot;י\|תהילים\|.{0,3}\|(.{1,3})\|.{0,3}\}\}', '#הפניה [[רש"י על תהלים \\1]]', '-regex', '-prefixindex:רש"י על תהילים'])
#run(call + ['replace', '<noinclude>[\s\S]*?#הפניה', '#הפניה', '-regex', '-prefixindex:תפארת ישראל על נידה', '-summary:החזרת הפניה'])
#run(call + ['replace', '\{\{גדול\|\[\[מדרש תנחומא (.*?) [ט-ל]?[א-ל]\|\'\'\'(.*?)\'\'\' ?\]\]\}\}', '{{פמ|מדרש תנחומא|\\1|\\2}}', '-regex', '-prefixindex:מדרש תנחומא', '-summary:התאמה לתבנית {{פמ}}'])
#run(call + ['replace', '(\[\[קט:משנה מסכת .*?) ([ט-ל]?[א-ל]\]\]</noinclude>)', '\\1|\\2', '-regex', '-prefixindex:מלאכת שלמה על', '-summary:קטגוריה'])
#run(call + ['add_text', '-text:<noinclude>\n[[קט:מלאכת שלמה על המשנה|{{ס:החלף|{{ס:שם הדף}}|מלאכת שלמה על |}}]]\n[[קט:משנה מסכת {{ס:החלף|{{ס:שם הדף}}|מלאכת שלמה על |}}]]</noinclude>', '-prefixindex:מלאכת שלמה על', '-summary:קטגוריה'])
#run(call + ['add_text', '-text:<noinclude>\n{{פירוש על פרק משנה|נידה|{{ס:החלף|{{ס:שם הדף}}|תפארת ישראל על נדה |}}}}\n[[קטגוריה:תפארת ישראל על המשנה|נידה]]</noinclude>', '-up', '-prefixindex:תפארת ישראל על נדה', '-summary:תיקון שיבוש בהפניה'])
#run(call + ['replace', '\<noinclude\>.+\</noinclude\>\n*', '', '-regex', '-prefixindex:תפארת ישראל על נידה', '-summary:תיקון שיבוש בהפניה'])
#run(call + ['replace', '==רש"י==', '==רש"י (ריב"ן)==', '|מפרש2=ר"ן', '|מפרש1=רש"י (ריב"ן)|מפרש2=ר"ן', '-titleregex:נדרים ([ט-צ][א-ט]?|[א-ט]) [אב]', '-links:בבלי נדרים', '-summary:החלפת "רש"י" ב"רש"י (ריב"ן)"'])
#run(call + ['replace', '-regex', '\|מרחב=:?קטע:?(\||\}\})', '\\1', '-start:!', '-summary:הסרת השאריות של מרחב קטע בתבניות'])
#run(call + ['replace', '<קטע (התחלה|סוף) ?= ?(ניקוד )?([ט-ל][א-ט]?|[א-ט])( ניקוד)? ?/>', '<קטע \\1=\\3/>', '-regex', '-prefixindex:משנה', '-titleregex:ניקוד$', '-summary:אחידות תגי קטע'])
#run(call + ['delete', '-prefixindex:חיפוש:', main_user, '-summary:מיותר לאחר שנוצרה {{חיפוש2}}'])
#run(call + ['redirect psukim'])
#run(call + ['rename bot', '-change:תשובות רשב"א', '-to:תשובות הרשב"א', '-prefixindex:תשובות רשב"א', '-summary:אחידות בשם "תשובות הרשב"א"'])
#run(call + ['sources bot', '-prefixindex:יערות דבש/דרוש'])
#run(call + ['replace', '\|', ')', '([^=] ?)\n\n', '\\1.\n\n', '-prefixindex:יערות דבש/דרוש', '-regex'])
#run(call + ['replace', '\n', '\n\n', '([א-ת])\| ', '\\1) ', ' \|([א-ת])', ' (\\1', '-prefixindex:יערות דבש/דרוש', '-regex'])
#run(call + ['add_text', '-text:[[קטגוריה:מקרא מבואר]]', '-prefixindex:מקרא מבואר/', '-grepnot:\[\[קטגוריה:מקרא מבואר', '-summary:קטגוריה'])
#run(call + ['replace', '[[קטגוריה:תרגום אבן תיבון למורה נבוכים]]', '[[קטגוריה:תרגום אבן תיבון למורה נבוכים|{{ס:החלף|{{ס:החלף|{{ס:שם הדף}}|מורה נבוכים (אבן תיבון)/חלק |}}|פרק |}}]]', '-prefixindex:מורה נבוכים (אבן תיבון)/', '-summary:אינדקס לקטגוריה'])
#run(call + ['add_text', '-text:[[קטגוריה:תרגום אבן תיבון למורה נבוכים|{{ס:החלף|{{ס:החלף|{{ס:שם הדף}}|מורה נבוכים (אבן תיבון)/חלק |}}|פרק |}}]]', '-prefixindex:מורה נבוכים (אבן תיבון)/', '-grepnot:\[\[קטגוריה:תרגום אבן תיבון למורה נבוכים', '-summary:קטגוריה'])
#run(call + ['add_text', '-prefixindex:ליקוטי תפילות', '-text:[[קטגוריה:ליקוטי תפילות]]', '-summary:קטגוריה'])
#run(call + ['add_text', '-prefixindex:לשון חכמים', '-text:[[קטגוריה:לשון חכמים]]', '-grepnot:[[קטגוריה:לשון חכמים]]', '-summary:קטגוריה'])
#run(call + ['add_text', '-prefixindex:הגהות רבי עקיבא איגר/', '-text:[[קטגוריה:הגהות רבי עקיבא איגר על {{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]', '-summary:קטגוריה'])
#run(call + ['add_text', '-prefixindex:ליקוטי הלכות/', '-text:[[קטגוריה:ליקוטי הלכות {{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]', '-summary:קטגוריה'])
#run(call + ['category', 'add', '-to:לקוטי מוהר"ן', '-links:ליקוטי מוהר"ן'])
#run(call + ['replace', '{{#קטע:תרגום אונקלוס/ספר', '{{#קטע:תרגום אונקלוס (תאג\')/ספר', '[[תרגום אונקלוס/ספר', '[[תרגום אונקלוס (תאג\')/ספר', '-prefixindex:תרגום אונקלוס (תאג\')/ספר', '-titleregex:/ספר [א-ת]+$'])
#run(call + ['replace', '{{#קטע:תרגום אונקלוס/ספר', '{{#קטע:תרגום אונקלוס (תאג\')/ספר', '-prefixindex:תרגום אונקלוס (תאג\')/ספר', '-titleregex:/פרשת'])
#run(call + ['replace', '{{הבהרה תאג\'}}', '{{הבהרה תאג\'|מקביל=ללא}}', '-transcludes:הבהרה תאג\'', '-titleregex:/פרשת'])
#run(call + ['add_text', '-up', '-text:{{הבהרה תאג\'}}', '-prefixindex:תרגום אונקלוס (תאג\')'])
#run(call + ['rename bot', '-change:תרגום אונקלוס/ספר', '-to:תרגום אונקלוס (תאג\')/ספר', '-prefixindex:תרגום אונקלוס/ספר', '-summary:שינוי שם למהדורה'])
#run(call + ['replace', '\{\{סרגל ניווט\|[\s\S]*משנה ..?==\n', '<noinclude>\\0</noinclude>\n', '-regex', '-prefixindex:דרך חיים (מהר"ל)/פרק', '-summary:noinclude'])
#run(call + ['replace', '\{\{מקראות גדולות על פסוק בנביאים אחרונים\|ישעיהו\|(.*?)\|(?:\\1 (.*?)|.*?)\|(.*?)\|(?:\\1 (.*?)|.*?)\}\}', '{{מקראות גדולות על פסוק|ישעיהו|\\1|\\2|\\3|\\4}}', '-regex', '-prefixindex:מ"ג ישעיהו', '-summary:הסבת תבנית {{מקראות גדולות על פסוק בנביאים אחרונים}} לתבנית הרגילה'])
#run(call + ['keta 3.0', '-regex:==סעיף (.*?)==', '-prefixindex:ביאור הגר"א על אורח', '-titleregex:ביאור הגר"א על אורח חיים [למנ][א-ט]?'])
#run(call + ['replace', '== ([א-ט]|[ט-נ][א-ט]?) ==', '==סעיף \\1==', '-regex', '-prefixindex:ביאור הגר"א על אורח', '-titleregex:ביאור הגר"א על אורח חיים [למנ][א-ט]?'])
#run(call + ['gra remove slash'])
#run(call + ['add_text', '-text:{{פרשן על שו"ע|ביאור הגר"א|אורח חיים|{{ס:#invoke:המרת מספרים ואותיות|num_to_he|{{ס:#חשב:{{ס:גימטריה|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}-1}}}}'
#'|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}|{{ס:#invoke:המרת מספרים ואותיות|num_to_he|{{ס:#חשב:{{ס:גימטריה|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}+1}}}}}}', '-up', '-prefixindex:ביאור הגר"א על אורח חיים/', '-summary:ניווט'])
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=חיים ביד|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}'
#'\n[[קטגוריה:חיים ביד|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]',
#'-prefixindex:חיים ביד/', '-up', '-summary:ניווט', pt])
#run(call + ['add_text', '-prefixindex:פרקי דרבי אליעזר פרק', '-text:==פירושים==\n===[[פר אחד/{{ס:החלף|{{ס:שם הדף}}|פרקי דרבי אליעזר פרק |}}|פר אחד]]===\n{{:פר אחד/{{ס:החלף|{{ס:שם הדף}}|פרקי דרבי אליעזר פרק |}}}}', '-summary:פירושים'])
#run(call + ['keta 3.0', '-links:אברבנאל על התורה', '-regex:=== ?פסוק (.*?) ?==='])
#run(call + ['add_text', '-text:{{פרשן על שו"ע|באר הגולה (רבקש)|חושן משפט|{{אות קודמת|{{ס:החלף|{{ס:שם הדף}}|באר הגולה (רבקש) על חושן משפט |}}}}|{{ס:החלף|{{ס:שם הדף}}|באר הגולה (רבקש) על חושן משפט |}}|{{אות הבאה|{{ס:החלף|{{ס:שם הדף}}|באר הגולה (רבקש) על חושן משפט |}}}}}}', '-up', '-prefixindex:באר הגולה (רבקש) על חושן משפט '])
#run(call + ['keta 3.0', '-prefixindex:ברכי יוסף על אורח חיים', '-regex:== \[\[שולחן ערוך אורח חיים .+?\| ?סעיף (.*?)\]\] =='])
#run(call + ['keta 3.0', '-page:אור החיים על דברים לב', '-regex:===פסוק (.*?)==='])
#run(call + ['replace', '\{\{מ"מ\|(תהילים|תהלים)\|.\}\}', '[[קט:זמני אור החיים|תהלים]]\\0', '-regex', '-prefixindex:אור החיים על', '-summary:תיקון הטעויות של בוט המקורות'])
#run(call + ['replace', '([\[\|\{\>\<]) \(', '\\1(', '\) ([\]\}\|\>\<])', ')\\1', '\| ?\{\{(מ"מ|הפניה)', '[[קט:זמני אור החיים|קישור]]\\0', '\}\} ?\]\]', '\\0[[קט:זמני אור החיים|קישור]]', '\{\{מ"מ\|(תהילים|תהלים)\|.\|', '[[קט:זמני אור החיים|תהלים]]\\0', '-regex', '-prefixindex:אור החיים על', '-summary:תיקון הטעויות של בוט המקורות'])
#run(call + ['sources bot', '-page:אור החיים על דברים כא יא'])
#run(call + ['replace', '<קטע התחלה=בהט ', '<קטע התחלה=', '<קטע סוף=בהט ', '<קטע סוף=', '-prefixindex:באר היטב על '])
#run(call + ['replace', '<קטע התחלה=בהל ', '<קטע התחלה=', '<קטע סוף=בהל ', '<קטע סוף=', '-prefixindex:ביאור הלכה על אורח חיים'])
#run(call + ['replace', '<קטע התחלה=מ"ב ', '<קטע התחלה=', '<קטע סוף=מ"ב ', '<קטע סוף=', '-prefixindex:משנה ברורה על אורח חיים'])
#run(call + ['replace', '==([א-י]) (.+?)==', '==פרק \\1/פסוק \\2==', '-regex', '-prefixindex:אור חדש/', '-titleregex:אור חדש/\d'])
#run(call + ['replace', '\n\n\n', '\n\n', '\n\n\n\n', '\n\n', '\n ', '\n', '-prefixindex:אור חדש/', '-titleregex:אור חדש/\d'])
#run(call + ['replace', '\n\n\n(.{0,200}\{\{מ"מ\|אסתר\|(.+?)\|(.+?)\|ק=\{\{שם הדף\}\}\}\})', '\n\n\n==\\2 \\3==\n\\1', '-regex', '-prefixindex:אור חדש/', '-titleregex:אור חדש/\d'])
#run(call + ['replace', '\.', '.\n\n\n', '==(ספר אור חדש עמוד .*?)==', '{{קטן|(\\1)}}', '-regex', '-prefixindex:אור חדש/', '-titleregex:אור חדש/\d'])
#run(call + ['add_text', '-text:[[קטגוריה:השתפכות הנפש|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]', '-prefixindex:השתפכות הנפש/', '-summary:קטגוריה'])
#run(call + ['touch', '-transcludes:פסוק בשורה', '-titleregex:/שורות'])
#run(call + ['add_text', '-text:[[קטגוריה:יפה תואר|{{ס:החלף|{{ס:#titleparts:{{ס:שם הדף}}|1|1}}|יפה תואר על |}} {{ס:#titleparts:{{ס:שם הדף}}|1|2}} {{ס:#titleparts:{{ס:שם הדף}}|1|3}}]]', '-prefixindex:יפה תואר על ', '-summary:קטגוריה'])
#run(call + ['replace', '[[קטגוריה:ספר תהלים]]', '', '[[קטגוריה:יוסף תהלות]]', '', '{{סרגל ניווט|יוסף תהלות|', '[[קט:תהלים {{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]\n{{סרגל ניווט|יוסף תהלות|קטגוריה=1|', '-prefixindex:יוסף תהלות/'])
#run(call + ['add_text', '-text:[[קטגוריה:ידי משה|{{ס:#titleparts:{{ס:שם הדף}}|1|2}} {{ס:#titleparts:{{ס:שם הדף}}|1|3}} {{ס:#titleparts:{{ס:שם הדף}}|1|4}}]]', '-prefixindex:ידי משה/', '-summary:קטגוריה'])
#run(call + ['category', 'add', '-to:חפץ חיים', '-prefixindex:חפץ חיים -'])
#run(call + ['taz oh temp'])
#run(call + ['sources bot', '-prefixindex:אור החיים על'])
#run(call + ['sources bot', draft])
#run(call + ['replace', '{{סרגל ניווט|חיי מוהר&quot;ן||', '{{סרגל ניווט|חיי מוהר"ן|קטגוריה=1||', '-prefixindex:חיי מוהר"ן '])
#run(call + ['replace', '{{סרגל ניווט|דעת תבונות||', '{{סרגל ניווט|דעת תבונות|קטגוריה=1||', '-prefixindex:דעת תבונות '])
#run(call + ['replace', '[[קטגוריה:חבל נחלתו]]', '', '-cat:חבל נחלתו'])
#run(call + ['add_text', '-prefixindex:אור החיים/פרשת', '-text:[[קטגוריה:אור החיים על המקרא|{{ס:#titleparts:{{ס:שם הדף}}|2|2}}]]', '-summary:קטגוריה'])
#run(call + ['add_text', '-prefixindex:חבל נחלתו ', '-text:[[קטגוריה:חבל נחלתו|{{ס:החלף|{{ס:שם הדף}}|חבל נחלתו |}}]]', '-grepnot:\[\[קטגוריה:חבל נחלתו\|', '-summary:קטגוריה'])
#run(call + ['keta 3.0', '-prefixindex:אלשיך על בראשית', '-regex:(?:\n|^)\{\{צ\|.+?\}\}.*? \(([א-ט]|[ט-צ][א-ט]?)(?: - ([א-ט]|[ט-צ][א-ט]?))?\):', '-titleregexnot:אלשיך על בראשית ..? ..?'])
#run(call + ['keta 3.0', '-prefixindex:בעל הטורים על התורה/', '-regex:(?:\n|^)\(([א-ט]|[ט-צ][א-ט]?)\)'])
#run(call + ['keta 3.0', '-prefixindex:ברטנורא על התורה/בראשית/', '-titles'])
#run(call + ['replace', '{{ברטנורא|', '{{ברטנורא על התורה|', '-prefixindex:ברטנורא על התורה/בראשית/'])
#run(call + ['add_text', '-text:[[קטגוריה:בעל הטורים על {{ס:#titleparts:{{ס:שם הדף}}|1|2}}|{{ס:#titleparts:{{ס:שם הדף}}|1|3}}]]', '-prefixindex:בעל הטורים על התורה/', '-summary:קטגוריה'])
#run(call + ['replace', '{{סרגל ניווט|בעל הטורים|', '{{סרגל ניווט|בעל הטורים על התורה|', '-prefixindex:בעל הטורים על התורה/'])
#run(call + ['temp mishna', pt])
#run(call + ['navigation maharal'])
#run(call + ['replace', "'''מתני'''' מני ", "מתני' מני ", "'''מתני'''' דלא", "מתני' דלא", '-summary:ביטול הדגשה מיותרת', '-links:משתמש:Ori229/כל דפי הבבלי'])
#run(call + ['replace', "<קטע התחלה=ג/>מתני' ", "<קטע התחלה=ג/>'''מתני'''' ", '-summary:הדגשת מתני', '-links:משתמש:Ori229/כל דפי הבבלי'])
#run(call + ['replace', "\nמתני' ", "\n'''מתני'''' ", '-summary:הדגשת מתני', '-links:משתמש:Ori229/כל דפי הבבלי'])
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=ספר יראים|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}'
#'\n{{קטע עם כותרת|ספר יראים/כל|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}'
#'\n[[קטגוריה:ספר יראים|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]',
#'-links:ספר יראים', '-titleregexnot:ספר יראים/כל', '-create', '-up', '-summary:הכללה מהדף הכולל', pt])
#run(call + ['create cat ben sira'])
#run(call + ['keta 3.0', '-page:ספר יראים/כל', '-titles'])
#run(call + ['replace', '-regex', '<קטע סוף=\{\{פסוק קודם\|\{\{המרת מספרים לאותיות\|(\d+)\}\}\}\}>\s*\
#<קטע התחלה=(\{\{המרת מספרים לאותיות\||)\\1\}?\}?>', 
#'=={{ס:#invoke:המרת מספרים ואותיות|num_to_he|\\1}}==', '-page:ספר יראים/כל', '-summary:כותרות'])
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=נצח ישראל|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}\
#\n{{קטע עם כותרת|נצח ישראל (מהר"ל)/כול הספר|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}',
#'-links:נצח ישראל', '-titleregex:נצח ישראל/', '-createonly'])
#run(call + ['keta 3.0', '-page:נצח ישראל (מהר"ל)/כול הספר', '-regex:==פרק (.*?)=='])
#run(call + ['keta 3.0', '-titles', '-page:אבן עזרא על שמות ט'])
#run(call + ['replace', '<קטע התחלה=/>', '', '<קטע סוף=/>', '', '-prefixindex:מלבי"ם'])
#run(call + ['replace', '{{ספר עץ חיים}}', '<noinclude>\n{{ספר עץ חיים}}\n</noinclude>', 
#'-prefixindex:עץ חיים/', pt, '-summary:תגי noinclude'])
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=משיבת נפש|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}\
#\n{{#קטע:משיבת נפש/הכל|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}', 
#'-links:משיבת נפש', '-titleregex:משיבת נפש/', '-createonly'])
#run(call + ['keta 2.0', '-page:משיבת נפש/הכל', '-regex:==(.*?)=='])
#run(call + ['keta 2.0', '-page:איסור והיתר לרבנו ירוחם/כל התוכן',
#'-regex:==סימן ([ט-פ]?"?[א-ט]?)\'?=='])
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=איסור והיתר לרבנו ירוחם|\
#{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}\n{{#קטע:איסור והיתר לרבנו ירוחם/כל התוכן\
#|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}', '-links:איסור והיתר לרבנו ירוחם', '-createonly'])
#run(call + ['keta 2.0', draft, '-regex:']) #test
#run(call + ['keta 3.0', draft, '-titles', '-remove_empty']) #test
#run(call + ['cotarot pnei yehoshua'])
#run(call + ['replace', 'אבן עזרה}}', 'אבן עזרא}}', '-prefixindex:ביאור:מ"ג'])
#run(call + ['replace', '[[קטע:', '[[', '-prefixindex:מצודות על ירמיה',
#pt, '-summary:תיקון הפניה שבורה'])
