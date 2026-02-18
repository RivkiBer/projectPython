# -*- coding: utf-8 -*-
import os
import hashlib

# תיקיית העבודה הנוכחית - תוך תיקיית wit
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
WIT_DIR = os.path.join(BASE_PATH, ".wit")
STAGED_DIR = os.path.join(WIT_DIR, "staged_file")
COMMITS_DIR = os.path.join(WIT_DIR, "commits")
HEAD_FILE = os.path.join(COMMITS_DIR, "head.txt")
WIT_IGNORE = os.path.join(WIT_DIR, ".witignore.txt")


def get_paths(base_path=None):
    """החזרת כל נתיבי ה-WIT"""
    if base_path:
        wit_dir = os.path.join(base_path, ".wit")
    else:
        wit_dir = WIT_DIR

    staged_dir = os.path.join(wit_dir, "staged_file")
    commits_dir = os.path.join(wit_dir, "commits")
    head_file = os.path.join(commits_dir, "head.txt")
    wit_ignore = os.path.join(wit_dir, ".witignore.txt")

    return wit_dir, staged_dir, commits_dir, head_file, wit_ignore


def is_wit_initialized(base_path=None):
    if base_path:
        wit_dir = os.path.join(base_path, ".wit")
    else:
        wit_dir = WIT_DIR
    return os.path.exists(wit_dir)


def get_ignored_list(base_path=None):
    skip = [".wit", ".git", "__pycache__"]
    if base_path:
        wit_ignore = os.path.join(base_path, ".wit", ".witignore.txt")
    else:
        wit_ignore = WIT_IGNORE

    if os.path.exists(wit_ignore):
        with open(wit_ignore, 'r', encoding='utf-8') as f:
            skip += [line.strip() for line in f if line.strip()]
    return skip


def get_head_id(base_path=None):
    if base_path:
        head_file = os.path.join(base_path, ".wit", "commits", "head.txt")
    else:
        head_file = HEAD_FILE

    if os.path.exists(head_file):
        with open(head_file, "r", encoding="utf-8") as f:
            content = f.read().strip()
            return content if content else None
    return None


def compare_files(f1, f2):
    if not os.path.exists(f1) or not os.path.exists(f2):
        return False
    if os.path.isdir(f1) or os.path.isdir(f2):
        return False

    h = hashlib.md5()
    with open(f1, 'rb') as file1, open(f2, 'rb') as file2:
        while chunk := file1.read(8192):
            h.update(chunk)
        h2 = hashlib.md5()
        while chunk := file2.read(8192):
            h2.update(chunk)
    return h.hexdigest() == h2.hexdigest()
