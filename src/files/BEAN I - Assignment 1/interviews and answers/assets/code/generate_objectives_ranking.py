from graphviz import Digraph

dot = Digraph(comment='Priority Trees')

dot.graph_attr['rankdir'] = 'TB'
dot.node_attr['shape'] = 'none'

dot.node('A', '1. Location 🗺️ (In Kista)')
dot.node('B', '2. Location 🗺️ (Close to Stations)')
dot.node('C', '3. Space 📏 (Around 50-60 ppl.)')
dot.node('D', '4. Location 🗺️ (Ground Floor)')
dot.node('E', '5. Facility 🍳 (Parking Lot)')
dot.node('F', '6. Budget 💰 (no more than 150,000-170,000 SEK)')

dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")
dot.edge("E", "F")

dot.render("../objectives_ranking", format='png', cleanup=True)
dot.render("../objectives_ranking", format='svg', cleanup=True)