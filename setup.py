from setuptools import setup

setup(
    name='worker',
    version='0.1.0',
    py_modules=['worker'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'panos-worker = worker.app:cli',
        ],
    },
)
