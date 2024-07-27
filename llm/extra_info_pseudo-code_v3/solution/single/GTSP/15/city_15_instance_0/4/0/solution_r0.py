import itertools
import math

# Coordinates of the cities including the depot
city_coords = {
    0: (9, 93),  # Depot city
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Groups of cities
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

def euclidean_distance(city1, city2):
    """ Calculates Euclidean distance between two cities. """
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_tour_cost(tour):
    """ Calculates the total cost of a given tour. """
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_shortest_tour():
    # Assemble all possible selections of cities, one from each group
    city_group_options = list(itertools.product(*groups.values()))
    
    best_tour = None
    min_cost = float('inf')
    
    # Evaluate each possible selection
    for cities in city_group_options:
        all_tours = itertools.permutations(cities)
        for tour in all_tours:
            complete_tour = [0] + list(tour) + [0]  # start and end at the depot
            cost = calculate_tour_cost(complete_tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = complete_tour
                
    return best_tour, min_cost

# Calculate the shortest possible tour
tour, total_cost = find_shortest_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")