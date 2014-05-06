from graph import Graph
from vertice import Vertice
from edge import Edge
import sys


''' 4611686018427387903 '''
infinity = sys.maxint / 2 

def shortestBellman(g, source, target, cmp_):
    
    bellmanFord(g, source, cmp_)
    source = g.vertice(source)
    target = g.vertice(target)

    def inner_shortest(target, accu):
        if target.weight(cmp_) == infinity:
            return []
        pred = g.vertice(target.weight("pred"))
        if pred == None:
            accu.insert(0, source)
            return accu
        accu.insert(0, target)
        return inner_shortest(pred, accu)

    return inner_shortest(target, [])

def initialize(g, source):
    for v in g.vertices():
        v.weight("d", infinity)
        v.weight("prev", None)
    g.vertice(source).weight("d", 0)

def relax(u, v, w):
    if u.weight("d") + w < v.weight("d"):
        v.weight("d", u.weight("d") + w)
        v.weight("pred", u.name())

def bellmanFord(g, source, cmp_):
    # Step 1: initialize graph
    initialize(g, source)

    # Step 2: relax edges repeatedly
    for _ in range(0, len(g.vertices())):
        for e in g.edges():
            u, v = g.srcDest(e.name())
            w = e.weight(cmp_)
            relax(u, v, w)

   # Step 3: check for negative-weight cycles
    for e in g.edges():
        u, v = g.srcDest(e.name())
        w = e.weight(cmp_)
        if u.weight("d") + w < v.weight("d"):
           print "Graph contains a negative-weight cycle"
           return None


def shortestDijkstra(g, source, target, cmp_):
    dijkstra(g, source, cmp_)
    S = []
    u = g.vertice(target)
    while u.weight("prev") != None:
        S.insert(0, u)
        u = g.vertice(u.weight("prev"))
    S.insert(0, g.vertice(source))
    return S


def dijkstra(g, source, cmp_):
    initialize(g, source)

    Q = g.vertices()
    while Q:
        u = min(Q, key=lambda x: x.weight("d"))
        Q.remove(u)
        if u.weight("d") == infinity:
            break
        for vname in g.neighbours(u.name()):
            v = g.vertice(vname)
            w = g.weightBetween(u.name(), vname, cmp_)
            alt = u.weight("d") + w
            if alt < v.weight("d"):
                v.weight("d", alt)
                v.weight("prev", u.name())
                Q.remove(v)
                Q.append(v)


def fordFulkerson(g, s, t, cmp_):

    raise Error("Not Implemented!")
    
    def inner_ford(s_, t_,):
        edges = g.edges()
        for edge in edges:
            edge.weight("c", 10)
            edge.weight("ff", 0)
            edge.weight("fb", 0)
        p = find(g, s_, t_, [])
        while p:
            cf = min(p, key=lambda x: x.weight(cmp_)).weight(cmp_)
            for edge in p:
                edge.updateWeight("ff", cf)
                edge.updateWeight("fb", -cf)
            p = find(g, s_, t_, [])


    def find(g, s, t, p):
        return p

    inner_ford(s, t)

