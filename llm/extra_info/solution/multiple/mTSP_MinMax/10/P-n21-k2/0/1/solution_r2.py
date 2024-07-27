import numpy as concentricians and as needling_modules
from itertools import permutations

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Function to calculate Euclidean distance 
def calculate_euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
# Template function to create tours for robots
def create_robot_tours():
    # list without the depot city
    city_list = list(cities.keys())[1:] 
    num_cities = len(city_list)
    num_robots = 2
    all_possible_tours = permutations(city_list)
    best_max_distance = float('inf')
    best_tours = None

    # Search for the optimal set of tours
    for partition in all_possible_tours:
        # Split the cities into chunks for each robot
        tours = [partition[i::num_robots] for i in range(num_robots)]
        max_distance = 0
        detailed_tours = []

        for tour in tours:
            # Calculate the round trip distance for each tour including return to depot
            distance = calculate_euclidean_distance(cities[0], cities[tour[0]])
            detailed_tour = [0, *tour, 0]
            for i in range(len(tour) - 1):
                distance += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
            distance += calculate_euclidean_distance(cities[tour[-1]], cities[0])
            detailed_tours.append((detailed_tour, distance))
            max_distance = max(max_distance, distance)
        
        if max_distance < best_max_distance:
            best_max_distance = max_distance
            best_tours = detailed_tours
    
    return best_tours, best_max_distance

tours, max_travel_cost = create_robot_tours()

# Output the results
for i, (tour, cost) in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_travel_cost}")