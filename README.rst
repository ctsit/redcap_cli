redcap\_cli
===========

REDCap Command Line Interface
-----------------------------

REDCap CLI is a suite of tools for interacting with Vanderbilt
University's Research Electronic Data Capture, tool know as REDCap.
These tools provide a command line interface for interacting with a
REDCap server's application programming interface (API). REDCAp CLI is
written in Pythin and uses the PyCap library for all interaction with
the API.

Installation
------------

To install from source, use setup.py

::

    python setup.py install

To install from the Python Package Index, use your favorite python
package installer:

::

    pip install redcap_cli

or

::

    easy_install redcap_cli

Package Contents
----------------

REDCap CLI currently installs two utilities:

-  redcap\_records - imports and exports data from a REDCap project.
-  redcap\_metadata - exports project metadata from a REDCap project.

Usage Instructions
------------------

The redcap\_cli utilities have a rich list of command line options.
These options reflect the features and terminology of the REDCap API. To
see the options supported by each tool. Run the tool with the "-h"
option.

::

    # redcap_records.py -h
    usage: redcap_records.py [-h] --token TOKEN --url URL
                             [--verify_ssl VERIFY_SSL] [-i IMPORT_DATA] [-f FORMS]
                             [-t {json,csv,xml}] [--fields FIELDS] [-e EVENTS]
                             [-r RECORDS]

    Read some data from a REDCap Project

    optional arguments:
      -h, --help            show this help message and exit
      --token TOKEN         Specify the authentication/authorization token that
                            will provide access to the REDCap project
      --url URL             Specify the url of the REDCap server to connect with
      --verify_ssl VERIFY_SSL
                            Specify whether the SSL cert of the REDCap server
                            should be checked
      -i IMPORT_DATA, --import_data IMPORT_DATA
                            Specify the input data file to load into REDCap
      -f FORMS, --forms FORMS
                            Specify a list of forms, separated by spaces, for
                            which data should be returned.
      -t {json,csv,xml}, --type {json,csv,xml}
                            Specify the file type used as input or output. Valid
                            types: json, csv, xml
      --fields FIELDS       Specify a list of fields, separated by spaces, for
                            which data should be returned.
      -e EVENTS, --events EVENTS
                            Specify a list of events, separated by spaces, for
                            which data should be returned.
      -r RECORDS, --records RECORDS
                            Specify a list of records, separated by spaces, for
                            which data should be returned.

Input data
----------

REDCap CLI tools consume data in the exact formats it generates for
output. To generate an example input file, for a project, populate the
project with the project with sample data and export it with
redcap\_records. The same data can be reimported when using the same
command line options.

Output data
-----------

Data output by REDCap records is kept as close as possible to the native
REDCap output. The output data is only modified to enhance readability
on the command line or improve re-import.

Requirements
------------

This project requires Python 2.7 or greater and PyCap 1.0 or greater.

Contributions
-------------

The redcap\_CLI Team welcomes contributions to this project. Please fork
and send pull requests with your revisions.
