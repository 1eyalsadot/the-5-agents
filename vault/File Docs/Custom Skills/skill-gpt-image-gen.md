---
file: .claude/skills/gpt-image-gen/SKILL.md
owner: יובל
type: skill
tags:
  - file-docs
  - skill
  - image
---

# gpt-image-gen/SKILL.md

**נתיב:** `.claude/skills/gpt-image-gen/SKILL.md`
**שייך ל:** יובל

## מה הקובץ עושה
מעטפת דקה סביב **OpenAI Images API** (מודל `gpt-image-2`). מקבל `PROMPT` ו-`OUT`, שולח POST ל-`/v1/images/generations`, ומפענח את `data[0].b64_json` ל-PNG.
- קורא `OPENAI_API_KEY` מ-[[file-env]].
- שלושה מסלולי פענוח לפי זמינות: jq → python → **node** (בסביבה הזו node הוא הזמין).
- אזהרה מפורשת: **לא לשנות את שם המודל** `gpt-image-2` (יצא 21/04/2026) ולא להציע אלטרנטיבות.

## קבצים קשורים
- [[agent-yuval]] — הסוכן היחיד שמשתמש בסקיל הזה
- [[file-env]] — מקור מפתח ה-API
- [[yuval-workspace-index]] — היעד לתמונות שנוצרות
