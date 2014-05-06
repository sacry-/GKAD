from graph import Graph
from vertice import Vertice
from edge import Edge
import re

# gp = GraphParser(String, String)
# g = gp.createGraph(pattern="")
class GraphParser():

    def __init__(self, apath, name="xxx"):
        self.path = apath
        self.g = Graph(name)
        self.tokens = []

    def __repr__(self):
        return str(self.__class__.__name__) + "(Path=" + self.path + ", GraphName=" + self.g.name() + ")"

    def getGraph(self):
        return self.g

    def createGraph(self, pattern=","):
        self.__split__(pattern)
        self.__interpret__()
        return self.g

    def overwriteGraph(self, apath, pattern=",", name="xxx"):
        self.path = apath
        self.g = Graph(name)
        self.tokens = []
        return self.createGraph(pattern)

    def __split__(self, pattern):
        for line in open(self.path, 'r'):
            token = re.split(pattern, line.strip())
            if token:
                self.tokens.append(token)

    def __interpret__(self):
        direction = str(self.tokens[0])

        # Klauck - v1,v2,w
        if re.search("#(un)?gerichtet", direction):
            self.__verticeVerticeWeightParse__(self.__direction__())
            return

        # Mine - v:v1{a:b,c:d},v2{a:b,c:d},e:e1{a:b,c:d}..en{a:b,c:d}
        if re.search("(un)?directed", direction):
            self.__undirectedDirectedParse__(self.__direction__())
            return 

        if re.search("mixed", direction):
            self.__mixedParse__()
            return

        raise Error('''Did not match any Regexp! Must be: "v1,v2,w" or 
            "v:v1{a:b,c:d},v2{a:b,c:d},e:e1{a:b,c:d}..en{a:b,c:d}". See given examples...''')

    def __direction__(self):
        dire = str(self.tokens[0][0])
        if re.match("(#gerichtet|directed)", dire):
            return True
        if re.match("(#ungerichtet|undirected)", dire):
            return False

    def __undirectedDirectedParse__(self, dire):
        vertice_regex = re.compile("(\{|\}| )")
        edge_regex = ""
        for idx, sublist in enumerate(self.tokens[1:]):

            src_name = str(sublist[0])
            dest_name = str(sublist[1])
            if vertice_regex.search(src_name):
                src_tokens = re.split("(\{|\}| )", src_name)

            if vertice_regex.search(dest_name):
                dest_tokens = re.split("(\{|\}| )", dest_name)

            for token in sublist[2:]:
                ename = str(token[0:2])
                attrs = token[3:len(token)-1].split(" ")
                attr_dict = {}
                for kv in attrs:
                    key, val = kv.split(":")
                    try:
                        attr_dict[str(key)] = int(val)
                    except ValueError:
                        attr_dict[str(key)] = str(val)
                self.g.addEdge(ename, src_name, dest_name, dire, attr_dict)

    def __mixedParse__(self):
        for idx, sublist in enumerate(self.tokens[1:]):
            src = self.sublist[1]
            dest = self.sublist[2]
            src_tokens = re.split("(\{|\}| )", src)
            dest_tokens = re.split("(\{|\}| )", dest)
            for token in sublist[3:]:
                edge = re.split("(\{|\}| )", token)
                #process edge

    def __verticeVerticeWeightParse__(self, dire):
        for idx, sublist in enumerate(self.tokens[1:]):
            src = sublist[0]
            dest = sublist[1]
            w = int(sublist[2])
            ename = "e" + str(idx)
            self.g.addEdge(ename, src, dest, dire, {"d" : w})


class GraphSaver():

    def __init__(self, g, apath, filename):
        self.g = g
        self.path = apath
        self.filename = filename
        self.__save__()

    def __save__(self):
        pass

        







