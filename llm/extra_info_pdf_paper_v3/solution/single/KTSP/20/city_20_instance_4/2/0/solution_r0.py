import random
import math
from itertools import permutations

# Cities position
positions = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((positions[city1][0] - positions[city2][0]) ** 2 + (positions[city1][1] - positions[city2][1]) ** 2)

def calculate_total_distance(tour):
    """ Calculate the total distance of the tour path. """
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += euclidean_distance(tour[i], tour[i+1])
    total_dist += euclidean_distance(tour[-1], tour[0]) # Return to the initial city (make it a round trip)
    return total_dist

def find_shortest_tour():
    num_cities = 20
    k = 16
    best_tour = None
    shortest_distance = float('inf')
    
    for _ in range(100):  # Multi-start approach
        # Randomly select k-1 cities plus the depot city (which is city 0)
        cities_to_visit = random.sample(range(1, num_cities), k - 1)
        cities_to_visit.insert(0, 0)  # Include the depot as the starting city
        
        # Check all permutations of these k cities
        for perm in permutations(cities_to_visit):
            tour_distance = calculate_total_distance(perm)
            
            # Update the best tour found
            if tour_distance < shortest_distance:
                shortest_distance = tour_distance
                best_tour = perm
    
    return best_tour, shortest_distance

# Find the optimal tour using the provided method.
optimal_tour, optimal_cost = find_shortest_tour()

# Output results
print("Tour: {}".format(list(optimal_tour) + [optimal_tour[0]]))
print("Total travel cost: {:.2f}".format(optimal_cost))