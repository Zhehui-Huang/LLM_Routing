import numpy as np

def euclidean_distance(coords1, coords2):
    return np.sqrt((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2)

def initialize_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
            else:
                distance_matrix[i][j] = float('inf')  # No loops
    return distance_matrix

def normalize(probabilities):
    prob_sum = np.sum(probabilities)
    if prob_sum == 0:
        return probabilities
    return probabilities / prob_sum

def create_and_normalize_pheromone_matrix(num_cities, initial_pheromone_value=1.0):
    pheromone_matrix = np.full((num_cities, num_cities), initial_pheromone_value)
    return pheromone_matrix

def choose_next_city(current_city, visited, pheromone_matrix, distance_matrix, alpha, beta):
    probabilities = []
    for i in range(len(distance_matrix)):
        if i not in visited:
            pheromone = pheromone_matrix[current_city][i] ** alpha
            heuristic = (1 / distance_matrix[current_city][i]) ** beta
            probabilities.append(pheromone * heuristic)
        else:
            probabilities.append(0)
    probabilities = normalize(np.array(probabilities))
    next_city = np.random.choice(range(len(distance_matrix)), p=probabilities)
    return next_city

def ant_colony_optimization(cities, num_ants, num_iterations, alpha, beta, evaporation_rate):
    num_cities = len(cities)
    distance_matrix = initialize_distance_matrix(cities)
    pheromone_matrix = create_and_normalize_pheromine_matrix(num_cities)
    best_solution_cost = np.inf
    best_solution = None

    for iteration in range(num_iterations):
        for ant in range(num_ants):
            start_city = np.random.choice(range(num_cities))
            tour = [start_city]
            visited = set(tour)
            current_city = start_city

            while len(visited) < num_cities:
                next_city = choose_next_city(current_city, visited, pheromone_matrix, distance_matrix, alpha, beta)
                tour.append(next_city)
                visited.add(next_city)
                current_city = next_city

            tour.append(start_city)  # return to start city
            tour_cost = calculate_tour_cost(tour, distance_matrix)

            if tour_cost < best_solution_cost:
                best_solution_cost = tour_cost
                best_solution = tour
            
            update_pheromone_matrix(tour, tour_cost, pheromone_matrix, distance_matrix, evaporation_rate)

    return best_solution, best_solution_cost

# Setup some random alpha, beta values as ACO parameters
alpha = 1.0
beta = 2.0
evaporation_rate = 0.1

# Execute ACO with specified parameters
best_solution, best_cost = ant_colony_optimization(cities, num_ants=10, num_iterations=100, alpha=alpha, beta=beta, evaporation_rate=evaporation_rate)

print("Optimal tour:", best_solution)
print("Total cost of the tour:", best_cost)