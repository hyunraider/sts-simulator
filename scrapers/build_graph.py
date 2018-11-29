import json
import networkx as nx
import matplotlib.pyplot as plt

with open('../data/runs/silent/1537904792.run') as f:
    obj = json.load(f)

graph = nx.DiGraph()

for card in obj["master_deck"]:
    card_name = card.split('+')[0]
    if card_name not in graph.nodes:
        graph.add_node(card_name)
        graph.nodes[card_name]["count"] = 0
    graph.nodes[card_name]["count"] += 1

for node in graph.nodes:
    for node2 in graph.nodes:
        if node != node2:
            graph.add_edge(node, node2, weight=(graph.nodes[node2]["count"]*1.0/graph.nodes[node]["count"]))

labels = nx.get_edge_attributes(graph, 'weight')
print labels
exit()
plt.figure()
count=nx.get_node_attributes(graph,'count')
nx.draw(graph, labels=count)
labels = nx.get_edge_attributes(graph, 'weight')
#nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.tight_layout()
plt.show()
