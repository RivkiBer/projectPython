#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from files_func import WIT_DIR, is_wit_initialized
import os

print(f"WIT_DIR: {WIT_DIR}")
print(f"WIT_DIR exists: {os.path.exists(WIT_DIR)}")
print(f"Is initialized: {is_wit_initialized()}")

if not is_wit_initialized():
    print("Creating .wit directory...")
    from init import create_init
    create_init()
    print("Done!")
else:
    print("Already initialized")

