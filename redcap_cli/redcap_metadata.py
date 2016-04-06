#!/usr/bin/env python

# Copyright 2015 University of Florida

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Contributors:
# Christopher P. Barnes <senrabc@gmail.com>
# Andrei Sura: github.com/indera
# Philip Chase <philipbchase@gmail.com>
# Ruchi Vivek Desai <ruchivdesai@gmail.com>
# Taeber Rapczak <taeber@ufl.edu>
# Nicholas Rejack <nrejack@ufl.edu>
# Copyright (c) 2015, University of Florida
# All rights reserved.

import sys, traceback
import logging
import argparse
from redcap import Project, RedcapError
import re
import pprint

def examine_exception(trace_limit):
    # Produce varying levels of output corresponding to verbosity level and length of stacktrace
    if trace_limit != 0:
        trace_len = len(sys.exc_info())
        adjusted_trace_limit = trace_len - (trace_len/trace_limit) + 1
        print(traceback.format_exc(limit=adjusted_trace_limit))
    else:
        print "Use '-v', flag to examine traceback"
        
def main():

    parser = argparse.ArgumentParser(
        description='Read project metadata from a REDCap Project')
    parser.add_argument(
        '--token',
        dest='token',
        default='',
        required=True,
        help='Specify the authentication/authorization token that will provide access to the REDCap project')
    parser.add_argument(
        '--url',
        dest='url',
        default='',
        required=True,
        help='Specify the url of the REDCap server to connect with')
    parser.add_argument(
        '--verify_ssl',
        dest='verify_ssl',
        default=True,
        help='Specify whether the SSL cert of the REDCap server should be checked')
    # parser.add_argument(
    #     '-f',
    #     '--forms',
    #     dest='forms',
    #     default='',
    #     help='Specify a list of forms, separated by spaces, for which metadata should be returned.')
    # parser.add_argument(
    #     '--fields',
    #     dest='fields',
    #     default='',
    #     help='Specify a list of fields, separated by spaces, for which metadata should be returned.')
    # Flag for additional verbosity
    parser.add_argument(
        '-v',
        dest="verbosity_level",
        action="count",
        default=0,
        help="Print stacktrace, use '-vv' or '-vvv' to print longer traceback"
        )

    # prepare the arguments we were given
    args = vars(parser.parse_args())

    # set trace limit by verbosity level
    trace_limit = args['verbosity_level']

    # prepare the arguments we were given
    args = vars(parser.parse_args())

    # Turn the 'verify_ssl' parameter into the truth value we need to make a
    # REDCap connection
    if args['verify_ssl'] == 'y':
        args['verify_ssl'] = True
    elif args['verify_ssl'] == 'n':
        args['verify_ssl'] = False
    else:
        args['verify_ssl'] = True

    # Attempt to connect to the REDCap project
    try:
        project = Project(args['url'], args['token'], "", args['verify_ssl'])
    except:
        
        print "Cannot connect to project at " + args['url'] + ' with token ' + args['token']

        # Handle examination of stack trace dynamically
        examine_exception(trace_limit)

        quit()

    # my_forms = args['forms'].split()
    # my_fields = args['fields'].split()
    data = project.export_metadata(
        # forms=my_forms,
        # fields=my_fields,
        format='csv')
    print unicode(data)

if __name__ == '__main__':
    main()
