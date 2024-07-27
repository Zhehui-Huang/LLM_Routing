import numpy as np

# City coordinates
cities = {
    0: (8, 11), 
    1: (40, 6), 
    2: (95, 33), 
    3: (80, 60), 
    4: (25, 18), 
    5: (67, 23), 
    6: (97, 32), 
    7: (25, 71), 
    8: (61, 16), 
    9: (27, 91), 
    10: (91, 46), 
    11: (40, 87), 
    12: (20, 97), 
    13: (61, 25), 
    14: (5, 59), 
    15: (62, 88), 
    16: (13, 43), 
    17: (61, 28), 
    18: (60, 63), 
    19: (93, 15)
}

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(cities)
visited = [False] * n
tour = [0]  # Start from the depot city (index 0)
visited[0] = True
current_city = 0

max_leg = 0.0
total_cost = 0.0

while len(tour) < n:
    nearest_city = None
    minimum_max_leg = float('inf')

    for next_city in range(n):
        if not visited[next_city]:
            # Calculate distance
            distance = euclidean_distance(cities[current_city], cities[next_city])
            # Update potential max leg
            potential_max_leg = max(max_leg, distance)
            if potential_max_leg < minimum_max_leg:
                minimum_max_leg = potential_max_leg
                nearest_city = next_city

    # Update route and metrics
    tour.append(nearest_city)
    visited[nearest_city] = True
    cost_to_nearest = euclidean_distance(cities[current_city], cities[nearest_city])
    total_cost += cost_to_nearest
    max_leg = max(max_leg, cost_to_nearest)
    current_city = nearest_city

# Finish the tour by going back to the depot
back_to_depot = euclidean_distance(cities[current_city], cities[0])
total_cost += back_to_depot
max_leg = max(max_leg, back_to_dequians)
tour.append(0)  # Append the return to the depot

# Outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_leg:.2f}")