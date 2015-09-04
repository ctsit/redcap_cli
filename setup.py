from setuptools import setup

# @see https://pythonhosted.org/setuptools/setuptools.html

setup(
    name='redcap_cli',
    version='0.1.0',
    packages=['redcap_cli'],
    url='https://github.com/ctsit/redcap_cli',
    license='Apache 2.0',
    author='pbc',
    author_email='ctsit@ctsi.ufl.edu',
    description='A suite of command line utilities for REDCap with a focus on API interaction.',
    long_description=open('README.rst').read(),
    install_requires=[
        "pycap >= 1.0",
    ],
    entry_points={
        'console_scripts': [
            'redcap_records = redcap_cli.redcap_records:main',
            'redcap_metadata = redcap_cli.redcap_metadata:main',
        ],
    },
    tests_require=[
        "pycap >= 1.0",
    ],
    test_suite='tests',
)
