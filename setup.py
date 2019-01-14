from setuptools import setup, find_packages

setup(
    name="diffcsv",
    version="1.6",
    author=u"Uğur Soğukpınar",
    author_email="sogukpinar.ugur@gmail.com",
    url="https://github.com/ugursogukpinar/diff-csv",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "diffcsv = diffcsv.main:main",
        ],
    },
    license="LICENSE.txt",
    description="Find difference between two large csv files",
    long_description=open("README.md").read(),
    install_requires=list(filter(None, [
    ])),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)