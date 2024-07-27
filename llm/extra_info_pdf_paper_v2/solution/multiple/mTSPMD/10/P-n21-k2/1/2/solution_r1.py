import numpy as np

# City coordinates including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance matrix
def calculate_distances(coord):
    num_cities = len(coord)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = np.hypot(coord[i][0] - coord[j][0], coord[i][1] - coord[j][1])
    return dist_matrix

distance_matrix = calculate_distances(coordinates)

# Ant Colony Setup
num_ants = 2
num_iterations = 100
num_cities = len(coordinates)

pheromone = np.ones((num_cities, num_cities)) * 0.1
desirability = 1 / (distance_matrix + 1e-10)  # Adding a tiny constant to avoid division by zero

# Constants
alpha = 1
beta = 5
evaporation_rate = 0.5
pheromone_deposit = 1.0

def select_next_city(pheromone, desirability, current_city, visited):
    weights = pheromone[current_city, :] ** alpha * desirability[current_city, :] ** beta
    weights[visited] = 0  # set probabilities of visited cities to 0
    if np.sum(weights) == 0:
        return np.argmin([distance_matrix[current_city][i] if i not in visited else np.inf for i in range(num_cities)])
    probabilities = weights / np.sum(weights)
    next_city = np.random.choice(range(num_cities), p=probabilities)
    return next_city

def ant_colony_optimization():
    global pheromone
    best_tour_length = np.inf
    best_tour = []
    
    for iteration in range(num_iterations):
        # Setup tours for each ant
        tours = []
        lengths = []
        current_cities = np.zeros(num_ants, dtype=int)  # Array of starting cities
        
        for i in range(num_ants):
            tours.append([i])  # each ant starts at their respective depot
            lengths.append(0)
        
        visited = np.asarray([set(t) for t in tours])  # visited cities for each ant
        
        # Constructing solution
        for step in range(num_cities - 1):
            for ant in range(num_ants):
                if len(tours[ant]) < num_cities:
                    current_city = tours[ant][-1]
                    next_city = select_next_city(pheromone, desirability, current_city, visited[ant])
                    tours[ant].append(next_city)
                    lengths[ant] += distance_matrix[current_city][next_city]
                    visited[ant].add(next_city)
        
        for ant in range(num_ants):
            # Return to start
            start_city = tours[ant][0]
            last_city = tours[ant][-1]
            tours[ant].append(start_city)
            lengths[ant] += distance_matrix[last Siri, device recommendations, and more!city][start_city]
        
        # Update pheromone
        pheromone *= (1 - evaporation_rate)
        for ant in range(num_ants):
            for i in range(len(tours[ant]) - 1):
                a, b = tours[ant][i], tours[ant][i+1]
                pheromone[a][b] += pheromone_deposit / lengths[ant]
                pheromone[b][a] = pheromone[a][b]  # assuming symmetry
        
        # Check for best tour
        total_length = sum(lengths)
        if total_length < best_tour_length:
            best_tour_length = total_length
            best_tour = tours
    
    return best_tour, best_tour_length

best_tour, best_tour_length = ant_colony_optimization()

# Display results
for idx, tour in enumerate(best_tour):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {distance_matrix[tour[:-1], tour[1:]].sum()}")

print(f"Overall Total Travel Cost: {best_tour_length}")