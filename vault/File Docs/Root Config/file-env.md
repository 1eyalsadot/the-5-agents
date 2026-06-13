---
file: .env
owner: כל הצוות (תשתית)
type: secrets
tags:
  - file-docs
  - secrets
  - env
---

# .env

**נתיב:** `.env`
**שייך ל:** תשתית משותפת (נקרא בפועל ע"י יובל דרך gpt-image-gen)

## מה הקובץ עושה
מחזיק את **הסודות האמיתיים** של הפרויקט — מפתחות API וקונפיגורציה. בין השאר: `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`, `OPENAI_API_KEY` (משמש את יובל ליצירת תמונות), ומפתחות אופציונליים ל-חן/יובל.

> [!danger] לא עולה ל-Git
> הקובץ מוחרג ב-[[file-gitignore]]. אסור לעשות לו commit — הוא מכיל מפתחות אמיתיים.

## קבצים קשורים
- [[file-env-example]] — התבנית שממנה משכפלים את הקובץ הזה
- [[file-gitignore]] — מחריג את `.env`
- [[skill-gpt-image-gen]] — קורא את `OPENAI_API_KEY` מכאן
- [[agent-yuval]] — תלוי ב-`OPENAI_API_KEY` ליצירת תמונות
