import math
from itertools import permutations

# Define the city coordinates
cities = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
          (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
          (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
          (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
          (155, 185), (139, 182)]

# Number of robots
num_robots = 4

# Function to calculate the Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate initial solution: split cities between robots naively
def initial_solution(cities, num_robots):
    tours = []
    non_depot_cities = list(range(1, len(cities)))  # Exclude depot city at index 0
    chunk_size = len(non_depot_cities) // num_robots
    for i in range(num_robots):
        tour = [0]  # Start at the depot
        if i < num_robots - 1:
            tour.extend(non_depot_cities[i*chunk_size:(i+1)*chunk_size])
        else:
            tour.extend(non_depot_cities[i*chunk_size:])  # Handle remaining cities in the last tour
        tour.append(0)  # Return to depot
        tours.append(tour)
    return tours

# Compute total travel cost of a tour
def tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Generate the initial tours
tours = initial_solution(cities, num_robots)

# Display the results
overall_total_cost = 0
for idx, tour in enumerate(tours):
    cost = tour_cost(tour, cities)
    overall_total_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Sea Cost: {overall_total_cost:.2f}")