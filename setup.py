from setuptools import setup, find_packages

setup(
    name="simpleduration",
    version="0.1.0",
    author="Anders Pearson",
    author_email="anders@columbia.edu",
    url="http://github.com/thraxil/simpleduration/",
    description="simple duration parsing library",
    long_description="convert human readable durations to python timedeltas",
    install_requires = [""],
    scripts = [],
    license = "BSD",
    platforms = ["any"],
    zip_safe=False,
    packages=find_packages(),
    test_suite='nose.collector',
    )
