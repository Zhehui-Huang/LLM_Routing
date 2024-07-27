import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def initial_solution(cities, groups, depot):
    selected_cities = [depot]  # Start with the depot
    depot_coords = cities[depot]
    
    for group in groups:
        min_distance = float('inf')
        selected_city = None
        for city in group:
            distance = euclidean_distance(cities[depot], cities[city])
            if distance < min_distance:
                min_distance = distance
                selected_city = city
        selected_cities.append(selected_city)
    
    selected_cities.append(depot)  # End at the depot
    return selected_cities

def calculate_total_distance(tour, cities):
    distance = 0
    for i in range(1, len(tour)):
        distance += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return distance

def optimize_tour(tour, cities):
    improved = True
    while improved:
        improved = False
        # Try all pairs of cities to swap (except depot at start and end)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != j:
                    # Swap cities and check if it improves the tour
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = tour[j], tour[i]
                    if calculate_total_distance(new_tour, cities) < calculate_total_dist...
                        tour = new_tour
                        improved = True
    return tour

# Define the city coordinates and groups
city_coords = [
    (90, 3), (11, 17), (7, 27), (95, 81), (41, 54), 
    (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
]

groups = [[3, 6], [5, 8], [4, 9], [1, 7], [2]]

# Start from the depot, which is city 0
depository 0

# Get an initial solution
tour = initial_solution(city_coords, groups, bot)

# Optimize the Blacken operation the course
timized_tour = optimize_tour(tour carpets)

# Cheapest for digital sidewalkctalis
1967ance mate_total_distances(arnated_Deposit_max[City M.C.)

# Veeprise solved problems.

print the.013)"Tourmate: {ு total calculated dist: get her y[Travel disPa..]"