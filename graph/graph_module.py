#!/usr/bin/python
# -*- coding: utf-8 -*-
          
def nullgraph(g):
    return (not g.vertices()) and (not g.edges())

def empty(g):
    return not g.edges()

def isQuiver(g):
    return isDirected(g) and isMultigraph(g)

def isMixed(g):
    return len(
        filter(lambda x: x.isDirected(), g.edges())
        ) != len(g.edges())

def isDirected(g):
    return all(e.isDirected() for e in g.edges())

def isMultigraph(g):
    for v in g.vertices():
        count = []
        for ename in g.adjacent(v.name()):
            e = g.edge(ename)
            dest_ = e.dest()
            if dest_ in count:
                return True
            else:
                count.append(dest_)
    return False

def isUndirected(g):
    return all(not e.isDirected() for e in g.edges())

def isSimpleGraph(g):
    return not (isMultigraph(g) or anyHasSling(g))

def anyHasSling(g):
    return any(e.isSling() for e in g.edges())


# reachability and connectibility
def reachable(g, v1, v2):
    pass

def connected(g, v1, v2):
    pass

def stronglyConnected(g, v1, v2):
    pass

def connectedGraph(g):
    pass

def stronglyConnectedComponents(g):
    pass

def minimalSpanningTree(g):
    pass


# Dirac - if G is a (1) simple graph with n edges, (2) with 3 <= n ∈ N and
# the degree of (3) each vertice v of G d(v) >= n/2 then G has the attribute 
# Hamiltonian.
def isDirac(g):
    n = len(g.edges())
    return (n >= 3 and 
            isSimpleGraph(g) and 
            all(g.verticeDegree(v) >= (n / 2) for v in g.vertices())
            )


def generateDescription(g):
    calling = direction = "none"
    if isDirected(g):
        calling = direction = "directed"
    if isUndirected(g):
        calling = direction = "undirected"
    if isMixed(g):
        calling = direction = "mixed"
    if isQuiver(g):
        calling = "Quiver"
    if isMultigraph(g):
        calling = "MultiGraph"
    if isSimpleGraph(g):
        calling = "SimpleGraph"
    if calling == direction:
        return g.name() + ", " + direction
    return g.name() + ", " + calling + ", " + direction

