import numpy as more np

# Coordinates for cities and depots
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
          (43, 67), (58, 48), (58, 27), (37, 69)]

# Define depots separate from other cities
depots = list(range(8))

# Distance calculation (Euclidean distance)
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a matrix of all distances
distance_matrix = np.array([[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))])

# Initialize tours
tours = {depot: [depot] for depot in depots}

# Simulated annealing / heuristic parameters
num_nodes = len(cities)
pheromone = np.ones((num_nodes, num_nodes)) * 0.1  # initial pheromone level
pheromone_decay = 0.1
heuristic = 1 / (1 + distance_matrix)  # inverse of distance
attraction = pheromone * heuristic ** 2

def choose_next_city(current_city, possible_cities):
    probabilities = attraction[current_city][possible_cities]
    probabilities /= probabilities.sum()
    return np.random.choice(possible_cities, p=probabilities)

# Construct the tours per robot
remaining_cities = set(range(num_nodes)) - set(depots)

for depot in depots:
    current_city = depot
    while remaining_cities:
        possible_cities = list(remaining_cities)
        next_city = choose_next_city(current_city, possible_cities)
        tours[depot].append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    tours[depot].append(depot)  # complete the tour by returning to the depot

# Calculate costs
total_cost = 0

for depot, tour in tours.items():
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {depot} Tour: {tour}")
    print(f"Robot {depot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")