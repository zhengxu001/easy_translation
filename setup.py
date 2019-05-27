from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='easy_translation',
    version='0.1dev',
    author="Xu Zheng",
    author_email="zhengxu5511@gmail.com",
    description="A quick Chinese<->English translation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhengxu001/easy_translation",
    install_requires=['googletrans',],
    scripts=['easy_translation/et'],
)