#!/bin/python
from math import inf
from heapq import heappop, heappush

test_graph = {
        'A': [(3, 'B'), (1, 'C'), (5, 'D')],
        'B': [(1, 'D'), (3, 'E'), (12, 'A')],
        'C': [(3, 'E'), (1, 'B'), (2, 'A')],
        'D': [(1, 'E'), (2, 'B'), (3, 'C')],
        'E': [(2, 'D'), (1, 'B')]
        }


def dijkstra(graph, start):
    distances = {}
    distances[start] = 0
    for vertex in graph:
        if vertex != start:
            distances[vertex] = inf
    to_check = [(0, start)]
    while to_check:
        total, current_vertex = heappop(to_check)
        for distance, neighbor in graph[current_vertex]:
            new_total = total + distance
            if new_total < distances[neighbor]:
                distances[neighbor] = new_total
                heappush(to_check, (new_total, neighbor))
    return distances


if __name__ == "__main__":
    choices = [vertex for vertex in test_graph]
    choice = ""
    while choice.upper() not in choices:
        print("Pick a starting point from the following list:")
        for _choice in choices:
            print(" - " + _choice)
        choice = input("> ")
    print(dijkstra(test_graph, choice.upper()))

