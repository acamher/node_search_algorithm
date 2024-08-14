import matplotlib.pyplot as plt

class Network:
    def __init__(self, name):
        self.name = name
        self.nodes = []
    
    def __str__(self):
        return f"{self.name}({self.nodes})"
    
    def printGraph(self):
        nodes_x = []
        nodes_y = []

        for node in self.nodes:
            nodes_x.append(node.coord_x)
            nodes_y.append(node.coord_y)
            for leg in node.connected_legs:
                plt.plot([leg.node_a.coord_x, leg.node_b.coord_x], [leg.node_a.coord_y, leg.node_b.coord_y], color='black', zorder=1)
        
        plt.scatter(nodes_x,nodes_y, zorder=2)
        plt.show()