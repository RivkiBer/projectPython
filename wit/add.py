import shutil
#פונקציה שבודקת את תיקיית staged_file ומכניסה לשם את כל הקבצים ששונו עם כל הבדיקות

def add_to_stage(file_name):
    if not os.path.exists('.wit/staged_file'):
        print("you need to initialize the repository first")
        return
    if is_file_changed(file_path):
        os.remove('.wit/staged_file/file_name')
        shutil.copy(file_path, '.wit/staged_file')




def is_file_changed(file_name):
    if os.path.exists('.wit/staged_file/file_name'):
            return not if_files_equal(file_name, '.wit/staged_file/file_name')
    if os.path.exists('.wit/commits/head.txt'):
        with open('.wit/commits/head.txt', 'r') as head_file:
            head_commit = head_file.read().strip()
            if head_commit:
                commit_path = f'.wit/commits/{head_commit}/{file_name}'
                if os.path.exists(commit_path):
                    return not if_files_equal(file_name, commit_path)


def if_files_equal(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read() == f2.read()
