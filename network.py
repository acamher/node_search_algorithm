from classes import network as net
from classes import node as nd
from classes import leg as lg

# Creating Network

network = net.Network("Network_A")

node_1 = nd.Node(network, "A", -1, 1)
node_2 = nd.Node(network, "B", -1, -1)
node_3 = nd.Node(network, "C", 1, -1)
node_4 = nd.Node(network, 4, 2,2)

leg_1 = lg.Leg(node_1, node_2)
leg_2 = lg.Leg(node_2, node_3)
leg_3 = lg.Leg(node_1, node_3)
leg_4 = lg.Leg(node_1, node_4)
leg_5 = lg.Leg(node_4, node_2)

# Actions
network.printGraph()