---
file: .claude/agents/yael.md
owner: יעל
type: agent-config
tags:
  - file-docs
  - agent
  - content
---

# yael.md — יעל, כותבת התוכן

**נתיב:** `.claude/agents/yael.md`
**שייך ל:** יעל

## מה הקובץ עושה
הגדרת הסוכנת **יעל** — כותבת התוכן. לוקחת מאמר גלם מ-`Content/`, משכתבת בסגנון הבית, ושומרת שני תוצרים ב-`Output/` (Markdown + HTML מעוצב עם `dir="rtl"`).
- **כלים:** Read, Write, Edit, Glob, Grep בלבד (לא מחפשת ברשת, לא יוצרת תמונות).
- **סגנון בית:** קוראת את [[yael-style-guide]] ואת `yael/reference/` בתחילת סשן.
- **תמונות:** מסמנת צורך בתמונה עם placeholder `{{IMAGE_NEEDED: "..."}}` שראובן מעביר ליובל.
- **כללי ברזל:** אסור להוסיף קישורים/CTAs/הפניות למחבר המקורי; מסירה כאלה אם קיימים; מותגים בתוך הסיפור נשארים.
- **מילות הפעלה:** שכתב, ערוך, נסח מחדש, תרגם, סכם / rewrite, edit, summarize, translate.

## קבצים קשורים
- [[file-CLAUDE]] — ראובן, שמפעיל את יעל
- [[yael-style-guide]] — מדריך סגנון הבית שיעל קוראת
- [[yael-reference-gitkeep]] — תיקיית דוגמאות הסגנון
- [[content-index]] — מקור הגלם
- [[output-index]] — היכן יעל שומרת תוצרים
- [[agent-yuval]] — מקבל את ה-placeholders של התמונות
