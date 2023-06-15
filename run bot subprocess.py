"""This file uses subprocesses to run the bot directly from python."""

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
visual_editor = ['<קטע (התחלה|סוף) ?= ?"([^>\s].*?)" ([^>\s].*?)="" />', '<קטע \\1=\\2 \\3/>', '<קטע (התחלה|סוף) ?= ?"([^>\s].*?)" />', '<קטע \\1=\\2/>',
"'''<קטע התחלה ?= ?([^>\s].*?)/>", "<קטע התחלה=\\1/>'''", "<קטע סוף ?= ?([^>\s].*?)/>'''", "'''<קטע סוף=\\1/>", '-regex', '-summary:תיקון נזקי העורך החזותי לתגי קטע']


#init scripts
#run(call + ['login'])
#run(call + ['generate_user_files'])
#run(call + ['version'])
#run(call + ['replace', '-help'])


#frequent scripts
#run(call + ['keta tags bot'])
#run(call + ['empty draft'])
#run(call + ['redirect', 'double', '-fullscan'])
#run(call + ['redirect', 'both'])
#run(call + ['test'])
#run(call + ['split bot'])
#run(call + [pt, 'wikidata sitelinks'])
#run(call + ['replace', *visual_editor, '-usercontribs:ראובן פרוס'])


#useful one-time temp
#run(call + ['keta 3.0', '-page:', '-regex:'])
#run(call + ['replace', '', '', '-regex', '-prefixindex:', '-summary:'])
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=name|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}'
#'\n{{קטע עם כותרת|big page|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}'
#'\n[[קטגוריה:name|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]',
#'-links:name', '-titleregexnot:big page', '-create', '-up', '-summary:הכללה מהדף הכולל', pt])
#run(call + ['sources bot', '-prefixindex:'])
#run(call + ['touch', '-transcludes:temp'])
#run(call + ['rename bot', '-change:', '-to:', '-prefixindex:', '-summary:שינוי שם למהדורה'])
#run(call + ['create redirect bot', '-change:', '-to:', '-prefixindex:', '-summary:שינוי שם למהדורה'])
#run(call + ['delete', '-prefixindex:', main_user, '-summary:נוצר בטעות'])
#run(call + ['revertbot', main_user, '-username:', '-limit:'])
#run(call + ['listpages', draft.replace('-page', '-put'), '-format:2', '-overwrite'])


#in build: (bots that i want to run but need more improve)
#run(call + ['add_text', '-text:\n[[קטגוריה:הפניות מהמרחב הראשי למרחב ביאור]]', '-start:!', '-ns:0', '-grep:# ?(הפניה|REDIRECT) \[\[ביאור:'])
#run(call + ['replace', '\{\{(מ"מ|ממ)\|([^\}].+)\|ק=\{\{שם הדף\}\}\}\}', '{{הפ|\\2}}', '-regex', '-transcludes:מ"מ'])

#one-time scripts (newest first)
#run(call + [])
#run(call + [])
#run(call + [])
#run(call + ['replace', '(^|\n)(<קטע התחלה=..?/>)?\(([ק-ת]?[ט-צ]?[א-ט]|[ק-ת]?[ט-צ])\) (.*?) -', '\\1\\2{{משע|מב|\\3|\\4}} -', '(^|\n)(<קטע התחלה=..?/>)?\(([ק-ת]?[ט-צ]?[א-ט]|[ק-ת]?[ט-צ])\)', '\\1\\2{{משע|מב|\\3|}}', '-regex', '-prefixindex:משנה ברורה על אורח חיים', '-summary:{{משע}}'])
#run(call + ['sources bot', '-prefixindex:ביאור:ירושלמי מאיר/'])
#books = ["בראשית", "שמות", "ויקרא", "במדבר", "דברים",
#"יהושע", "שופטים", "שמואל א", "שמואל ב", "מלכים א", "מלכים ב", 'יהושוע',
#"ישעיה", "ירמיה", "יחזקאל", "הושע", "יואל", "עמוס", "עובדיה", "יונה",
#"מיכה", "נחום", "חבקוק", "צפניה", "חגי", "זכריה", "מלאכי",
#"תהלים", "משלי", "איוב", "שיר השירים", "איכה", "קהלת", "אסתר", "רות", 'תהילים',
#"דניאל", "עזרא", "נחמיה", "דברי הימים א", "דברי הימים ב"]
#parashot = '(בראשית|נח|לך לך|וירא|חיי שרה|תולדות|ויצא|וישלח|וישב|מקץ|ויגש|ויחי|שמות|וארא|בא|בשלח|יתרו|משפטים|תרומה|תצוה|כי תשא|ויקהל|פקודי|ויקרא|צו|שמיני|תזריע|מצורע|אחרי מות|קדושים|אמור|בהר|בחוקותי|במדבר|נשא|בהעלותך|שלח|קורח|חוקת|חקת|בלק|פינחס|מטות|מסעי|דברים|ואתחנן|עקב|ראה|שופטים|כי תצא|כי תבוא|ניצבים|וילך|האזינו|וזאת הברכה)'
#run(call + ['replace', '<div style="height:100px;width:320px;border:1px solid #ccc;font:16px/26px Georgia, Garamond, Serif;overflow:auto;">([\s\S]*?)</div>', '{{תיבה נגללת|\g<1>}}', '\[(בראשית|שמות|ויקרא|במדבר|דברים) '+parashot+' ([ט-פ]?[א-ט]|[י-פ]) ([ט-פ]?[א-ט]|[י-פ])\]', '([[\\1 \\3 \\4|\\1 \\2 \\3 \\4]])', '(?<!\[)\[(' + '|'.join(books) + ')'+'(.*?)\]', '(\\1\\2)', '-regex', '-prefixindex:ביאור:ירושלמי מאיר/', '-summary:קישורים לפרשות, שינוי לסוגריים עגולים'])
#tanaim = ["שמעון הצדיק", "רבי דוסא בן הרכינס", "אנטיגנוס איש סוכו", "יוסי בן יועזר איש צרידה", "יוסי בן יוחנן איש ירושלים", "יהושע בן פרחיה", "נתאי הארבלי", "הלל", "שמאי", "רבן יוחנן בן זכאי", "רבן גמליאל", "רבן שמעון בן גמליאל", "רבן שמעון בן יוחאי", "ר' אליעזר בן הורקנוס", "ר' יהושע בן חנניה", "ר' יוסי הכהן", "ר' שמעון בן נתנאל", "ר' אלעזר בן ערך", "רבי ישמעאל בן אלישע", "רבי עקיבא", "יהודה בן בבא", "רבי טרפון", "אלישע בן אבויה", "רבי מאיר", "רבי יוסי בן חלפתא", "רבי נחמיה", "רבי יוסי הגלילי", "רבי נתן", "רבי יהודה הנשיא", "רבי שמעון בן אלעזר", "רבי יוסי בן יהודה", "רבי לעזר בן יהודה איש בירתותא", "רבי אלעזר בן יהודה איש בירתותא", "רבי חייא בן אבא", "רבי חייא הגדול", "רבי חייא רבא"]
#amoraim = ["רבי חנינא בר חמא", "רבי אושעיא", "רבי ינאי", "רבי יונתן", "רבי יהושע בן לוי", "רבי יוחנן", "חזקיה", "ריש לקיש", "רבי שמעון בן לקיש", "רבי יוסי בן חנינא", "רבי אלעזר בן פדת", "רבי אבהו", "רבי זירא", "רבי ירמיה", "רבי אחא", "רבי יונה", "רב דימי", "רבין", "רב אמי", "רבי אסי", "רבי אילא", "רבי אבא", "שמואל", "רבי יצחק בר חקולה"]
#replaces = []
#for tana in tanaim:
#	replaces.append(tana)
#	replaces.append('{{תנא|'+tana+'}}')
#for amora in amoraim:
#	replaces.append(amora)
#	replaces.append('{{אמורא|'+amora+'}}')
#run(call + ['replace', *replaces, '-prefixindex:ביאור:ירושלמי מאיר/', '-summary:תבניות תנא ואמורא'])
#run(call + ['replace', '\[https://www\.hebrewbooks\.org/pdfpager\.aspx\?req=.*?(\{\{ירושלמי מאיר/קישורים\|[\s\S]*?עמוד [אב]\])\]', '\\1', '-regex', '-prefixindex:ביאור:ירושלמי מאיר/', '-summary:תבנית קישורים'])
#run(call + ['replace', '\{\{ירושלמי מאיר/קישורים\|מסכת ', '{{ירושלמי מאיר/קישורים|', '-regex', '-prefixindex:ביאור:ירושלמי מאיר/', '-summary:תבנית קישורים'])
#run(call + ['replace', '\[דף ([ט-צ][א-ט]?|[א-ט]) עמוד ([אב])\]', '{{ירושלמי מאיר/קישורים|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}|\\1|\\2|קנייבסקי=|סירלאו=|פולדא=|תולדות יצחק=|שמחת תורה=|זהב הארץ=|אהלי שם=|פנים מאירות=}}\n\g<0>', '-regex', '-prefixindex:ביאור:ירושלמי מאיר/', '-summary:תבנית קישורים'])
#run(call + ['replace', "תלמוד ירושלמי \(וילנא\) מסכת ([א-ת\s]+?)\s*?(<br>)?\s*?\n(''')?פרק (..?) הלכה (.\S?)(''')?", '{{ירושלמי מאיר/הלכה|\\1|\\4|\\5}}',
#'(\{\{ירושלמי מאיר/הלכה\|[א-ת\|\s]+?)(\'|<)\}\}(br>|\'\')', '\\1}}', # '(?<!<br>)\nגמ’:', '\n\nגמ’:', '(?<!<br>)\n\[דף (..?) עמוד ב\]', '\n\n[דף \\1 עמוד ב]', "(?<!<br>)\n'''עין משפט", "\n\n'''עין משפט", 
#'-regex', '-prefixindex:ביאור:ירושלמי מאיר/', '-summary:ירידות שורה'])
#run(call + ['replace', ']] [[', ']] {{*}} [[', '-prefixindex:תבנית:פרקי ', '-summary:נקודות בין הפרקים'])
#run(call + ['replace', '</?div.*?>(?!\n)', '\g<0>\n', '-regex', '-prefixindex:בן סירא/בן זאב/', '-summary:עיצוב וקטגוריה'])
#run(call + ['replace', '</?div.*?>', '', '\A', '<div style="font-size:14pt;font-family: david;">', '\Z', '</div>\n[[קטגוריה:בן סירא]]', '\{\{סרגל ניווט\|.*?\}\}', '', '\n{3,6}', '\n\n', '-regex', '-prefixindex:בן סירא/בן זאב/', '-summary:עיצוב וקטגוריה'])
#run(call + ['ben sira perek'])
#run(call + ['nivut teamim', '-transcludes:טעמי המקרא באינטרנט', '-titleregex:/טעמים'])
#run(call + ['rename bot', '-change:משתמש:מושך בשבט/ירושלמי', '-to:ביאור:ירושלמי מאיר/מסכת', '-prefixindex:משתמש:מושך בשבט/ירושלמי', '-summary:העברת מרחב'])
#run(call + ['sources bot', '-prefixindex:כסף משנה/'])
#run(call + ['keta 3.0', '-prefixindex:תרגום ירושלמי (קטעים)/ספר דברים/', '-regex:(^|\n)([א-ט]|[ט-צ][א-ט]?) ', '-group:2'])
#run(call + ['replace', '\{\{פסוק בשורה\|([א-ת ]*?)\|([א-ת]*?)\|א\}\}', '<noinclude>{{כותרת עליונה לפרק תנך|\\1|\\2|שורות}}</noinclude>\n{{פסוק בשורה|\\1|\\2|א}}', '-transcludes:פסוק בשורה', '-titleregex:/שורות', '-regex'])
#run(call + ['replace', ' |', ' {{!}}', '[[מ"ג ', '[[:קטגוריה:', '-transcludes:דף של ספר תנ"ך', '-titleregex:(מגילת|ספר) (דניאל|משלי|איוב|דברי הימים|שיר השירים|רות|קהלת|אסתר)', '-summary:שינוי ממ"ג לפסוקים עצמם'])
#run(call + ['replace', '\{\{#invoke:Param.+?\}\}', '', '-regex', '-transcludes:דף של ספר תנ"ך', '-titleregex:ספר (הושע|יואל|עמוס|עובדיה|יונה|מיכה|נחום|חבקוק|צפניה|חגי|זכריה|מלאכי)', '-summary:שינוי ממ"ג לפסוקים עצמם'])
#run(call + ['replace', ' \|', ' {{!}}', '\[\[מ"ג ', '[[:קטגוריה:', '===פרק (..?)===', '===[[{{ס:החלף|{{ס:שם הדף}}|ספר |}} \\1|פרק \\1]]===', '-regex', '-transcludes:דף של ספר תנ"ך', '-titleregex:ספר (הושע|יואל|עמוס|עובדיה|יונה|מיכה|נחום|חבקוק|צפניה|חגי|זכריה|מלאכי)', '-summary:שינוי ממ"ג לפסוקים עצמם'])
#run(call + ['replace', '{{דף של ספר|', '{{דף של ספר תנ"ך|', '-transcludes:דף של ספר', '-summary:שינוי שם תבנית'])
#run(call + ['rename bot', '-change:ידי משה/', '-to:ידי משה על ', '-prefixindex:ידי משה/', '-summary:התאמה לשאר הפרשנים'])
#run(call + ['add_text', '-text:<noinclude>{{פרשן פיסקת מדרש|ידי משה|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}|{{ס:#titleparts:{{ס:שם הדף}}|1|3}}|{{ס:#titleparts:{{ס:שם הדף}}|1|4}}}}</noinclude>', '-prefixindex:ידי משה/', '-up', '-summary:ניווט', '-grepnot:{{פרשן פיסקת מדרש'])
#run(call + ['replace', '\{\{ניווט קטעים\|(יפה תואר|עץ יוסף|רש&#34;י) על (בראשית|שמות|ויקרא|במדבר|דברים) רבה/(..?.?)/(..?.?)\}\}', '{{פרשן פיסקת מדרש|\\1|\\2 רבה|\\3|\\4}}', '-regex', '-transcludes:ניווט קטעים', '-summary:שינוי תבנית ניווט לספציפית יותר'])
#run(call + ['halacha rambam bot'])
#run(call + ['replace', '(?<!\n)\n(?!\n)', '\n\n', '-regex', '-prefixindex:טיוטה:'])
#run(call + ['sources bot', '-prefixindex:טיוטה:'])
#run(call + ['replace', '(\n)הזנה אוטומטית (.+)', '\\1=\\2=', '-regex', '-prefixindex:טיוטה:'])
#run(call + ['add_text', '-text:==מפרשים==\n===הגהות רבינו פרץ===\n{{:הגהות רבינו פרץ על סמ"ק/{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}'
#'\n===הגהות חדשות===\n{{:הגהות חדשות על סמ"ק/{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}'
#'\n[[קטגוריה:סמ"ק|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}]]',
#'-prefixindex:סמ"ק/', '-summary:מפרשים'])
#run(call + ['replace', '^=(.*?)=\n', '{{ניווט ספר|שם הספר=סמ"ק|\\1}}\n', '-regex', '-prefixindex:סמ"ק/', '-summary:ניווט'])
#run(call + [main_user, 'delete link page'])
#run(call + ['replace', '(?<!small>)(?<!\{\{קטן\|)(\(...+?\))', '{{קטן|\\1}}', '-regex', '-prefixindex:אור החיים על', '-summary:הקטנת כל סוגריים, לבקשת משתמש:ראובן פרוס'])
#run(call + ['replace', *visual_editor, '-prefixindex:אור החיים'])
#run(call + ['replace', '\n<noinclude>[[קטגוריה: אלון בכות: א]]</noinclude>', '', '-cat:אלון בכות: א'])
#run(call + ['replace', '[[קטגוריה:להסב להפניות זמני]]', '', '-cat:להסב להפניות זמני'])
#run(call + ['add_text', '-text:{{הבהרה ספר המילים}}', '-cat:ספר המילים של שבי"ל', '-up', user])
#run(call + ['delete', '-prefixindex:ביאור הגר"א על אורח חיים/', main_user, '-summary:על פי דף [[שיחה:ביאור הגר"א על אורח חיים/יא|השיחה]]'])
#run(call + ['delete', '-prefixindex:גור אריה', '-titleregex:^גור אריה .*\d$', main_user, '-summary:מיותר, ערכו אולי כתיעוד'])
#run(call + ['replace', '<קטע (התחלה|סוף) ?= ?שו"ע ', '<קטע \\1=', '-prefixindex:שולחן ערוך', '-regex', '-summary:אחידות תגי קטע'])
#run(call + ['rename bot', '-change:^(.{3,12})(?!\(רחל\))$', '-to:\\1 (רחל)', '-regex', '-catr:קט:שירי רחל', '-summary:הוספת שם המשורר בשם הדף'])
#run(call + ['rename bot', '-change:^(.{3,12})(?!\(ביאליק\))$', '-to:\\1 (ביאליק)', '-regex', '-catr:קט:שירי חיים נחמן ביאליק', '-summary:הוספת שם המשורר בשם הדף'])
#run(call + ['rename bot', '-change:^(.{3,12})$', '-to:\\1 (אורי ניסן גנסין)', '-regex', '-cat:קט:אורי ניסן גנסין', '-summary:שינוי שם למהדורה'])
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



#old archive: (converted automaticly to subprocess format, oldest first)
#run("python pwb.py pagefromfile -lang:he -family:wikisource -user:shalomori123 -showdiff -notitle -appendbottom -autosummary -file:"/storage/emulated/0/MyAppSharer/.txt"")
#run("python pwb.py generate_user_files")
#run("python pwb.py login")
#run("python pwb.py 'keta tags bot'")
#run("python pwb.py 'empty draft'")
#run("python pwb.py redirect.py double")
#run("python pwb.py 'bot for rashi'")
#run("python pwb.py 'mefarshim temp'")
#run("python pwb.py 'bot for tavniot mefarshim'")
#run("python pwb.py 'nedarim bot'")
#run("python pwb.py 'cotarot shitmaq'")
#run("python pwb.py 'ein aia'")
#run("python pwb.py category add -links:'ר"ן על הרי"ף'")
#run("python pwb.py 'bot mefarshim to daf'")
#run("python pwb.py 'Caf Hahaim transform bot'")
#run("python pwb.py 'edit ran bot'")
#run("python pwb.py replace -ns:0 '[[en:Mishnah' '[[en:Translation:Mishnah' -prefixindex:משנה")
#run("python pwb.py replace '(שבי"ל)' '([[מחבר:שבי"ל|שבי"ל]])' -addcat:'ספר המילים של שבי"ל' -start:רגע2 -namespace:106")
#run("python pwb.py claimit -lang:he -family:wikipedia -links:'תבנית:תנאים' -ns:0 -exists:p P31 Q975574")
#Q55649849
#run("python pwb.py "hapeli'a transfer"")
#run("python pwb.py "sha'ar hagilgulim transfer bot"")
#run("python pwb.py 'nivut malbim'")
#run("python pwb.py add_text -text:'\n[[קטגוריה:דפי פרק במלבי"ם]]' -links:'משתמש:Shalomori123/קישורים לבוט' -always")
#run("python pwb.py 'mishlei param'")
#run("python pwb.py replace '|32|קהלת}}' '|33|קהלת}}' -prefixindex:'קטגוריה:קהלת'")
#run("python pwb.py replace '|28|איוב}}' '|29|איוב}}' -prefixindex:'קטגוריה:איוב'")
#run("python pwb.py replace '|31|שיר+השירים}}' '|30|שיר+השירים}}' -prefixindex:'קטגוריה:שיר השירים' -summary:'תיקון פרמטר'")
#run("python pwb.py replace '|30|רות}}' '|31|רות}}' -prefixindex:'קטגוריה:רות' -summary:'תיקון פרמטר'")
#run("python pwb.py replace '|33|איכה}}' '|32|איכה}}' -prefixindex:'קטגוריה:איכה' -summary:'תיקון פרמטר'")
#run("python pwb.py replace '#הפניה [[:קטגוריה:תהלים' '#הפניה [[תהלים' -titleregex:'תהילים ק?[ט-צ]?[א-ט]?' -prefixindex:תהילים")
#run("python pwb.py 'keta transform bot'")
#run("python pwb.py 'transform sarei'")
#run("python pwb.py replace -ns:0 '[[קטע:' '[[' '{{קטע:' '{{:'")
#run("python pwb.py replace -ns:0 -start:! '[[s:קטע:' '[[s:' '[[S:קטע:' '[[s:' '{{ויקיטקסט|קטע:' '{{ויקיטקסט|'")
#run("python pwb.py add_text -up -ns:0 -start:'רש"י על דברי הימים' -titleregex:'רש"י על (בראשית|שמות|ויקרא|במדבר|דברים|יהושע|שופטים|שמואל א|שמואל ב|מלכים א|מלכים ב|ישעיהו|ירמיהו|יחזקאל|תרי עשר|הושע|יואל|עמוס|עובדיה|יונה|מיכה|נחום|חבקוק|צפניה|חגי|זכריה|מלאכי|תהלים|משלי|איוב|שיר השירים|רות|אסתר|קהלת|איכה|דניאל|עזרא|נחמיה|דברי הימים א|דברי הימים ב) (ק?[ט-צ]?[א-ט]?) (ק?[ט-צ]?[א-ט]?)' -text:'<noinclude>{{ניווט לקטע ברש"י|{{ס:#invoke:String|reverse|{{ס:החלף|{{ס:#invoke:String|reverse|{{ס:החלף|{{ס:שם הדף}}|רש&#34;י על |}}}}| |{{ס:!}}|count=2}}}}}}</noinclude>' -grepnot:'\{\{(ניווט ל)?קטע ברש"י\|' -summary:'{{ניווט לקטע ברש"י}}' -site:wikisource:he -pt:0")
#run("python pwb.py replace -ref:'תבנית:דף רי"ף' "\{\{דף רי\"ף\|(דף |דף רי\"ף |)([ט-צ]?)\"?([א-ט]?)\'? ע?\"?([אב])\}\}" '{{דף רי"ף|\2\3|\4}}' -regex -site:wikisource:he -pt:0 -summary:'שינוי פורמט ל[[תבנית:דף רי"ף]]'")
#run("python pwb.py 'creat ben sira psukim'")
#run("python pwb.py 'creat rif dafs'")
#run("python pwb.py 'creat rif dafs' -pt:0")
#run("python pwb.py 'clear rif dafs'")
#run("python pwb.py 'edit radak psalms'")
#run("python pwb.py add_text -text:'{{ניווט ספר|שם הספר=שיחות הר"ן|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}\n{{#קטע:שיחות הר"ן/שלם|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}' -links:'שיחות הר"ן' -create -site:wikisource:he")
#run("python pwb.py replace '|מרחב=קטע:' '' -prefix:'מ"ג'")
#run("python pwb.py add_text -text:'{{ניווט ספר|שם הספר=השתפכות הנפש|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}\n{{#קטע:השתפכות הנפש/הכל|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}' -links:'משתמש:Shalomori123/קישורים לבוט' -create -site:wikisource:he")
