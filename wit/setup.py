from setuptools import setup

setup(
    name='wit',
    version='0.1.0',
    # הוסף כאן את files_func וכל קובץ אחר שחסר
    py_modules=['wit', 'init', 'add', 'commit', 'checkout', 'status', 'files_func'],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'wit = wit:cli',
        ],
    },
)