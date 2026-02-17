# -*- coding: utf-8 -*-
import os
import hashlib

# הגדרת נתיבים (השתמש בנתיב יחסי כדי שזה יעבוד בכל מחשב)
BASE_PATH = os.getcwd()
WIT_DIR = os.path.join(BASE_PATH, ".wit")
STAGED_DIR = os.path.join(WIT_DIR, "staged_file")
COMMITS_DIR = os.path.join(WIT_DIR, "commits")
HEAD_FILE = os.path.join(COMMITS_DIR, "head.txt")
WIT_IGNORE = os.path.join(WIT_DIR, ".witignore.txt")


def is_wit_initialized():
    return os.path.exists(WIT_DIR)


def get_ignored_list():
    """מחזיר רשימת קבצים ותיקיות להתעלמות"""
    skip = [".wit", ".git", "__pycache__"]
    if os.path.exists(WIT_IGNORE):
        with open(WIT_IGNORE, 'r', encoding='utf-8') as f:
            skip += [line.strip() for line in f if line.strip()]
    return skip


def get_head_id():
    """קריאת ה-ID של הקומיט האחרון"""
    if os.path.exists(HEAD_FILE):
        with open(HEAD_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            return content if content else None
    return None


def compare_files(f1, f2):
    """השוואה בינארית של קבצים (הכי בטוח)"""
    if not os.path.exists(f1) or not os.path.exists(f2):
        return False
    if os.path.isdir(f1) or os.path.isdir(f2):
        return False

    def hash_file(path):
        h = hashlib.md5()
        with open(path, 'rb') as file:
            while chunk := file.read(8192):
                h.update(chunk)
        return h.hexdigest()

    return hash_file(f1) == hash_file(f2)

