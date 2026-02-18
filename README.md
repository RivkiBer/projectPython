# WIT - מערכת ניהול גרסאות

WIT היא מערכת ניהול גרסאות פשוטה (Version Control System) שנוצרה כפרויקט לימודי. היא מאפשרת לך לעקוב אחר שינויים בקבציך, ליצור checkpoints (commits) ולחזור לגרסאות קודמות של הקבצים.

## התקנה

### דרישות מקדימות
- Python 3.7 ו-מעלה
- Click (יתותקן אוטומטית)

### התקנה מקומית

```bash
cd projectPython
pip install -e wit/
```

## שימוש

### אתחול מאגר חדש

```bash
wit init
```

יוצר תיקייה `.wit` בתיקייה הנוכחית שמכילה את כל הנתונים הנדרשים לניהול הגרסאות.

### הוספת קבצים

```bash
wit add <file_name>
```

הוספת קובץ לאזור ההעריכה (staging area) כדי להכין אותו לcommit.

דוגמה:
```bash
wit add myfile.txt
```

### יצירת Commit

```bash
wit commit -m "הודעה תיאורית על השינויים"
```

יצירת נקודת ביקורת (checkpoint) עם תיאור של השינויים שבוצעו.

### בדיקת סטטוס

```bash
wit status
```

הצגת סטטוס הקבצים - אילו קבצים שונו, אילו בהעריכה, ואילו כבר committed.

### חזרה לגרסה קודמת

```bash
wit checkout <commit_id>
```

חזרה לגרסה מסוימת של הקבצים. זה מחליף את הקבצים בעותקים מה-commit המבוקש.

## מבנה הפרויקט

```
wit/
├── wit.py           # קובץ ראשי עם ה-CLI interface
├── init.py          # פונקציות אתחול המאגר
├── add.py           # פונקציות הוספת קבצים
├── commit.py        # פונקציות יצירת commits
├── status.py        # פונקציות הצגת סטטוס
├── checkout.py      # פונקציות חזרה לגרסאות קודמות
├── files_func.py    # פונקציות עזר לעבודה עם קבצים
├── setup.py         # קובץ setup לצורך התקנה
└── .wit/           # תיקייה המכילה את נתוני המאגר
```

## דוגמה לזרימת עבודה

```bash
# אתחול מאגר חדש
wit init

# יצירת קובץ חדש
echo "Hello World" > hello.txt

# הוספת הקובץ לstaging area
wit add hello.txt

# יצירת commit
wit commit -m "הוספת hello.txt"

# בדיקת סטטוס
wit status

# ערוך את הקובץ
echo "Hello WIT" > hello.txt

# הוספת השינוי החדש
wit add hello.txt

# יצירת commit חדש
wit commit -m "עדכון hello.txt"

# חזרה לגרסה הקודמת
wit checkout <commit_id>
```

## פרטים טכניים

### כיצד זה עובד?

1. **אתחול (.wit/)**: כשמריצים `wit init`, נוצרת תיקייה `.wit` שמאחסנת את כל הנתונים
2. **Staging**: כשמוסיפים קובץ עם `wit add`, הוא מתווסף ל-staging area
3. **Commit**: כשמריצים `wit commit`, נוצר snapshot של כל הקבצים בstaging area
4. **Status**: מציג את ההבדלים בין הגרסה הנוכחית ל-last commit
5. **Checkout**: מחזיר את הקבצים לגרסה מסוימת

### מבנה מאגר .wit

```
.wit/
├── commits/          # כל ה-commits בתוך תיקיות עם timestamp
├── staging/          # קבצים בהעריכה
└── metadata.json     # מידע על ה-commits וה-history
```

## הערות חשובות

- זוהי מערכת פשוטה למטרות לימודיות בלבד
- אין תמיכה בענפים (branches) או merge
- כל commit מאחסן את כל הקבצים (לא רק ההבדלים)
- קבצים בינריים עדיין נתמכים, אך עלול להיות זיכרון רב

## תהליך הפיתוח

הפרויקט התפתח בשלבים:
- אתחול של המערכת
- הוספת קבצים לtracking
- יצירת commits
- בדיקת סטטוס
- ציון לגרסאות קודמות

## עזרה ודוקומנטציה נוספת

הפעל את הפקודה הבאה להצגת כל הפקודות הזמינות:

```bash
wit --help
```

או לעזרה בפקודה מסוימת:

```bash
wit <command> --help
```

---

**יצרן**: פרויקט לימודי
**תאריך יצירה**: 2026
**שפה**: Python

