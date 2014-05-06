#!/usr/bin/python
# -*- coding: utf-8 -*-
from vertice import Vertice
from edge import Edge
from graph_module import generateDescription

# graph_object = Graph(String, String="Description", dict={String : Edge}, dict={String : Vertice})
class Graph():

    # Creation
    def __init__(self, name):
        self.name_ = name
        self.description_ = "None"
        self.edges_ = {}
        self.vertices_ = {}

    def nullgraph(self):
        return (not self.vertices_) and (not self.edges_)

    def empty(self):
        return not self.edges_

    # Removal
    def removeEdges(self, enames):
        for ename in enames:
            self.removeEdge(ename)

    def removeVertices(self, vnames):
        for vname in vnames:
            self.removeVertice(vname)

    def removeEdge(self, ename):
        if ename in self.edges_:
            for v in self.vertices_.values():
                v.removeEdge(ename)
            del self.edges_[ename]
            return True
        return False

    def removeVertice(self, vname):
        if vname in self.vertices_:
            for ename, e in self.edges_.items():
                if e.src() == vname or e.dest() == vname:
                    self.removeEdge(ename)
            del self.vertices_[vname]
            return True
        return False

    # Creation 
    def addVertices(self, vnames):
        for vname in vnames:
            self.addVertice(vname)

    def addEdge(self, ename, src_name, dest_name, isdirected=True, weight={}):
        src_name = self.addVertice(src_name)
        dest_name = self.addVertice(dest_name)
        self.vertice(src_name).addEdge(ename)
        self.vertice(dest_name).addEdge(ename)
        self.edges_[ename] = Edge(ename, src_name, dest_name, isdirected, weight)
        return ename

    def addVertice(self, vname):
        if not vname in self.vertices_ and isinstance(vname, basestring):
            self.vertices_[vname] = Vertice(vname)
        return vname

    # Functions
    def neighbours(self, vname):
        adja = set([])
        for ename in self.incident(vname):
            e = self.edge(ename)
            if e.isVerticeSrc(vname):
                adja.add(e.destBySrc(vname))
        if not self.hasSling(vname) and vname in adja:
            adja.remove(vname)
        return adja # -> Set(Vertice.name)

    def adjacent(self, vname):
        adja = set([])
        for e in self.incident(vname):
            if self.edge(e).isVerticeSrc(vname):
                adja.add(e)
        return adja # -> Set(Edge.name)

    def incident(self, vname):
        return self.vertice(vname).edges() # -> Set(Edge.name)

    def hasSling(self, vname):
        if not vname in self.vertices_:
            return False
        return any(self.edge(ename).isSling() for ename in self.incident(vname))

    # Selectors Graph
    def name(self, graph_name=None):
        if graph_name != None:
            self.name_ = graph_name
        else:
            return self.name_

    # Selectors Graph Components
    def verticeDegree(self, vname):
        return len(self.incident(vname))

    def vertice(self, vname):
        if vname in self.vertices_:
            return self.vertices_[vname]
        return None

    def edge(self, ename):
        if ename in self.edges_:
            return self.edges_[ename]
        return None

    def edges(self):
        return self.edges_.values()

    def vertices(self):
        return self.vertices_.values()

    def edgesByName(self, enames):
        return [v for ename, v in self.edges_.items() if ename in enames]

    def verticesByName(self, names):
        return [v for vname, v in self.vertices_.items() if vname in vnames] 

    # Delegation
    def srcDest(self, ename):
        return map(self.vertice, self.edge(ename).srcDest())

    # edgeSrcDest
    def edgeSrcDest(self, src_name, dest_name):
        for ename in self.incident(src_name):
            e = self.edge(ename)
            if e.inBetween(src_name, dest_name):
                return e
        return None

    # edgeSrcDestList
    def edgeSrcDestList(self, src_name, dest_name):
        result = []
        for ename in self.incident(src_name):
            e = self.edge(ename)
            if e.inBetween(src_name, dest_name):
                result.append(e)
        return result

    def weightBetween(self, src_name, dest_name, cmp_):
        return self.edgeSrcDest(src_name, dest_name).weight(cmp_)

    def __eq__(self, other):
        if isinstance(other, Graph):
            return self.name_ == other.name()
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.name_)

    # Sorted Alphabetical Order by Vertice.name
    # srcVertice.name, srcVertice.weightMap 
    #       - Edge.name, Edge.weightMap -> 
    #           destVertice.name, destVertice.weightMap
    def __repr__(self):

        indentation = "\n\t"

        def nameMap(comp):
            return "(" + comp.name() + ", " + str(comp.weightMap()) + ")"

        def edge_s(edge):
            direction = "  " if edge.isDirected() else "  <"
            return direction + "--" + nameMap(edge) + "-->  "

        # Extracting Rows from components
        rows = []
        book_keeping = []
        for vname in self.vertices_:
            for ename in self.adjacent(vname):
                e = self.edge(ename)
                src_, dest_ = self.srcDest(ename)
                if not (e, src_, dest_) in book_keeping:
                    book_keeping.append((e, src_, dest_))
                    row = (vname, nameMap(src_) + edge_s(e) + nameMap(dest_))
                    rows.append(row)

        # Sorting, Concatenation       
        sorted_by_name = self.__unique__(sorted(rows, key=lambda vname: vname[0]))
        reduced_string = reduce(lambda accu, row: accu + row[1] + indentation, sorted_by_name, "")

        paranthesis = indentation + "<(" + indentation
        return "Graph(" + self.description_ + ")" + paranthesis + reduced_string + ")>"
    
    def __unique__(self, seq):
        result = []
        for elem in seq:
            if elem not in result:
                result.append(elem)
        return result

    def updateDescription(self):
        self.description_ = generateDescription(self)

    def description(self):
        return self.description_






