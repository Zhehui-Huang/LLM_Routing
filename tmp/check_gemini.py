import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
G = nx.Graph()
G.add_nodes_from(['Place 1', 'Place 2', 'Place 3', 'Place 4', 'Place 5'])
G.add_weighted_edges_from([
    ('Place 1', 'Place 2', 5),
    ('Place 1', 'Place 3', 5),
    ('Place 1', 'Place 4', 6),
    ('Place 1', 'Place 5', 4),
    ('Place 2', 'Place 3', 2),
    ('Place 2', 'Place 4', 1),
    ('Place 2', 'Place 5', 2),
    ('Place 3', 'Place 4', 1),
    ('Place 3', 'Place 5', 4),
    ('Place 4', 'Place 5', 4)
])

# Find the shortest Hamiltonian cycle
tour = nx.find_hamiltonian_cycle(G)

# Calculate the cost of the tour
cost = nx.Graph.size(G, weight='weight')

# Print the results
print(f'Tour: {tour}')
print(f'Cost: {cost}')

# Visualize the tour
pos = {
    'Place 1': (9, 4),
    'Place 2': (4, 6),
    'Place 3': (4, 4),
    'Place 4': (3, 4),
    'Place 5': (4, 8)
}

nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue')
nx.draw_networkx_edges(G, pos, edgelist=tour, arrows=True, arrowstyle='->')
plt.show()