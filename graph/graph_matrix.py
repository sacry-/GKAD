#!/usr/bin/python
# -*- coding: utf-8 -*-
from graph_module import isDirected

class GraphMatrix():
    
    def __init__(self, g):
        self.g = g
        self.vertices = sorted(self.g.vertices(), key=lambda x: x.name())
        self.m = [[]]

    def __repr__(self):
        acc = "\n   v" + " v".join([str(_) for _ in range(1, len(self.m)+1)])
        for idx, row in enumerate(self.m):
            acc += "\nv" + str(idx + 1) + " " + str(row)
        return acc

    # |V| x |V|
    def toAdjacentMatrix(self):
        self.m = self.__initAdjacentMatrix__(len(self.vertices))
        for i, v1 in enumerate(self.vertices):
            for j, v2 in enumerate(self.vertices):
                vn1, vn2 = v1.name(), v2.name()
                e_count = len(self.g.edgeSrcDestList(vn1, vn2))
                self.m[i][j] += e_count
        return self.m

    def __initAdjacentMatrix__(self, size):
        return [[0 for _ in range(0, size)] for _ in range(0, size)]

    # |V| x |E|
    def toIncidentMatrix(g):   
        if isDirected(g):
            return __inciDirected__(g)
        return __inciUndirected__(g)


    def __inciDirected__(g):
        pass


    def __inciUndirected__(g):
        pass
    
