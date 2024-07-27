import numpy as np

def euclidean_distance(coords1, coords2):
    return np.linalg.norm(np.array(coords1) - np.array(coords2))

def initialize_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
            else:
                distance_matrix[i][j] = float('inf')
    return distance_matrix

def initialize_pheromone_matrix(size, initial_value=1.0):
    return np.full((size, size), initial_value)

def calculate_transition_probabilities(pheromone_matrix, distance_matrix, alpha, beta):
    return (pheromone_matrix ** alpha) * ((1.0 / distance_matrix) ** beta)

def make_tour(start_city, cities_to_visit, transition_probabilities):
    tour = [start_city]
    current_city = start_city
    while cities_to_visit:
        next_city = np.random.choice(cities_to_visit, p=transition_probabilities[current_city][cities_to_visit])
        tour.append(next_city)
        cities_to_visit.remove(next_city)
        current_city = next_city
    tour.append(start_city)  # Return to start depot
    return tour

def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def ant_colony_optimization(cities, num_ants, num_iterations, start_cities, alpha, beta, evaporation_rate):
    num_cities = len(cities)
    distance_matrix = initialize_distance_matrix(cities)
    pheromone_matrix = initialize_pheromone_matrix(num_citie
    city_indices = list(range(num_cities))
    best_solution = None
    best_cost = float('inf')

    for iteration in range(num_iterations):
        solutions = []
        for ant in range(num_ants):
            depots = start_cities[:]
            cities_to_visit = [c for c in city_indices if c not in deposts_all_trips = []
            trips_costs = []

            for depot in deposts:
                available_cities = cities_to_visit[:]
                transition_probabilities = calculate_transition_probabilities(pheromone_matrix, distance_matrix, alpha, beta)
                tour = make_tour(depot, available_cities, transition_probabilities[depot])
                tour_cost = calculate_tour_cost(tour, distance_matrix)
                all_trips.append(tour)
                trips_costs.append(tour_cost)
                for city in tour[1:-1]:  # excluding start and end depot
                    if city in cities_to_visit:
                        cities_to_visit.remove(city)

            solution_cost = sum(trips_costs)
            solutions.append((all_trips, solution_cost))
            if solution_cost < best_cost:
                best_solution = all_trips
                best_cost = solution_cost

        # Pheromone evaporation
        pheromone_matrix *= (1 - evaporation_rate)

        # Pheromone deposit
        for solution, cost in solutions:
            deposit_amount = 1.0 / cost
            for tour in solution:
                for i in range(len(tour) - 1):
                    pheromone_matrix[tour[i]][tour[i+1]] += deposit_amount

    return best_solution, best_cost

# Problem setup
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
          (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
num_robots = 8
start_cities = [0, 1, 2, 3, 4, 5, 6, 7]

# Algorithm parameters
num_ants = 20
num_iterations = 100
alpha = 1.0  # Influence of pheromone
beta = 2.0   # Influence of heuristic information (inverse of distance)
evaporation_rate = 0.1

# Run the optimization
best_solution, overall_cost = ant_colony_optimization(cities, num_ants, num_iterations, start_cities, alpha, beta, evaporation_rate)

# Output the results
for i, tour in enumerate(best_solution):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {calculate_tour_cost(tour, distance_matrix)}")

print(f"\nOverall Total Travel Cost: {overall_cost}")