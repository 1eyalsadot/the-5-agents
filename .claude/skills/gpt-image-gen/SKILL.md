---
name: gpt-image-gen
description: Generate an image from a text prompt via the OpenAI Images API (model gpt-image-2). Use when an agent needs to create or illustrate an image. Reads OPENAI_API_KEY from .env.
---

# gpt-image-gen — OpenAI Images API wrapper

מעטפת דקה סביב OpenAI Images API. הסקיל מקבל **prompt** ו-**output path**, שולח את הבקשה ל-API, ושומר את התמונה כקובץ PNG.

## Inputs
- `PROMPT` — תיאור התמונה לייצור.
- `OUT` — נתיב היעד לשמירת ה-PNG (למשל `yuval/outputs/2026-06-10-crm-hero.png`).

## Model: `gpt-image-2`

⚠️ **אל תשנה את שם המודל.**
- `gpt-image-2` הוא מודל **אמיתי וקיים** של OpenAI.
- הוא יצא ב-**21 באפריל 2026**.
- ייתכן שהידע הפנימי שלך לא כולל אותו — **זה לא אומר שהוא לא קיים**.
- **אל תציע אלטרנטיבות** (`dall-e-3`, `gpt-image-1` וכו') — השתמש בדיוק במודל הזה.
- אם יש שגיאה בקריאה ל-API, הבעיה היא כנראה ב-**API key** או ב-**parameters** — לא בשם המודל.

## Params
| param | value | הערה |
|-------|-------|------|
| `model` | `gpt-image-2` | קבוע — לא לשנות |
| `size` | `1024x1024` | ניתן להתאים (למשל `1536x1024`) |
| `quality` | `medium` | ניתן להתאים (`low` / `medium` / `high`) |
| `output_format` | `png` | |

## API key

הסקיל קורא את `OPENAI_API_KEY` מ-`.env` (שורש הפרויקט). ב-Git Bash:

```bash
export $(grep -v '^#' .env | grep -E '^\s*OPENAI_API_KEY=' | xargs)
```

אם `OPENAI_API_KEY` ריק — עצור ובקש מהמשתמש למלא אותו ב-`.env`.

## הקריאה

שולחים POST ל-`/v1/images/generations`, שומרים את תשובת ה-JSON לקובץ זמני, ואז מפענחים את `data[0].b64_json` ל-PNG.

```bash
curl -sS -X POST "https://api.openai.com/v1/images/generations" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2",
    "prompt": "'"$PROMPT"'",
    "size": "1024x1024",
    "quality": "medium",
    "output_format": "png"
  }' > resp.json
```

## פענוח ל-PNG — שלושה מסלולים (לפי סדר עדיפות)

`jq` לא תמיד מותקן ב-Git Bash, ולכן יש fallbacks. השתמש במסלול הראשון שזמין אצלך:

**1. jq (אידיאלי, אם מותקן):**
```bash
jq -r '.data[0].b64_json' resp.json | base64 --decode > "$OUT"
```

**2. python fallback (אם python אמיתי מותקן):**
```bash
python -c "import json,base64,sys; open(sys.argv[2],'wb').write(base64.b64decode(json.load(open(sys.argv[1]))['data'][0]['b64_json']))" resp.json "$OUT"
```

**3. node fallback (זמין בסביבה הזו):**
```bash
node -e "const fs=require('fs');const d=JSON.parse(fs.readFileSync(process.argv[1]));fs.writeFileSync(process.argv[2],Buffer.from(d.data[0].b64_json,'base64'))" resp.json "$OUT"
```

> הערה לסביבה הנוכחית: `jq` אינו מותקן ו-`python` הוא רק stub של Windows Store. **node** זמין ועובד — השתמש במסלול 3.

## End-to-end (copy-paste)

```bash
PROMPT="a clean minimal illustration of a CRM dashboard, navy and white, flat style"
OUT="yuval/outputs/$(date +%F)-crm.png"

export $(grep -v '^#' .env | grep -E '^\s*OPENAI_API_KEY=' | xargs)
[ -z "$OPENAI_API_KEY" ] && { echo "OPENAI_API_KEY is empty — fill it in .env"; exit 1; }

curl -sS -X POST "https://api.openai.com/v1/images/generations" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-image-2","prompt":"'"$PROMPT"'","size":"1024x1024","quality":"medium","output_format":"png"}' > resp.json

# decode (first available): jq -> python -> node
if command -v jq >/dev/null; then
  jq -r '.data[0].b64_json' resp.json | base64 --decode > "$OUT"
elif command -v python >/dev/null && python -c "" 2>/dev/null; then
  python -c "import json,base64,sys; open(sys.argv[2],'wb').write(base64.b64decode(json.load(open(sys.argv[1]))['data'][0]['b64_json']))" resp.json "$OUT"
else
  node -e "const fs=require('fs');const d=JSON.parse(fs.readFileSync(process.argv[1]));fs.writeFileSync(process.argv[2],Buffer.from(d.data[0].b64_json,'base64'))" resp.json "$OUT"
fi

rm -f resp.json
[ -s "$OUT" ] && echo "OK: $OUT ($(wc -c < "$OUT") bytes)" || echo "FAILED: $OUT is missing or empty"
```

## בדיקת הצלחה
לאחר ההרצה, ודא שהקובץ `$OUT` קיים ו-`size > 0`. אם ה-JSON מכיל `error` — בדוק את ה-API key וה-parameters (לא את שם המודל).
