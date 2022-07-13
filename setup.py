from setuptools import setup

setup(
    name='panos-worker',
    version='0.1.0',
    py_modules=['worker'],
    install_requires=[
        'Click',
        'Pydantic'
    ],
    entry_points={
        'console_scripts': [
            'panos-worker = worker.app:cli',
        ],
    },
)
