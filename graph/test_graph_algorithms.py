#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import graph
from graph_parser import GraphParser
import graph_algorithms

class TestGraphAlgorithms(unittest.TestCase):

    def test_bellman_ford(self):
        print "Bellman Ford"
        name = "graph3"
        p = "/Users/sacry/dev/uni/s3/WS1314/GKA/graphs/"+name+".graph"
        gp = GraphParser(p, name)
        g = gp.createGraph()
        l = graph_algorithms.shortestBellman(g, "y", "u", "d")
        shortest_path_as_names = map(lambda x: x.name(), l)
        self.assertEqual(["y","s","x","u"], shortest_path_as_names)

    def test_dijkstra(self):
        print "Dijkstra"
        name = "graph3"
        p = "/Users/sacry/dev/uni/s3/WS1314/GKA/graphs/"+name+".graph"
        gp = GraphParser(p, name)
        g = gp.createGraph()
        l = graph_algorithms.shortestDijkstra(g, "y", "u", "d")
        shortest_path_as_names = map(lambda x: x.name(), l)
        self.assertEqual(["y","s","x","u"], shortest_path_as_names)

    def test_ford_fulkerson(self):
        pass
        '''
        name = "graph9"
        p = "/Users/sacry/dev/uni/s3/WS1314/GKA/graphs/"+name+".graph"
        gp = GraphParser(p, name)
        g = gp.createGraph()
        print g
        graph_algorithms.fordFulkerson(g, "Quelle", "Senke", "c")
        edgenames = g.getVertice("Senke").getEdges()
        edges = g.getEdgesByName(edgenames)
        weight = map(lambda x: x.getWeight("ff"), edges)
        print edges
        print sum(weight)
        '''
        
if __name__ == '__main__':
    unittest.main()


    