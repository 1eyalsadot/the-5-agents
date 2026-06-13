---
file: .claude/agents/yuval.md
owner: יובל
type: agent-config
tags:
  - file-docs
  - agent
  - image
---

# yuval.md — יובל, מעצב התמונות

**נתיב:** `.claude/agents/yuval.md`
**שייך ל:** יובל

## מה הקובץ עושה
הגדרת הסוכן **יובל** — מעצב התמונות. אחראי על יצירת כל התמונות במערכת, מניסוח ה-prompt ועד שמירת ה-PNG. מטרת-על: **עקביות ויזואלית** בין כל התמונות.
- **כלים:** Read, Write, Bash, Glob (Bash דרוש לקריאת ה-API דרך הסקיל).
- **Workflow:** סורק `yuval/reference/` לחילוץ סגנון → מנסח prompt → קורא ל-[[skill-gpt-image-gen]] → שומר `<date>-<slug>.png` + `.txt` עם ה-prompt ב-`yuval/outputs/` → מאמת `size > 0` → מדווח.
- **תלות:** אם `OPENAI_API_KEY` ריק ב-[[file-env]] — עוצר ומבקש למלא.
- **מילות הפעלה:** תמונה של, ציור של, תיצור תמונה, איור / image of, illustration, draw.

## קבצים קשורים
- [[file-CLAUDE]] — ראובן, שמפעיל את יובל
- [[skill-gpt-image-gen]] — הסקיל שיובל קורא לו
- [[file-env]] — מקור `OPENAI_API_KEY`
- [[yuval-workspace-index]] — היכן יובל שומר תמונות
- [[yuval-reference-gitkeep]] — תיקיית ה-reference לסגנון
- [[agent-yael]] — מקור בקשות התמונה (placeholders)
