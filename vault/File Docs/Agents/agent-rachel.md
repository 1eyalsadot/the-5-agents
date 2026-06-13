---
file: .claude/agents/rachel.md
owner: רחל
type: agent-config
tags:
  - file-docs
  - agent
  - data-analysis
---

# rachel.md — רחל, אנליסטית הנתונים

**נתיב:** `.claude/agents/rachel.md`
**שייך ל:** רחל

## מה הקובץ עושה
הגדרת הסוכנת **רחל** — אנליסטית הנתונים. לוקחת קובצי אקסל/CSV מ-`Planning_Data/`, מבצעת חישובים, נוסחאות, סינון וטבלאות ציר, ומפיקה ל-`Planning_Output/`: גרפים (PNG), קובץ xlsx מעובד, ודוח תובנות (Markdown).
- **כלים:** Read, Write, Edit, Bash, Glob, Skill (Bash+Skill דרושים לסקיל `xlsx` ולספריות Python).
- **עובדת רק עם המספרים שבקובץ:** לא ממציאה נתונים, לא משלימה ערכים חסרים, **לא ממירה שערי מטבעות/יחידות**.
- **גבול ארכיטקטוני:** לא קוראת ישירות לאריאל/יעל — רק מניחה ב-`Planning_Output/` ומדווחת לראובן.
- **מילות הפעלה:** אקסל, נתח, ניתוח נתונים, גרף, טבלת ציר / excel, xlsx, csv, analyze, pivot, chart.

## קבצים קשורים
- [[file-CLAUDE]] — ראובן, שמפעיל את רחל
- [[rachel-workspace-index]] — תיקיות הקלט/פלט של רחל
- [[agent-ariel]] — צורך בהמשך את הגרפים/טבלאות שרחל מפיקה למצגות
- [[skill-xlsx]] — הסקיל שרחל משתמשת בו לניתוח
