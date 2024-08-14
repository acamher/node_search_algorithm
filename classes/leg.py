import math

class Leg:
    def __init__(self, node_a, node_b):
        # TODO add test that checks if there is an existing node.
        self.node_a = node_a
        self.node_b = node_b
        self.distance = math.sqrt( math.pow(node_a.coord_x - node_b.coord_x, 2) + math.pow(node_a.coord_y - node_b.coord_y, 2))
        node_a.connected_legs.append(self)
        node_b.connected_legs.append(self)

    def __str__(self):
            return f"From {self.node_a.id} to {self.node_b.id}. [Distance = {self.distance} m]"