#!/usr/bin/env python

from graph import Graph

g = Graph()

test_cases = [('add vertices',[(g.add_vertex,[1]), \
                               (g.add_vertex,[2]), \
                               (g.add_vertex,[3]), \
                               (g.add_vertex,[4])],
               '{1: [], 2: [], 3: [], 4: []}'), \
              ('  add edge  ',[(g.add_edge,[1,2]), \
                               (g.add_edge,[1,3])], \
               '{1: [2, 3], 2: [1], 3: [1], 4: []}'), \
              ('  negative  ',[(g.delete_edge,[3,777])], \
               '{1: [2, 3], 2: [1], 3: [1], 4: []}'), \
              ('test delete ',[(g.delete_vertex,[3]), \
                               (g.delete_edge,[1,4])], \
               '{1: [2], 2: [1], 4: []}')]

def run_test_case(graph, test_case):
    tc_name, tc_func, tc_expect = test_case
    for func in tc_func:
        f, a = func
        f(*a)
    result = str(graph) == tc_expect
    print(f'{tc_name}, result: {result}')
    return result

def run_test_cases(graph, test_cases):
    total_number = len(test_cases)
    pass_number = 0
    for test_case in test_cases:
        if run_test_case(graph, test_case): pass_number += 1
    print(f'== Pass rate {float(pass_number)/float(total_number)*100}% ({pass_number} out of {total_number})')

run_test_cases(g, test_cases)

'''
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
print g

g.add_edge(1,2)
g.add_edge(1,3)
print g.graph

g.delete_edge(3,777)
print g

g.delete_vertex(3)
g.delete_edge(1,4)
print g

'''
