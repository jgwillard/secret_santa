#!/usr/bin/env python3

import csv
import os
import random
from string import Template
import sys

from send import send_email

user = os.environ.get('USER')
password = os.environ.get('PASSWORD')

csvfile = sys.argv[1]
email_content = sys.argv[2]

test_user = 'jgwil2'

with open(csvfile) as f:
    with open(email_content) as c:
        content = Template(c.read())
        santas = list(csv.reader(f))
        random.shuffle(santas)
        l = len(santas)
        for i, santa in enumerate(santas):
            name, email = santa
            k = (i + 1) % l
            print('To:', santas[k][1])
            print(content.substitute(name=name.capitalize()))
