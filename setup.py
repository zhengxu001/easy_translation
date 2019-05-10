from setuptools import setup

setup(
    name='et',
    version='0.1dev',
    install_requires=['googletrans',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    scripts=['easy_translation/et'],
)