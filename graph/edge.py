


# edge_object = Edge(String, Vertice, Vertice, Bool=True, dict={Any : Any})
class Edge():

    def __init__(self, name, src, dest, isdirected=True, weight={}):
        self.name_ = name
        self.isdirected = isdirected
        self.src_ = src
        self.dest_ = dest
        self.weight_ = weight

    def __repr__(self):
        return (
            self.src_ + 
            "  " if self.isDirected() else "  <" + 
            "--(" + str(self.name_) + ", =" + str(self.weight_) + 
            ")--> " + self.dest_)

    # Functions
    def inBetween(self, v1, v2):
        same_source = self.src_ == v1 and self.dest_ == v2
        if self.isdirected:
            return same_source
        not_same = self.dest_ == v1 and self.src_ == v2
        return same_source or not_same

    def isVerticeSrc(self, vertice):
        same = self.src_ == vertice
        if self.isdirected:
            return same
        return same or self.dest_ == vertice

    def isVerticeDest(self, vertice):
        same = self.dest_ == vertice
        if self.isdirected:
            return same
        return same or self.src_ == vertice

    def destBySrc(self, vertice):
        if self.src_ == vertice:
            return self.dest_
        if not self.isdirected and self.dest_ == vertice:
            return self.src_
        return None

    def srcByDest(self, vertice):
        if self.dest_ == vertice:
            return self.src_
        if not self.isdirected and self.src_ == vertice:
            return self.dest_
        return None

    # Weight Mutators
    def updateWeight(self, key, value):
        if key in self.weight_:
            self.weight_[key] += value
        else:
            self.setWeight(key, value)

    def resetWeight(self):
        self.weight_ = {}

    # Selectors
    def isSling(self):
        return self.src_ == self.dest_

    def isDirected(self):
        return self.isdirected

    def srcDest(self):
        return (self.src_, self.dest_)

    def src(self):
        return self.src_

    def dest(self):
        return self.dest_

    def name(self):
        return self.name_

    def weightMap(self):
        return self.weight_

    def weight(self, cmp_, value=None):
        if value != None:
            self.weight_[cmp_] = value
        if cmp_ in self.weight_:
            return self.weight_[cmp_]
        return None

    # Built in
    def __eq__(self, other):
        if isinstance(other, Edge):
            is_in = self.inBetween(other.src(), other.dest())
            return (self.name_ == other.name() and is_in)
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.name_)

    