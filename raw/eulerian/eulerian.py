#!/usr/bin/env python

graph = {1:[2,3,5],2:[1,3],3:[1,4,5],4:[2,3], 5:[1,3]}

def isodd(n):
    return n % 2 == 1

def check_eulerian(g):
    # odd_vertex_list = [v for v, n in g.iteritems() if isodd(len(n))]
    odd_vertex_list = []
    for vertex, neighbors in g.items():
        if isodd(len(neighbors)):
            odd_vertex_list.append(vertex)
    if len(odd_vertex_list) == 0 or len(odd_vertex_list) == 2:
        return True,odd_vertex_list
    else:
        return False,[]

print(f'{check_eulerian(graph)}')
