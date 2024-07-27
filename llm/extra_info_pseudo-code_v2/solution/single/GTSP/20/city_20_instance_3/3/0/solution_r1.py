import math
import random

# City coordinates indexed by city number
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Groups, each with list of city numbers
groups = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def generate_initial_tour():
    tour = [0]  # start at the depot
    used_groups = set()
    
    # Randomly choose one city from each group
    for group_id in sorted(groups.keys()):
        city = random.choice(groups[group_id])
        tour.append(city)
        used_groups.add(group_id)
        
    tour.append(0)  # end at the depot
    return tour

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate an initial tour and calculate its total cost
initial_tour = generate_initial_tour()
initial_tour_cost = total_tour_cost(initial_tour)

# Output the results
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {initial_tour_cost:.2f}")