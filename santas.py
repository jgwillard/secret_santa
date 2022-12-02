#!/usr/bin/env python3

import os
import json
from string import Template
import sys
from typing import Dict, List

from send import send_email

user = os.environ.get('USER')
password = os.environ.get('PASSWORD')

jsonfile = sys.argv[1]
email_content = sys.argv[2]

test_user = 'jgwil2'

def generateAdjacencyList(n, participants):
    keys = participants.keys()
    adjacency_list: Dict[str, List[str]] = {p: [] for p in participants}
    for name, detail in participants.items():
        for key in keys:
            if key not in detail['excludes'] and key != name:
                adjacency_list[name].append(key)
    return adjacency_list


def validPath(
    n: int, adjacency_list: Dict[str, List[str]]
) -> List[str]:
    source = list(adjacency_list)[0]
    target = source
    stack = [source]
    visited = { node: False for node in list(adjacency_list)}

    return backtrack(stack, visited, adjacency_list)


def backtrack(
    stack: List[str],
    visited: Dict[str, bool],
    data: Dict[str, List[str]]
) -> List[str]:
    if is_solution(stack, visited, data):
        print(stack)
    else:
        candidates = construct_candidates(stack, visited, data)
        for candidate in candidates:
            stack.append(candidate)
            visited[candidate] = True
            backtrack(stack, visited, data)
            stack.pop()
            visited[candidate] = False

def is_solution(
    stack: List[str],
    visited: Dict[str, bool],
    data: Dict[str, List[str]]
) -> bool:
    #print(stack, len(stack), len(list(data)))
    #print(stack[-1], stack[0])
    #print(stack[-1] == stack[0] and len(stack) - 1 == len(list(data)))
    return stack[-1] == stack[0] and len(stack) - 1 == len(list(data))

def construct_candidates(
    stack: List[str],
    visited: Dict[str, bool],
    data: Dict[str, List[str]]
) -> List[str]:
    current_node = stack[-1]
    return [node for node in data[current_node] if not visited[node]]


with open(jsonfile) as f:
    with open(email_content) as c:
        content = Template(c.read())
        santas = json.load(f)
        n = len(santas)
        adjacency_list = generateAdjacencyList(n, santas)
        print(validPath(n, adjacency_list))
        #for i, santa in enumerate(santas):
        #    name, email = santa
        #    k = (i + 1) % l
        #    print('To:', santas[k][1])
        #    print(content.substitute(name=name.capitalize()))
