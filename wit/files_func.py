import os
import shutil


def copy_files(src, dest, skip=''):
    if True:
     shutil.copytree(src, dest, ignore=shutil.ignore_patterns(*skip), dirs_exist_ok=True)

    # מחיקת הנתיב הקיים אם קיים
def remove_path(path):
     if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                 os.remove(path)



def if_files_equal(file1, file2):
    if os.path.isdir(file1) or os.path.isdir(file2):
        return False
    try:
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            return f1.read() == f2.read()
    except Exception as e:
        print(f"Error comparing files: {e}")
        return False


def if_folders_equals(dir1, dir2):
    """השוואה רקורסיבית בין שתי תיקיות."""

    # בדיקת רשימת הפריטים בתיקייה (קבצים ותת-תיקיות)
    try:
        items1 = sorted(os.listdir(dir1))
        items2 = sorted(os.listdir(dir2))
    except OSError:
        # אם אחד הנתיבים הוא לא תיקייה, הם לא שווים כתיקיות
        return False

    if items1 != items2:
        return False

    for item in items1:
        path1 = os.path.join(dir1, item)
        path2 = os.path.join(dir2, item)

        if os.path.isdir(path1) and os.path.isdir(path2):
            # אם שניהם תיקיות - ממשיכים ברקורסיה צעד אחד פנימה
            if not if_folders_equals(path1, path2):
                return False
        elif os.path.isfile(path1) and os.path.isfile(path2):
            # אם שניהם קבצים - משווים את התוכן שלהם (כאן הרקורסיה נעצרת)
            if not if_files_equal(path1, path2):
                return False
        else:
            # אם אחד תיקייה והשני קובץ - הם לא שווים
            return False

    return True

def check_name_in_file(name_to_find, path):
    if not os.path.exists(path):
        return False
    with open(f'{path}', 'r', encoding='utf-8') as file:
        for line in file:
            if name_to_find.strip() == line.strip():
                return True
    return False


def find_file_in_folder(file_name, path):
        for root, dirs, files in os.walk(path):
            # אם נמצא תיקיה בשם 'name'
            if file_name in dirs:
                return os.path.join(root, file_name)
            # אם נמצא קובץ בשם 'name'
            elif file_name in files:
                return os.path.join(root, file_name)
        return None




def is_file_changed(path_file):
    """
    בודק אם קובץ השתנה מאז שנוסף לסטייג'ינג או הקומיט האחרון.
    """
    try:
        file_name = os.path.basename(path_file)

        # התעלמות מקבצים שנמצאים ב-.witignore
        if check_name_in_file(file_name, '.wit/.witignore.txt'):
            return False

        staged_file_path = os.path.join('.wit', 'staged_file', file_name)

        if os.path.exists(staged_file_path):
            # אם קיים כבר קובץ בסטייג'ינג, נוודא שהוא שונה
            if os.path.isdir(path_file):
                return not if_folders_equals(path_file, staged_file_path)
            else:
                return not if_files_equal(path_file, staged_file_path)

        # אם אין קובץ בסטייג'ינג, נבדוק אם יש אותו בקומיט האחרון
        head_path = '.wit/commits/head.txt'
        if os.path.exists(head_path):
            with open(head_path, 'r', encoding='utf-8') as head_file:
                head_commit = head_file.read().strip()
                commit_path = f'.wit/commits/{head_commit}'
                if os.path.exists(commit_path):
                    path = find_file_in_folder(file_name, commit_path)
                    if path is not None:
                        if os.path.isdir(path):
                            return not if_folders_equals(path, path_file)
                        elif if_files_equal(path, path_file):
                            return False
        return True

    except Exception as e:
        raise Exception(f"נפלה שגיאה במהלך בדיקת שינויים לקובץ {path_file}: {e}")


