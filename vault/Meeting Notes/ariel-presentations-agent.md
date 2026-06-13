# Ariel — Presentations Agent

## Overview
אריאל הוא הסוכן הרביעי בצוות (אחרי יעל/יובל/חן) — **מומחה המצגות**. הוא הופך תוכן מתיקיית `Content PPTX/` למצגת `.pptx` מעוצבת ב-`Output PPTX/`, דרך הסקיל `pptx` (מבוסס `python-pptx`). הקלט נתמך במגוון פורמטים (`.md`/`.txt`/`.pdf`/`.docx`/`.xlsx`), הוא מחיל סגנון בית מ-`ariel/templates/`, בונה גרפים/טבלאות native, יודע לערוך דק קיים, ולייצא ל-PDF דרך PowerPoint COM. התמונות מגיעות מיובל בתהליך דו-שלבי שראובן מתאם (אריאל מציין image-specs ב-Pass 1, משבץ ב-Pass 2). הגדרת הסוכן: `.claude/agents/ariel.md`.

## Open Questions
- צבעי/פונטי מותג ב-`ariel/templates/style-guide.md` הם ברירת-מחדל נייטרלית — להחליף בערכי מותג רשמיים כשיהיו.
- `house-template.pptx` הוא בסיס 16:9 מינימלי בלבד (ללא לוגו/layouts מותאמים) — אפשר להעשיר בהמשך.
- קלט `.xlsx` נתמך, אך אינטגרציה עם תוצרי רחל ב-`Planning_Output/` (גרפים/טבלאות) עדיין לא מומשה/נבדקה בפועל.
- File Docs עדיין לא מכסה את הקבצים החדשים: `ariel/templates/style-guide.md`, `ariel/templates/house-template.pptx`, ותיקיות `Content PPTX/` / `Output PPTX/` (טענת ה-85/85 ב-[[file-docs-vault]] התיישנה).

## Session Log

### 2026-06-11 — יצירת אריאל + שדרוג למומחה מצגות [shipped]
- **What was done:**
  - נוצר הסוכן `.claude/agents/ariel.md` (frontmatter + Workflow דו-שלבי סביב תמונות מיובל), עודכן `CLAUDE.md` (רשימת צוות, תהליך "מצגת עם תמונות", מבנה תיקיות), ונוצרו `Content PPTX/`, `Output PPTX/`, `ariel/templates/`.
  - הותקן **Python אמיתי 3.12.10** (winget) כי `python` בסביבה היה רק stub של Windows Store; הותקנו `python-pptx`, `pypdf`, `pdfplumber`, `python-docx`, `openpyxl`.
  - נוספו יכולות מומחה: קלט רב-פורמטי (PDF/Word/Excel), סגנון בית (`ariel/templates/style-guide.md` + `house-template.pptx`), גרפים/טבלאות native, עריכת דק קיים, וייצוא ל-PDF דרך PowerPoint COM.
- **Decisions:**
  - **מנוע מצגות = הסקיל `pptx` (python-pptx)** ולא ספריית node — לפי בחירת המשתמש, אחרי שהתגלה שה-python היה stub (התקנת python אמיתי פתרה זאת).
  - **שמות תיקיות עם רווח** (`Content PPTX/` / `Output PPTX/`) לפי בחירת המשתמש — מחייב מרכאות בכל נתיב ב-shell.
  - **סגנון בית מיושם per-shape תכנותית** (font/size/RGBColor) ולא דרך theme גלובלי, כי python-pptx לא עורך theme בקלות.
  - **ייצוא PDF דרך PowerPoint COM** ולא LibreOffice — PowerPoint כבר מותקן בסביבה (`POWERPNT.EXE`, Office16), COM אומת עובד.
  - **אריאל לא קורא ישירות ליובל** — מחזיר image-specs לראובן, כמו הגבול של יעל/חן.
- **Notes / Caveats:**
  - אומת end-to-end: נבנה דק בדיקה עם תמונה משובצת; דק עם גרף עמודות + טבלה מעוצבים; והמרת `.pptx`→`.pdf` (32KB) דרך COM. כל ה-artifacts של הבדיקות נמחקו.
  - PowerPoint COM דורש **נתיבים מוחלטים** (`SaveAs(dst, 32)`, 32=ppSaveAsPDF).
  - ה-PATH ברמת המשתמש מעדיף את ה-python האמיתי על-פני ה-stub של WindowsApps — שלים חדשים יפתרו `python` נכון.
- **Related:** [[agent-ariel]], [[agent-yuval]], [[agent-yael]], [[agent-chen]], [[file-CLAUDE]], [[skill-gpt-image-gen]], [[file-docs-vault]]
