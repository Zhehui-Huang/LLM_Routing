import numpy as np
from math import sqrt
import random

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def initialize_tours(cities, num_robots):
    # Sort cities based on the distance from the depot (city 0), excluding the depot itself
    city_distances = [(i, euclidean_distance(cities[0], cities[i])) for i in cities if i != 0]
    city_distances.sort(key=lambda x: x[1])
    
    tours = [[] for _ in range(num_robots)]
    # Assign each city to a tour in a round-robin fashion
    for index, (city, _) in enumerate(city_distances):
        tours[index % num_robots].append(city)
    
    # Add depot at start and end of each tour
    for tour in tours:
        tour.insert(0, 0)
        tour.append(0)
    
    return tours

def shake(tours, k):
    for _ in range(k):
        # Choose a random tour to remove a city from
        from_tour = random.choice(tours)
        if len(from_tour) > 2:  # Make sure it has cities besides the depot start and end
            city_to_move = random.choice(from_tour[1:-1])
            from_tour.remove(city_to_move)
            
            # Choose a random tour to add the city to, ensuring it's a different tour
            to_tour = random.choice(tours)
            if to_tour != from_tour:
                insert_position = random.randint(1, len(to_tour)-1)
                to_tour.insert(insert_position, city_to_move)

def apply_local_search(tour, cities):
    # Simple local search using 2-opt
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                if tour[i] == 0 or tour[j] == 0:
                    continue
                # Swap edges and check if better
                new_tour = tour[:]
                new_tour[i:j] = reversed(tour[i:j])
                if calculate_total_cost(new_tour, cities) < calculate_total_cost(tour, cities):
                    tour = new_tour
                    improved = True
    return tour

# Initialize tours
tours = initialize_tours(cities, num_robots)

# Apply GVNS
lmax, kmax, tmax = 5, 10, 100  # Example parameters
iter_count = 0

while iter_count < tmax:
    k = 1
    while k < kmax:
        old_tours = [tour[:] for tour in tours]
        shake(tours, k)
        new_tours = [apply_local_search(tour, cities) for tour in tours]
        
        if all(calculate_total_cost(new_tour, cities) <= calculate_total_cost(old_tour, cities) for new_tour, old_tour in zip(new_tours, old_tours)):
            tours = new_tours
            k = 1  # Improvement found, reset k
        else:
            k += 1
    
    iter_count += 1

# Calculating the results
total_costs = [calculate_total_cost(tour, cities) for tour in tours]
max_cost = max(total_costs)

# Output the results
for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {total_costs[idx]}")

print(f"Maximum Travel Cost: {max_cost}")