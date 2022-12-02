#!/usr/bin/env python3

import os
import json
import random
from string import Template
import sys

from hamiltonian_cycle_finder import HamiltonianCycleFinder
from send import send_email

user = os.environ.get('USER')
password = os.environ.get('PASSWORD')

jsonfile = sys.argv[1]
email_content = sys.argv[2]

test_user = 'jgwil2'

def randomize(santas):
    keys = list(santas.keys())
    random.shuffle(keys)
    return { key: santas[key] for key in keys }

if __name__ == '__main__':
    with open(jsonfile) as f:
        with open(email_content) as c:
            content = Template(c.read())
            santas = json.load(f)
            n = len(santas)
            random_santas = randomize(santas)
            cycle_finder = HamiltonianCycleFinder()
            cycle_finder.validPath(n, random_santas)
            print(cycle_finder.solution)

            #for i, santa in enumerate(santas):
            #    name, email = santa
            #    k = (i + 1) % l
            #    print('To:', santas[k][1])
            #    print(content.substitute(name=name.capitalize()))
