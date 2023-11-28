from copy import copy
from typing import Dict, List


class HamiltonianCycleFinder:
    def __init__(self):
        self.finished = False
        self.solution = []

    def generateAdjacencyList(self, n, participants) -> Dict[str, List[str]]:
        keys = participants.keys()
        adjacency_list: Dict[str, List[str]] = {p: [] for p in participants}
        for name, detail in participants.items():
            for key in keys:
                if key not in detail["excludes"] and key != name:
                    adjacency_list[name].append(key)
        return adjacency_list

    def validPath(self, n: int, participants) -> List[str]:
        adjacency_list = self.generateAdjacencyList(n, participants)
        source = list(adjacency_list)[0]
        target = source
        stack = [source]
        visited = {node: False for node in list(adjacency_list)}

        return self.backtrack(stack, visited, adjacency_list)

    def backtrack(
        self,
        stack: List[str],
        visited: Dict[str, bool],
        data: Dict[str, List[str]],
    ) -> List[str]:
        if self.is_solution(stack, visited, data):
            self.finished = True
            self.solution = copy(stack)
        else:
            candidates = self.construct_candidates(stack, visited, data)
            for candidate in candidates:
                stack.append(candidate)
                visited[candidate] = True
                self.backtrack(stack, visited, data)
                stack.pop()
                visited[candidate] = False
                if self.finished:
                    return

    def is_solution(
        self,
        stack: List[str],
        visited: Dict[str, bool],
        data: Dict[str, List[str]],
    ) -> bool:
        return stack[-1] == stack[0] and len(stack) - 1 == len(list(data))

    def construct_candidates(
        self,
        stack: List[str],
        visited: Dict[str, bool],
        data: Dict[str, List[str]],
    ) -> List[str]:
        current_node = stack[-1]
        return [node for node in data[current_node] if not visited[node]]
