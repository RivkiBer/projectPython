### פרטים ID וכו ע"י פונקציות נוספות ומכניסה תיקייה חדשה עם הקבצים עם השינויים"#
#יוצR HEAD שמצביע על הCOMMIT האחרון המשתנה יהיה מצביע על כל השמות
# -*- coding: utf-8 -*-
import os
import shutil
import datetime


def create_commit(message):

   if not os.path.exists('.wit/staged_file'):
        print("you need to do add Command before commit")
        return

   commit_id=get_commit_id()
   os.makedirs(f".wit/commits/{commit_id}/files")
   source = '.wit/staged_file'
   dest= f".wit/commits/{commit_id}.files"
   shutil.copytree(source, dest)
   os.makedirs(f".wit/commits/{commit_id}")
   with open(f".wit/commits/{commit_id}/details.txt", "w") as details_file:
         details_file.write(f"Date: {datetime.datetime.now()}\n")
         details_file.write(f"Message: {message}\n")


def get_commit_id():




