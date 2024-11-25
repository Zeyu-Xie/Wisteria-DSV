from graphviz import Digraph

dot = Digraph(comment='Preferences Tree')

dot.graph_attr['rankdir'] = 'TB'
dot.edge_attr['arrowhead'] = 'none'
dot.node_attr['shape'] = "box"

with dot.subgraph(name='cluster_0') as c_0:
    c_0.node('A', 'Location 🗺️', style='filled', fillcolor='darkgoldenrod1')
    c_0.node('A1', 'In Kista')
    c_0.node('A2', 'Close to Stations')
    c_0.node('A3', 'Ground Floor')
    c_0.node('A4', 'Park Surroundings')
    c_0.edge("A", "A1")
    c_0.edge("A", "A2")
    c_0.edge("A", "A3")
    c_0.edge("A", "A4")

with dot.subgraph(name='cluster_1') as c_1:
    c_1.node('B', 'Space 📏', style='filled', fillcolor='darkgoldenrod1')
    c_1.node('B1', 'Open Collaborative Area')
    c_1.node('B2', 'Modern Style')
    c_1.node('B3', 'Capacity for 50-60 ppl.')
    c_1.node('B4', '150-200 sqm.')
    c_1.edge("B", "B1")
    c_1.edge("B", "B2")
    c_1.edge("B", "B3")
    c_1.edge("B", "B4")

with dot.subgraph(name='cluster_2') as c_2:
    c_2.node('C', 'Facilities 🍳', style='filled', fillcolor='darkgoldenrod1')
    c_2.node('C1', 'Kitchen')
    c_2.node('C2', 'Fika Area')
    c_2.node('C3', 'Parking Lot')
    c_2.edge("C", "C1")
    c_2.edge("C", "C2")
    c_2.edge("C", "C3")

with dot.subgraph(name='cluster_3') as c_3:
    c_3.node('D', 'Rent 💰', style='filled', fillcolor='darkgoldenrod1')
    c_3.node('D1', '150,000-170,000 SEK')
    c_3.edge("D", "D1")

dot.render("../preferences_tree", format='png', cleanup=True)
dot.render("../preferences_tree", format='svg', cleanup=True)