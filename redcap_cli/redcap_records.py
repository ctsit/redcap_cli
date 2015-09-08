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

import sys
import argparse
import json
from redcap import Project, RedcapError

def main():

    parser = argparse.ArgumentParser(
        description='Read some data from a REDCap Project')
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
    parser.add_argument('-i', '--import_data', dest='import_data', default='',
                        help='Specify the input data file to load into REDCap')
    parser.add_argument(
        '-f',
        '--forms',
        dest='forms',
        default='',
        help='Specify a list of forms, separated by spaces, for which data should be returned.')
    parser.add_argument(
        '-t',
        '--type',
        choices=['json', 'csv', 'xml'],
        dest='data_type',
        default='csv',
        help='Specify the file type used as input or output. Valid types: json, csv, xml')
    parser.add_argument(
        '--fields',
        dest='fields',
        default='',
        help='Specify a list of fields, separated by space or comma, for which data should be returned.')
    parser.add_argument(
        '-e',
        '--events',
        dest='events',
        default='',
        help='Specify a list of events, separated by space or comma, for which data should be returned.')
    parser.add_argument(
        '-r',
        '--records',
        dest='records',
        default='',
        help='Specify a list of records, separated by spaces or comma, for which data should be returned.')

    # prepare the arguments we were given
    args = vars(parser.parse_args())

    # According to http://pycap.readthedocs.org/en/latest/api.html
    # allowed data_types are: csv, json, xml
    data_type = args['data_type']

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
        quit()

    # either we export data...
    if args['import_data'] == '':
        my_forms = args['forms'].split()
        my_fields = args['fields'].split()
        my_events = args['events'].split()
        my_records = args['records'].split()
        data = project.export_records(
            forms=my_forms,
            format = data_type,
            fields=my_fields,
            events=my_events,
            records=my_records,
            event_name='unique')
        if 'json' == data_type:
            print json.dumps(data, ensure_ascii=False)
        else:
            print str(data)
    else:
        # ...or we import data
        file = args['import_data']
        try:
            input = open(file, 'r')
        except IOError:
            print "Cannot open file " + file
            quit()
        if 'json' == data_type:
            json_data = json.load(input)
            response = project.import_records(json_data)
        else:
            response = project.import_records(input.read(), format = data_type)

        print response

if __name__ == '__main__':
    main()
