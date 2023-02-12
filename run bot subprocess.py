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
#run(call + ['redirect', 'double'])
#run(call + ['test'])
#run(call + ['split bot'])


#useful one-time temp
#run(call + ['keta 3.0', '-page:', '-regex:'])
#run(call + ['replace', '', '', '-prefixindex:'])
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=name|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}'
#'\n{{קטע עם כותרת|big page|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}'
#'\n[[קטגוריה:name|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]',
#'-links:name', '-titleregexnot:big page', '-create', '-up', '-summary:הכללה מהדף הכולל', pt])
#run(call + ['sources bot', '-prefixindex:'])
#run(call + ['touch', '-transcludes:temp'])


#one-time scripts
#run(call + ['replace', '[[קטע:', '[[', '-prefixindex:מצודות על ירמיה',
#pt, '-summary:תיקון הפניה שבורה'])
#run(call + ['replace', 'אבן עזרה}}', 'אבן עזרא}}', '-prefixindex:ביאור:מ"ג'])
#run(call + ['cotarot pnei yehoshua'])
#run(call + ['keta 3.0', draft, '-titles', '-remove_empty']) #test
#run(call + ['keta 2.0', draft, '-regex:']) #test
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=איסור והיתר לרבנו ירוחם|\
#{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}\n{{#קטע:איסור והיתר לרבנו ירוחם/כל התוכן\
#|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}', '-links:איסור והיתר לרבנו ירוחם', '-createonly'])
#run(call + ['keta 2.0', '-page:איסור והיתר לרבנו ירוחם/כל התוכן',
#'-regex:==סימן ([ט-פ]?"?[א-ט]?)\'?=='])
#run(call + ['keta 2.0', '-page:משיבת נפש/הכל', '-regex:==(.*?)=='])
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=משיבת נפש|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}\
#\n{{#קטע:משיבת נפש/הכל|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}', 
#'-links:משיבת נפש', '-titleregex:משיבת נפש/', '-createonly'])
#run(call + ['replace', '{{ספר עץ חיים}}', '<noinclude>\n{{ספר עץ חיים}}\n</noinclude>', 
#'-prefixindex:עץ חיים/', pt, '-summary:תגי noinclude'])
#run(call + ['replace', '<קטע התחלה=/>', '', '<קטע סוף=/>', '', '-prefixindex:מלבי"ם'])
#run(call + ['keta 3.0', '-titles', '-page:אבן עזרא על שמות ט'])
#run(call + ['keta 3.0', '-page:נצח ישראל (מהר"ל)/כול הספר', '-regex:==פרק (.*?)=='])
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=נצח ישראל|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}\
#\n{{קטע עם כותרת|נצח ישראל (מהר"ל)/כול הספר|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}',
#'-links:נצח ישראל', '-titleregex:נצח ישראל/', '-createonly'])
#run(call + ['replace', '-regex', '<קטע סוף=\{\{פסוק קודם\|\{\{המרת מספרים לאותיות\|(\d+)\}\}\}\}>\s*\
#<קטע התחלה=(\{\{המרת מספרים לאותיות\||)\\1\}?\}?>', 
#'=={{ס:#invoke:המרת מספרים ואותיות|num_to_he|\\1}}==', '-page:ספר יראים/כל', '-summary:כותרות'])
#run(call + ['keta 3.0', '-page:ספר יראים/כל', '-titles'])
#run(call + ['create cat ben sira'])
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=ספר יראים|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}'
#'\n{{קטע עם כותרת|ספר יראים/כל|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}'
#'\n[[קטגוריה:ספר יראים|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]',
#'-links:ספר יראים', '-titleregexnot:ספר יראים/כל', '-create', '-up', '-summary:הכללה מהדף הכולל', pt])
#run(call + ['replace', "\nמתני' ", "\n'''מתני'''' ", '-summary:הדגשת מתני', '-links:משתמש:Ori229/כל דפי הבבלי'])
#run(call + ['replace', "<קטע התחלה=ג/>מתני' ", "<קטע התחלה=ג/>'''מתני'''' ", '-summary:הדגשת מתני', '-links:משתמש:Ori229/כל דפי הבבלי'])
#run(call + ['replace', "'''מתני'''' מני ", "מתני' מני ", "'''מתני'''' דלא", "מתני' דלא", '-summary:ביטול הדגשה מיותרת', '-links:משתמש:Ori229/כל דפי הבבלי'])
#run(call + ['navigation maharal'])
#run(call + ['temp mishna', pt])
#run(call + ['replace', '{{סרגל ניווט|בעל הטורים|', '{{סרגל ניווט|בעל הטורים על התורה|', '-prefixindex:בעל הטורים על התורה/'])
#run(call + ['add_text', '-text:[[קטגוריה:בעל הטורים על {{ס:#titleparts:{{ס:שם הדף}}|1|2}}|{{ס:#titleparts:{{ס:שם הדף}}|1|3}}]]', '-prefixindex:בעל הטורים על התורה/', '-summary:קטגוריה'])
#run(call + ['replace', '{{ברטנורא|', '{{ברטנורא על התורה|', '-prefixindex:ברטנורא על התורה/בראשית/'])
#run(call + ['keta 3.0', '-prefixindex:ברטנורא על התורה/בראשית/', '-titles'])
#run(call + ['keta 3.0', '-prefixindex:בעל הטורים על התורה/', '-regex:(?:\n|^)\(([א-ט]|[ט-צ][א-ט]?)\)'])
#run(call + ['keta 3.0', '-prefixindex:אלשיך על בראשית', '-regex:(?:\n|^)\{\{צ\|.+?\}\}.*? \(([א-ט]|[ט-צ][א-ט]?)(?: - ([א-ט]|[ט-צ][א-ט]?))?\):', '-titleregexnot:אלשיך על בראשית ..? ..?'])
#run(call + ['add_text', '-prefixindex:חבל נחלתו ', '-text:[[קטגוריה:חבל נחלתו|{{ס:החלף|{{ס:שם הדף}}|חבל נחלתו |}}]]', '-grepnot:\[\[קטגוריה:חבל נחלתו\|', '-summary:קטגוריה'])
#run(call + ['add_text', '-prefixindex:אור החיים/פרשת', '-text:[[קטגוריה:אור החיים על המקרא|{{ס:#titleparts:{{ס:שם הדף}}|2|2}}]]', '-summary:קטגוריה'])
#run(call + ['replace', '[[קטגוריה:חבל נחלתו]]', '', '-cat:חבל נחלתו'])
#run(call + ['replace', '{{סרגל ניווט|דעת תבונות||', '{{סרגל ניווט|דעת תבונות|קטגוריה=1||', '-prefixindex:דעת תבונות '])
#run(call + ['replace', '{{סרגל ניווט|חיי מוהר&quot;ן||', '{{סרגל ניווט|חיי מוהר"ן|קטגוריה=1||', '-prefixindex:חיי מוהר"ן '])
#run(call + ['sources bot', draft])
#run(call + ['sources bot', '-prefixindex:אור החיים על'])
#run(call + ['taz oh temp'])
#run(call + ['category', 'add', 'חפץ חיים', '-prefixindex:חפץ חיים -'])
#run(call + ['add_text', '-text:[[קטגוריה:ידי משה|{{ס:#titleparts:{{ס:שם הדף}}|1|2}} {{ס:#titleparts:{{ס:שם הדף}}|1|3}} {{ס:#titleparts:{{ס:שם הדף}}|1|4}}]]', '-prefixindex:ידי משה/', '-summary:קטגוריה'])
#run(call + ['replace', '[[קטגוריה:ספר תהלים]]', '', '[[קטגוריה:יוסף תהלות]]', '', '{{סרגל ניווט|יוסף תהלות|', '[[קט:תהלים {{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]\n{{סרגל ניווט|יוסף תהלות|קטגוריה=1|', '-prefixindex:יוסף תהלות/'])
#run(call + ['add_text', '-text:[[קטגוריה:יפה תואר|{{ס:החלף|{{ס:#titleparts:{{ס:שם הדף}}|1|1}}|יפה תואר על |}} {{ס:#titleparts:{{ס:שם הדף}}|1|2}} {{ס:#titleparts:{{ס:שם הדף}}|1|3}}]]', '-prefixindex:יפה תואר על ', '-summary:קטגוריה'])
#run(call + ['touch', '-transcludes:פסוק בשורה', '-titleregex:/שורות'])
#run(call + ['add_text', '-text:[[קטגוריה:השתפכות הנפש|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]', '-prefixindex:השתפכות הנפש/', '-summary:קטגוריה'])
#run(call + ['replace', '\.', '.\n\n\n', '==(ספר אור חדש עמוד .*?)==', '{{קטן|(\\1)}}', '-regex', '-prefixindex:אור חדש/', '-titleregex:אור חדש/\d'])
#run(call + ['replace', '\n\n\n(.{0,200}\{\{מ"מ\|אסתר\|(.+?)\|(.+?)\|ק=\{\{שם הדף\}\}\}\})', '\n\n\n==\\2 \\3==\n\\1', '-regex', '-prefixindex:אור חדש/', '-titleregex:אור חדש/\d'])
#run(call + ['replace', '\n\n\n', '\n\n', '\n\n\n\n', '\n\n', '\n ', '\n', '-prefixindex:אור חדש/', '-titleregex:אור חדש/\d'])
#run(call + ['replace', '==([א-י]) (.+?)==', '==פרק \\1/פסוק \\2==', '-regex', '-prefixindex:אור חדש/', '-titleregex:אור חדש/\d'])
#run(call + ['replace', '<קטע התחלה=מ"ב ', '<קטע התחלה=', '<קטע סוף=מ"ב ', '<קטע סוף=', '-prefixindex:משנה ברורה על אורח חיים'])
#run(call + ['replace', '<קטע התחלה=בהל ', '<קטע התחלה=', '<קטע סוף=בהל ', '<קטע סוף=', '-prefixindex:ביאור הלכה על אורח חיים'])
#run(call + ['replace', '<קטע התחלה=בהט ', '<קטע התחלה=', '<קטע סוף=בהט ', '<קטע סוף=', '-prefixindex:באר היטב על '])
#run(call + ['sources bot', '-page:אור החיים על דברים כא יא'])
#run(call + ['replace', '([\[\|\{\>\<]) \(', '\\1(', '\) ([\]\}\|\>\<])', ')\\1', '\| ?\{\{(מ"מ|הפניה)', '[[קט:זמני אור החיים|קישור]]\\0', '\}\} ?\]\]', '\\0[[קט:זמני אור החיים|קישור]]', '\{\{מ"מ\|(תהילים|תהלים)\|.\|', '[[קט:זמני אור החיים|תהלים]]\\0', '-regex', '-prefixindex:אור החיים על', '-summary:תיקון הטעויות של בוט המקורות'])
#run(call + ['replace', '\{\{מ"מ\|(תהילים|תהלים)\|.\}\}', '[[קט:זמני אור החיים|תהלים]]\\0', '-regex', '-prefixindex:אור החיים על', '-summary:תיקון הטעויות של בוט המקורות'])
#run(call + ['keta 3.0', '-page:אור החיים על דברים לב', '-regex:===פסוק (.*?)==='])
#run(call + ['keta 3.0', '-prefixindex:ברכי יוסף על אורח חיים', '-regex:== \[\[שולחן ערוך אורח חיים .+?\| ?סעיף (.*?)\]\] =='])
#run(call + ['add_text', '-text:{{פרשן על שו"ע|באר הגולה (רבקש)|חושן משפט|{{אות קודמת|{{ס:החלף|{{ס:שם הדף}}|באר הגולה (רבקש) על חושן משפט |}}}}|{{ס:החלף|{{ס:שם הדף}}|באר הגולה (רבקש) על חושן משפט |}}|{{אות הבאה|{{ס:החלף|{{ס:שם הדף}}|באר הגולה (רבקש) על חושן משפט |}}}}}}', '-up', '-prefixindex:באר הגולה (רבקש) על חושן משפט '])
#run(call + [])
#run(call + [])
#run(call + [])
#run(call + [])
#run(call + [])
#run(call + [])
#run(call + [])
#run(call + [])
#run(call + [])
#run(call + ['redirect psukim'])
