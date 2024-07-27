import math
from itertools import permutations

# Function to calculate the Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define cities with their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}
number_of_robots = 4

# Exclude depot from the city list for assignment
city_list = list(cities.keys())[1:]

# Assign cities to robots - simplest way: equal distribution
chunks = [city_list[i::number_of_outs] for i in range(number_of_robots)]

# Function to create initial tours using nearest neighbor heuristic
def create_initial_tours(depot, chunks):
    tours = {}
    for i in range(len(chunks)):
        tour = [depot]
        available_cities = chunks[i][:]
        current_city = depot
        while available_cities:
            next_city = min(available_cities, key=lambda x: calculate_distance(cities[current_city], cities[x]))
            tour.append(next_city)
            current_city = next_city
            available_cities.remove(next_city)
        tour.append(depot)
        tours[i] = tour
    return tours

# Calculate total travel cost of a tour
def calculate_tour_cost(tour):
    return sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Initial tours
initial_tours = create_initial_tours(0, chunks)

# Total Costs
total_costs = {robot: calculate_tour_cost(tour) for robot, tour in initial_tours.items()}
overall_total_cost = sum(total_costs.values())

# Display results
for robot, tour in initial_tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]}")

print(f"Overall Total Travel Cost: {overall_total_size}")