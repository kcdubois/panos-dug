from setuptools import setup

setup(
    name='panos_uid_worker',
    version='0.1.0',
    py_modules=['worker'],
    install_requires=[
        'click',
        'pydantic',
        'pan-os-python',
        'pika'
    ],
    entry_points={
        'console_scripts': [
            'panos-worker = worker.app:cli',
        ],
    },
)
