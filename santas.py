#!/usr/bin/env python3

import os
import json
import random
from string import Template
import sys

from hamiltonian_cycle_finder import HamiltonianCycleFinder
from send import send_email


def randomize(santas):
    keys = list(santas.keys())
    random.shuffle(keys)
    return {key: santas[key] for key in keys}


if __name__ == "__main__":
    user = os.environ.get("USER")
    password = os.environ.get("PASSWORD")

    jsonfile = sys.argv[1]
    email_content = sys.argv[2]

    with open(jsonfile) as f:
        santas = json.load(f)
        n = len(santas)
        random_santas = randomize(santas)
        cycle_finder = HamiltonianCycleFinder()
        cycle_finder.validPath(n, random_santas)
        santa_cycle = cycle_finder.solution
        santa_cycle.pop()

        with open(email_content) as c:
            content = Template(c.read())
            for i, santa in enumerate(santa_cycle):
                name = santa
                email = santas[name]["email"]
                # get next person in cycle
                k = (i + 1) % n
                next_person_name = santa_cycle[k]
                body = content.substitute(
                    addressee=name.capitalize(),
                    name=next_person_name.capitalize(),
                )
                send_email(
                    f"{user}@gmail.com",
                    email,
                    "Secret Santa",
                    body,
                    user,
                    password,
                )
