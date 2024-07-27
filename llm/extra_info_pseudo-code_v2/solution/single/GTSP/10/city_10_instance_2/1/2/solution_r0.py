import math
import itertools

# City positions
city_positions = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# City groups
city_groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

def calculate_distance(city1, city2):
    x1, y1 = city_positions[city1]
    x2, y2 = city_positions[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Iterate over all combinations of selecting one city from each group
    for combination in itertools.product(*city_groups.values()):
        # ensure each selected city is unique to avoid revisiting
        if len(set(combination)) == len(city_groups):
            # Create potential tour starting and ending at the depot
            current_tour = [0] + list(combination) + [0]
            
            # Calculate the cost of the current tour
            current_cost = sum(calculate_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
            
            # Check if this tour is better than the best found so far
            if current_cost < best_cost:
                best_tour = current_tour
                best_cost = current_cost
                
    return best_tour, best_cost

# Get the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()

print("Tour:", optimal_tour)
print("Total travel cost: {:.2f}".format(optimal_cost))