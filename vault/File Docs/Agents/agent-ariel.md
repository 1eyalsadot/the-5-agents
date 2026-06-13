---
file: .claude/agents/ariel.md
owner: אריאל
type: agent-config
tags:
  - file-docs
  - agent
  - presentations
---

# ariel.md — אריאל, מומחה המצגות

**נתיב:** `.claude/agents/ariel.md`
**שייך ל:** אריאל

## מה הקובץ עושה
הגדרת הסוכן **אריאל** — מומחה המצגות. הופך תוכן מ-`Content PPTX/` למצגת `.pptx` מעוצבת ב-`Output PPTX/`, דרך הסקיל `pptx` (מבוסס `python-pptx`).
- **כלים:** Read, Write, Edit, Bash, Glob, Skill (Bash + Skill כדי להריץ את הסקיל `pptx`).
- **קלט רב-פורמטי:** `.md` / `.txt` / `.pdf` / `.docx` / `.xlsx` (דרך Read / הסקילים `pdf`/`docx`/`xlsx`).
- **תהליך דו-שלבי לתמונות:** Pass 1 מתכנן שקופיות ופולט `{{IMAGE_NEEDED: slide=, placement=, "..."}}`; ראובן מפעיל את יובל; Pass 2 בונה ומשבץ.
- **סגנון בית:** מחיל [[ariel-style-guide]] (צבעים/פונטים/פריסה) per-shape; פותח את `house-template.pptx` כבסיס 16:9.
- **יכולות מומחה:** גרפים/טבלאות native (לא תמונות), עריכת דק קיים, וייצוא ל-PDF דרך PowerPoint COM.
- **גבול ארכיטקטוני:** לא קורא ישירות ליובל — מחזיר image-specs לראובן.
- **מילות הפעלה:** מצגת, שקופית, תכין מצגת, דק, PPT / presentation, slides, deck, pptx.

## תלויות סביבה
Python אמיתי 3.12 + `python-pptx`, `pypdf`, `pdfplumber`, `python-docx`, `openpyxl`. ייצוא PDF דורש PowerPoint מותקן (COM). ראה [[ariel-presentations-agent]] ל-session log מלא.

## קבצים קשורים
- [[file-CLAUDE]] — ראובן, שמפעיל את אריאל
- [[agent-yuval]] — מייצר את התמונות שאריאל משבץ
- [[ariel-presentations-agent]] — Meeting Note עם החלטות והקשר
- [[skill-gpt-image-gen]] — שרשרת התמונות (יובל)
