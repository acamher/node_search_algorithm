class Node:
    def __init__(self, network, id, coord_x, coord_y):
        network.nodes.append(self)
        self.id = id
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.connected_legs = []
    
    def print_info(self, option):
        match option:
            case "normal":
                print(f"From {self.node_a.id} to {self.node_b.id}. [Distance = {self.distance} m]")
            
            case "legs":
                print(f"Legs connected to {self.id} are: ({self.connected_legs})")