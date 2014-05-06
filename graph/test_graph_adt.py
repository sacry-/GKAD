#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from graph import Graph
from graph_parser import GraphParser
import graph_module
from os import getcwd

class TestGraph(unittest.TestCase):

    # Workflow of a Graph
    def test_graph_integration(self):
        print "Graph Creation"
        g = Graph("Euclid")
        self.assertEqual("Euclid", g.name())
        self.assertTrue(g.empty())
        v1,v2,v3,v4,v5,v6,v7,v8 = [g.addVertice("v"+str(x)) for x in xrange(1, 8 + 1)]
        e1 = g.addEdge("e1", v1, v2, True, weight={"d" : 1})
        e2 = g.addEdge("e2", v1, v3, True, weight={"d" : 10})
        e3 = g.addEdge("e3", v1, v4, True, weight={"d" : 10})
        e4 = g.addEdge("e4", v2, v8, True, weight={"d" : 1})
        e5 = g.addEdge("e5", v3, v5, True, weight={"d" : 10})
        e6 = g.addEdge("e6", v4, v6, True, weight={"d" : 10})
        e7 = g.addEdge("e7", v5, v8, True, weight={"d" : -10})
        e8 = g.addEdge("e8", v6, v7, True, weight={"d" : 10})
        e9 = g.addEdge("e9", v7, v8, True, weight={"d" : -20})
        e10 = g.addEdge("e10", v7, v1, False, weight={"d" : 50})
        # Adding only edges shall result in a populated Graph with edges + vertices
        self.assertEqual(set([v2,v3,v4,v7]), g.neighbours(v1))
        self.assertEqual(set([e9, e10]), g.adjacent(v7))
        # removing an edge results in removing the whole history
        g.removeEdge(e10)
        self.assertEqual(set([v2,v3,v4]), g.neighbours(v1))
        self.assertEqual(set([e9]), g.adjacent(v7))
        self.assertEqual(set([v8]), g.neighbours(v7))
        v9 = g.addVertice("v9")
        e11 = g.addEdge("e11", v1, v9, True, weight={"d" : 50})
        # v9 should be removed from g and all edges e dependant on v9
        g.removeVertice(v9)
        self.assertEqual(None, g.edge("e11"))
        self.assertEqual(set([v2,v3,v4]), g.neighbours(v1))
        self.assertEqual(set([e9]), g.adjacent(v7))
        self.assertEqual(set([v8]), g.neighbours(v7))
        # Simple Graph
        self.assertTrue(graph_module.isSimpleGraph(g))
        e13 = g.addEdge("e13", v2, v2, True, weight={"d" : 10}) # Added a Sling 
        self.assertTrue(not graph_module.isSimpleGraph(g))
        # Multigraph
        self.assertTrue(not graph_module.isMultigraph(g))
        e12 = g.addEdge("e12", v5, v8, True, weight={"d" : 5}) # Add another edge bewteen v5 -> v8
        self.assertTrue(graph_module.isMultigraph(g))
        g.updateDescription()
        # Removing all Vertices is equal to emptyness
        g.removeEdges([e1,e2,e3,e4,e5,e6,e7,e8,e9,e12,e13])
        self.assertTrue(g.empty())
        self.assertTrue(not g.nullgraph())
        g.removeVertices([v1,v2,v3,v4,v5,v6,v7,v8])
        self.assertTrue(g.nullgraph())
        self.assertTrue(g.empty())
        self.assertEqual([], g.edges())
        self.assertEqual([], g.vertices())
        # Checked that g is empty, these should behave differently
        self.assertFalse(graph_module.isDirac(g))
        self.assertFalse(graph_module.isMultigraph(g))
        self.assertTrue(graph_module.isSimpleGraph(g)) # NullGraph is always simple - it doesn't break any rules

    def test_graph_parser(self):
        print "Graph Parsing"
        name = "graph1"
        p = getcwd() + "/graphs/old/" + name + ".graph"
        gp = GraphParser(p, name)
        g = gp.createGraph()
        self.assertTrue(not g.empty())
        actual_neighbours = set(["Neumünster", "Bremen", "Berlin", "Hannover","Lüneburg","Lübeck"])
        expected_neighbours = g.neighbours("Hamburg")
        self.assertEqual(actual_neighbours, expected_neighbours)
        hamburg = g.vertice("Hamburg")
        self.assertTrue("Hamburg", hamburg.name())
        print g

    # Certain typical Edge Cases
    def test_edge_cases(self):
        pass

    def test_vertice(self):
        pass

    def test_edge(self):
        pass



if __name__ == '__main__':
    unittest.main()




