import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        pass
    def creaGrafo(self):
        self.nodes = DAO.getChrom()
        self.edges = DAO.getArchi()
        self.grafo = nx.DiGraph()
        self.grafo.add_nodes_from(self.nodes)
        self.grafo.add_edges_from(self.edges)
        self.pesi = DAO.getPesi()
        for e in self.grafo.edges:
            sum = 0
            for p in self.pesi:
                if (e[0]==p[0] and e[1]==p[1]):
                    sum+=p[2]
            self.grafo[e[0]][e[1]]['weight'] = sum

    def stampa(self):
        return (f"Numero nodi: {len(self.grafo.nodes)}, numero archi: {len(self.grafo.edges)}\n"
                f"Informazione sul peso degli archi: min = {self.min()}, max = {self.max()}")

    def min(self):
        min = 1000
        for e in self.grafo.edges:
            if self.grafo[e[0]][e[1]]["weight"]<min:
                min = self.grafo[e[0]][e[1]]["weight"]
        return min

    def max(self):
        max = -1000
        for e in self.grafo.edges:
            if self.grafo[e[0]][e[1]]["weight"]>max:
                max = self.grafo[e[0]][e[1]]["weight"]
        return max

    def contaArchi(self,soglia):
        cmag = 0
        for e in self.grafo.edges:
            if self.grafo[e[0]][e[1]]["weight"] > soglia:
                cmag +=1
        cmin = 0
        for e in self.grafo.edges:
            if self.grafo[e[0]][e[1]]["weight"] < soglia:
                cmin +=1
        return (cmag,cmin)
