# File Docs Vault

## Overview
תת-עץ `vault/File Docs/` הוא מפת תיעוד קובץ-אחר-קובץ של כל קבצי הפרויקט: לכל קובץ מקור יש נוטת Markdown שמסבירה מה הוא עושה, למי הוא משויך (owner), וקישורי `[[wikilinks]]` לקבצים קשורים. הכספת מאורגנת לפי אזורים (Root Config, Agents, Custom/Bundled Skills, Content, Output, סביבות חן/יעל/יובל, Obsidian Config, Placeholders), כל אזור עם `_index.md` משלו, ומעליהם [[file-docs-vault|מפת-על]] (`File Docs/_index.md`). נכון ל-2026-06-10 מכוסים 85/85 קבצי המקור.

## Open Questions
- האם לתחזק את ה-File Docs ידנית בכל הוספת קובץ, או להפוך זאת לאוטומטי (hook/סקריפט)?
- קבצי `yael/style-guide.md` ו-tikיות ה-reference עדיין ריקים — הנוטות יתעדכנו כשימולאו.

## Session Log

### 2026-06-13 — אימות זרימת רחל מקצה-לקצה [verified]
- **What was done:** הותקנו `pandas 3.0.3` / `matplotlib 3.11.0` / `openpyxl 3.1.5` (Python 3.12.10). נוצר קובץ דוגמה `Planning_Data/2026-06-13-regional-sales.xlsx` (מכירות רבעוניות, 5 אזורים), והורץ הפייפליין של רחל: קריאה → חישוב Total+Growth → 2 גרפים PNG + xlsx מעובד + דוח MD ב-`Planning_Output/`.
- **Decisions:** הפייפליין הורץ **ישירות** (לא דרך spawn של הסוכנת) כי `rachel` עדיין לא רשומה כסוכנת בת-הפעלה בסשן — נדרש restart כדי שתופיע ב-Agent registry.
- **Notes / Caveats:** אומת ש-4/4 הקבצים נוצרו עם size>0 והמספרים נכונים (East=644K, צמיחת Central=63%, סך=₪2,256,000). אחרי restart מומלץ לחזור על המבחן דרך הפעלת הסוכנת עצמה כדי לאמת ניתוב + frontmatter.
- **Related:** [[agent-rachel]], [[rachel-workspace-index]]

### 2026-06-13 — הוספת רחל, אנליסטית הנתונים [shipped]
- **What was done:** נוצרה סוכנת חמישית **רחל** — אנליסטית נתונים. קובץ הגדרה `.claude/agents/rachel.md` (כלים: Read/Write/Edit/Bash/Glob/Skill, סקיל `xlsx`), שתי תיקיות עבודה `Planning_Data/` (קלט) ו-`Planning_Output/` (פלט: גרפים PNG + xlsx מעובד + דוח MD), כל אחת עם `.gitkeep`. עודכן [[file-CLAUDE]] (ראובן): פסקת צוות + ניתוב, סעיף "תהליך: ניתוח נתונים", ומבנה התיקיות. עודכן [[agent-ariel]] שרשאי למשוך גרפים/טבלאות מ-`Planning_Output/` למצגות. תועד בכספת: [[agent-rachel]], [[rachel-workspace-index]] + [[planning-data-gitkeep]]/[[planning-output-gitkeep]], ועודכנו [[agents-index]] ו-[[file-docs-vault]].
- **Decisions:** (1) המשתמש ביקש **בלי המרת שערי מטבעות** — רחל עובדת אך ורק עם המספרים שבקובץ. (2) שם תיקיית הפלט תוקן ל-`Planning_Output` (במקום `Planing_Output`). (3) תוצר משולש: PNG + xlsx + דוח MD, כדי שאריאל יוכל לשבץ גרפים ישירות במצגת. (4) רחל בלי גישה לרשת — מקבלת את הנתונים בקובץ.
- **Notes / Caveats:** דרישת תשתית — `pip install openpyxl pandas matplotlib`. ייתכן שצריך restart לסשן כדי שרחל תופיע ברשימת הסוכנים. ה-File Docs root index עדיין מתאר "שלושה סוכנים" בכמה מקומות (חוב טכני מלפני הוספת אריאל) — לא טופל כאן מעבר להוספת רחל.
- **Related:** [[agent-rachel]], [[rachel-workspace-index]], [[file-CLAUDE]], [[agent-ariel]]

### 2026-06-10 — בניית כספת File Docs [shipped]
- **What was done:** נוצרו 85 נוטות תיעוד (קובץ-לכל-קובץ) + 11 `_index.md` + נוטת convention ל-`.gitkeep`, תחת `vault/File Docs/`. כל נוטה כוללת frontmatter (`file`, `owner`, `type`, `tags`), תיאור "מה הקובץ עושה", שיוך owner, וקישורי `[[wikilinks]]` לקבצים קשורים.
- **Decisions:** (1) המשתמש בחר רזולוציית "קובץ-לכל-קובץ" כולל קבצי התמיכה של סקילי Superpowers — נוטות אלה נכתבו תמציתית כי הן קוד צד-שלישי. (2) קבצי `.gitkeep` הזהים תועדו כל אחד בנפרד אך מצביעים ל-[[convention-gitkeep]] משותף. (3) אינדקסי התיקיות נקראים `_index.md` (לפי הפרוטוקול) וקיבלו `aliases` כדי שקישורי `[[*-index]]` יתפענחו.
- **Notes / Caveats:** אומת ב-diff ש-85/85 קבצי המקור מכוסים ושאין wikilinks שבורים (הקישורים `[[Note]]`/`[[wikilinks]]` שנותרו הם דוגמאות בתוך code-spans). קובץ `Content/2026-06-10-israel-orthopedics-market.md` לא הופיע ברשימה הראשונית והתווסף בבדיקת הכיסוי.
- **Related:** [[file-docs-vault]], [[convention-gitkeep]]

### 2026-06-10 — התקנת סקילי obsidian [shipped]
- **What was done:** שלושה סקילים (`obsidian-bases`, `obsidian-markdown`, `obsidian-vault-workflow`) הורדו מ-`ZeremItay/the-5-agents-obsidian` ל-`.claude/skills/`. נוצרה תיקיית `vault/` (תוקן שם מ-`valut`).
- **Decisions:** הכספת אומצה כזיכרון ארוך-טווח של הפרויקט לפי פרוטוקול [[skill-obsidian-vault-workflow|obsidian-vault-workflow]].
- **Notes / Caveats:** התבקשה גם הפעלה אוטומטית של הסקיל בכל סשן/פקודה — מטופל דרך hooks ב-settings.json.
- **Related:** [[file-docs-vault]]
