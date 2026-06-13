---
file: .claude/agents/chen.md
owner: חן
type: agent-config
tags:
  - file-docs
  - agent
  - research
---

# chen.md — חן, חוקרת הרשת

**נתיב:** `.claude/agents/chen.md`
**שייך ל:** חן

## מה הקובץ עושה
הגדרת הסוכנת **חן** — חוקרת הרשת. מוצאת מאמרים ומקורות עדכניים ואמינים לפי בקשה מראובן, מסננת לפי איכות, ומכינה קלט ליעל ב-`Content/` (עם לינק למקור בראש הקובץ).
- **כלים:** WebSearch, WebFetch, Read, Write, Edit, Glob, Grep (בלי Bash/API חיצוני).
- **זיכרון:** לפני כל חיפוש בודקת ב-[[chen-searches]] (Grep) אם כבר חיפשה נושא דומה; אחרי כל חיפוש מוסיפה entry.
- **גבול ארכיטקטוני:** לא קוראת ישירות ליעל — רק מניחה ב-`Content/` ומדווחת לראובן.
- **מילות הפעלה:** חפש, מצא, מחקר, מאמר על / search, find, research, latest on.

## קבצים קשורים
- [[file-CLAUDE]] — ראובן, שמפעיל את חן
- [[chen-searches]] — לוג הזיכרון של חן
- [[content-index]] — היכן חן מניחה את הממצאים
- [[agent-yael]] — צורכת בהמשך את מה שחן מצאה
