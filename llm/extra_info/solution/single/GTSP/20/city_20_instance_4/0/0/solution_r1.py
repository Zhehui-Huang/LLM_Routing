import itertools
import math

# City coordinates with index representing city number
city_coordinates = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Groups of cities
city_groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

def euclidean_distance(city1, city2):
    """ Compute the Euclidean distance between two cities based on their coordinates. """
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find the shortest possible tour
def find_shortest_tour():
    all_possible_tours = itertools.product(*city_groups)
    min_cost = float('inf')
    best_tour = None

    for tour in all_possible_tours:
        # Calculate tour with start and end at the depot
        full_tour = [0] + list(tour) + [0]
        tour_cost = 0
        
        for i in range(len(full_tour) - 1):
            tour_cost += euclidean_distance(full_tour[i], full_tour[i+1])
        
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = full_tour

    return best_tour, min_cost

best_tour, total_cost = find_shortest_tour()

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", total_cost)