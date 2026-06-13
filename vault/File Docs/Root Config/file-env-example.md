---
file: .env.example
owner: כל הצוות (תשתית)
type: template
tags:
  - file-docs
  - env
  - template
---

# .env.example

**נתיב:** `.env.example`
**שייך ל:** תשתית משותפת

## מה הקובץ עושה
תבנית לדוגמה של [[file-env]]. מתעד אילו משתני סביבה הפרויקט צריך, עם ערכי placeholder (`your-anthropic-api-key-here` וכו'). משתמש חדש מעתיק את הקובץ ל-`.env` וממלא ערכים אמיתיים. בניגוד ל-`.env`, הקובץ הזה **כן** עולה ל-Git (אין בו סודות).

מתעד את המשתנים: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL` (ברירת מחדל `claude-opus-4-8`), `SEARCH_API_KEY`, `IMAGE_API_KEY`, `OPENAI_API_KEY`.

## קבצים קשורים
- [[file-env]] — הקובץ האמיתי שנוצר מהתבנית הזו
- [[file-gitignore]] — מסביר למה `.env` מוחרג אבל התבנית לא
