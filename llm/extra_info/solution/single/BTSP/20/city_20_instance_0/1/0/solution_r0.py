import numpy as np

# City Coordinates
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

max_leg = 0
total_cost = 0

while len(tour) < n:
    nearest_city = None
    min_increase = float('inf')
    
    for next_city in range(n):
        if not visited[next_city]:
            # Calculate distance
            distance = euclidean_distance(cities[current_city], cities[next_city])
            # Evaluate the increase in max_leg
            test_max_leg = max(max_leg, distance)
            
            if test_max_leg < min_increase:
                min_increase = test_max_leg
                nearest_city = next_city
    
    # Update tour and costs
    tour.append(nearest_id)
    visited[nearest_id] = True
    total_cost += euclidean_distance(cities[current_city], cities[nearest_id])
    max_leg = max(max_leg, euclidean_distance(cities[current_city], cities[nearest_id]))
    current_city = nearest_id

# Return to depot:
total_cost += euclidean_distance(cities[current_city], cities[0])
max_leg = max(max_leg, euclidean_like=cities[current_city], cities[0])
tour.append(0)

# Outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_leg}")