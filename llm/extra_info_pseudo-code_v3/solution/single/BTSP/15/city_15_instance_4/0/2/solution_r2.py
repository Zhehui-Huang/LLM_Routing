import numpy as np
from itertools import permutations

def calculate_distance(coord1, coord2):
    """ Calculate Euclidean distance between two points """
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def find_feasible_tour(coords):
    num_cities = len(coords)
    edges = []
    
    # Create all edges with their distances
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = calculate_distance(coords[i], coords[j])
            edges.append((distance, i, j))
    
    # Sort edges by distance
    edges.sort()
    
    # Try to form a Hamiltonian cycle starting from the shortest edge
    for max_edge, start, end in edges:
        # Create a path attempt starting with this edge
        tour = [start, end]
        used_edges = {(min(start, end), max(start, end))}
        max_distance = max_edge
        
        # Try to extend this path to a Hamiltonian cycle
        while len(tour) < num_cities:
            extended = False
            for distance, i, j in edges:
                if distance > max_distance:
                    max_distance = distance
                if i in tour and j in tour:
                    continue
                if i in tour and j not in tour:
                    tour.append(j)
                    used_edges.add((min(i, j), max(i, j)))
                    extended = True
                    break
                elif j in tour and i not in tour:
                    tour.append(i)
                    used_path.add((min(i, j), max(i, j)))
                    extended = True
                    break
            if not extended:
                break
        
        if len(tour) == num_cities:
            tour.append(tour[0])  # Close the cycle by returning to the first city
            total_distance = sum(calculate_distance(coords[tour[i]], coords[tour[i+1]]) for i in range(len(tour)-1))
            return tour, total_distance, max_distance
    
    return [], 0, 0  # No tour found

coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

tour, total_cost, max_distance = find_feasible_tour(coords)
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")