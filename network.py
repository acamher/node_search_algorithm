import json
from classes import network as net
from classes import node as nd
from classes import leg as lg

# Creating Network
f = open('network/B.json')
data = json.load(f)

network = net.Network(data['name'])
node_list = {}
leg_list = {}

for node in data['nodes']:
    node_list[node['id']] = nd.Node(network, node['id'], node['x'], node['y'])

n = 0
for leg in data['legs']:
    leg_list[str(n)] = lg.Leg(node_list[str(leg['start'])], node_list[str(leg['finish'])])
    n += 1

# Actions
network.printGraph()