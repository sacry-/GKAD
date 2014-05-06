

# vertice_object = Vertice(String, dict={Any : Any})
class Vertice():

    # Creation
    def __init__(self, name):
        self.name_ = name
        self.weight_ = {}
        self.edges_ = set([])

    def __repr__(self):
        return "v{" + str(self.name) + "}"

    # Mutators
    def addEdge(self, ename):
        self.edges_.add(ename)

    def removeEdge(self, ename):
        if ename in self.edges_:
            self.edges_.remove(ename)

    def edges(self):
        return self.edges_

    def updateWeight(self, key, value):
        if key in self.weight_:
            self.weight_[key] += value
        else:
            self.weight_[key] = value

    # Selectors
    def weight(self, cmp_, value=None):
        if value != None:
            self.weight_[cmp_] = value
        if cmp_ in self.weight_:
            return self.weight_[cmp_]
        return None

    def weightMap(self):
        return self.weight_
            
    def name(self):
        return self.name_

    def resetWeight(self):
        self.weight_ = {}

    # Built in
    def __eq__(self, other):
        if isinstance(other, Vertice):
            return self.name() == other.name()
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.name())

