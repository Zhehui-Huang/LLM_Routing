import math
import random

def euclidean_dist(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35)
}

# Initialize a distance matrix
distance_matrix = [[euclidean_dist(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Initial solution
def initial_solution():
    cities_list = list(cities.keys())[2:]  # excluding depots
    random.shuffle(cities_list)
    mid = len(cities_list) // 2
    return [cities_list[:mid], cities_list[mid:]]

# Calculate total distance for tours
def calculate_cost(tours):
    total_cost = 0
    for depot, tour in enumerate(tours):
        # start at respective depot
        cost = 0
        current_city = depot  # Robot starts at its depot
        for city in tour:
            cost += distance_matrix[current_city][city]
            current_city = city
        total_cost += cost
    return total_cost

# Simulated Annealing
def simulated_annealing(tours):
    T = 1000
    cooling_rate = 0.995
    iterations = 3000
    
    current_solution = tours
    current_cost = calculate_cost(current_solution)
    best_solution = current_solution
    best_cost = current_cost
    
    for i in range(iterations):
        # Generate a new candidate solution
        new_solution = [list(tour) for tour in current_solution]
        # Pick a random tour and do a random swap or shift
        tour_idx = random.randint(0, 1)
        city_idx = random.randint(0, len(new_solution[tour_idx]) - 1)
        if random.random() > 0.5:  # Swap within a tour
            swap_idx = random.randint(0, len(new_solution[tour_idx]) - 1)
            new_solution[tour_idx][city_idx], new_solution[tour_idx][swap_idx] = new_solution[tour_idx][swap_idx], new_solution[tour_idx][city_idx]
        else:  # Move between tours
            other_tour = 1 - tour_idx
            new_solution[other_tour].append(new_solution[tour_idx].pop(city_idx))
        
        new_cost = calculate_cost(new_solution)
        
        # Acceptance probability
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
            current_solution = new_solution
            current_cost = new_cost
            
            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost
                
        T *= cooling_rate
        
    return best_solution, best_cost

# Initialize tours starting from respective depots
initial_tours = initial_solution()
# Apply Simulated Annealing
optimized_tours, optimized_cost = simulated_annealing(initial_tours)

# Output final tours and costs
tours_output = []
total_cost = 0
for robot_id in range(2):
    tour = [robot_id] + optimized_tours[robot_id]
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    total_cost += tour_cost
    tours_output.append((robot_id, tour, tour_cost))

for robot_id, tour, tour_cost in tours_output:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")