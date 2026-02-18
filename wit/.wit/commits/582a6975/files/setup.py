from setuptools import setup

setup(
    name='wit',
    version='0.1.0',
    py_modules=['wit', 'init', 'add', 'commit', 'status', 'files_func', 'checkout'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'wit = wit:cli',
        ],
    },
)