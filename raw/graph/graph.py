#!/usr/bin/env python

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self,vertex):
        self.graph[vertex] = []

    def add_edge(self,start,end):
        self.graph[start].append(end)
        self.graph[end].append(start)

    def __check_vertex(self, vertex):
        return vertex in self.graph.keys()

    def __check_neighbor(self, vertex, neighbor):
        if self.__check_vertex(vertex) and self.__check_vertex(neighbor):
            return (neighbor in self.graph[vertex]) and (vertex in self.graph[neighbor])
        else:
            return False

    def delete_edge(self,start,end):
        if self.__check_neighbor(start, end):
            self.graph[start].remove(end)
            self.graph[end].remove(start)

    def delete_vertex(self,vertex):
        for neighbor in self.graph[vertex]:
            self.delete_edge(vertex,neighbor)
        del self.graph[vertex]

    def __str__(self):
        return str(self.graph)
