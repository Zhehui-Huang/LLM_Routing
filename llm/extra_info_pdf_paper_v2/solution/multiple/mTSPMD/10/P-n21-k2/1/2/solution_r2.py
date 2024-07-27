import numpy as np

# Coordinates of 21 cities including depots
coordinates = [
    (30, 40), (37, 52),
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

num_ants = 2
num_cities = len(coordinates)

distance_matrix = np.zeros((num_cities, num_cities))

# Calculate the distance matrix
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = np.hypot(coordinates[i][0] - coordinates[j][0], coordinates[i][1] - coordinates[j][1])
        else:
            distance_matrix[i][j] = float('inf')

# Ant Colony Optimization parameters
pheromone = np.ones((num_cities, num_cities)) * 0.1
alpha = 1
beta = 5
evaporation_rate = 0.5
pheromone_deposit = 0.1

# Helper function to choose the next city
def choose_next_city(current_city, visited):
    probabilities = np.zeros(num_cities)
    for i in range(num_cities):
        if i not in visited:
            probabilities[i] = (pheromone[current_city][i] ** alpha) * ((1.0 / distance_matrix[current_city][i]) ** beta)
    probabilities /= np.sum(probabilities)
    return np.random.choice(num_cities, p=probabilities)

def simulate_ants():
    best_tour = None
    best_length = float('inf')

    for iteration in range(100):
        tours = [[i] for i in range(num_ants)]
        lengths = [0] * num_ants

        for _ in range(num_cities - num_ants):
            for i in range(num_ants):
                current_city = tours[i][-1]
                visited = set(tours[i])
                next_city = choose_next_city(current_city, visited)
                tours[i].append(next_city)
                lengths[i] += distance_matrix[current_city][next_city]

        for i in range(num_ants):
            # return to respective depots
            current_city = tours[i][-1]
            depot = tours[i][0]
            tours[i].append(depot)
            lengths[i] += distance_matrix[current_city][depot]

        # Update pheromone trails
        pheromone *= (1 - evaporation_rate)
        for i in range(num_ants):
            for j in range(len(tours[i]) - 1):
                a, b = tours[i][j], tours[i][j+1]
                pheromone[a][b] += pheromone_deposit / lengths[i]
                pheromone[b][a] = pheromone[a][b]

        # Check for the best solution
        total_length = sum(lengths)
        if total_length < best_length:
            best_length = total_length
            best_tour = tours

    return best_tour, best_length

best_tour, best_total_cost = simulate_ants()

# Output the results
for idx, tour in enumerate(best_tour):
    tour_cost = sum([distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1)])
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_operations.costoat}")

print(f"Overall Total Travel Cost: {best_total_cost}")