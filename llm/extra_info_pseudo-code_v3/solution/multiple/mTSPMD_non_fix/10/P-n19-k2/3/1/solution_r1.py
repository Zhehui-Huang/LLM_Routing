import numpy as np

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate initial solution based on Nearest Neighbor Search
def nearest_neighbor_solution(depot, cities_list):
    tour = [depot]
    current = depot
    while cities_list:
        next_city = min(cities_list, key=lambda x: distance(current, x))
        tour.append(next_city)
        cities_list.remove(next_city)
        current = next_city
    return tour

# Calculate total travel cost of a tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)) + distance(tour[-1], tour[0])

# Implementing the NNS for initial solution and divide cities between two robots
def initial_solution():
    available_cities = list(range(2, 19))
    half = len(available_cities) // 2
    random.shuffle(available_cities)

    tour1 = nearest_neighbor_solution(0, available_cities[:half])
    tour2 = nearest_neighbor_solution(1, available_cities[half:])

    return tour1, tour2

# Generating and computing the tours
tour1, tour2 = initial_solution()

# Calculating the cost of each tour
cost_tour1 = calculate_tour_cost(tour1)
cost_tour2 = calculate_tour_cost(tour2)
total_cost = cost_tour1 + cost_tour2

# Outputting tour and cost information
print(f"Robot 0 Tour: {tour1}")
print(f"Robot 0 Total Travel Cost: {cost_tour1}\n")

print(f"Robot 1 Tour: {tour2}")
print(f"Robot 1 Total Travel Cost: {cost_tour2}\n")

print(f"Overall Total Travel Cost: {total_cost}")