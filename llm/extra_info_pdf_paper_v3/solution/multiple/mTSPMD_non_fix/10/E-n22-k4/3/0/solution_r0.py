import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def initialize_cities():
    # Coordinates of all cities including depots
    return {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 
        3: (130, 254), 4: (128, 252), 5: (163, 247),
        6: (146, 246), 7: (161, 242), 8: (142, 239), 
        9: (163, 236), 10: (148, 232), 11: (128, 231),
        12: (156, 217), 13: (129, 214), 14: (146, 208),
        15: (164, 208), 16: (141, 206), 17: (147, 193),
        18: (164, 193), 19: (129, 189), 20: (155, 185),
        21: (139, 182)
    }

def simulated_annealing(cities, max_iterations=1000, initial_temp=100, cooling_rate=0.95):
    def calculate_total_distance(tours):
        total_dist = 0
        for tour in tours:
            for i in range(1, len(tour)):
                total_dist += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        return total_dist

    # Initial random assignment of cities to robots
    all_cities = list(cities.keys())
    all_cities.remove(0)  # Remove the depot
    random.shuffle(all_cities)
    partition_size = len(all_cities) // 4
    robot_tours = [ [0] + all_cities[i*partition_size:(i+1)*partition_size] for i in range(4)]
    
    current_temp = initial_temp
    best_tours = robot_tours
    best_cost = calculate_total_distance(robot_tours)

    for iteration in range(max_iterations):
        # Generate new neighbor tours
        new_tours = [tour[:] for tour in best_tours]
        for tour in new_tours:
            # Swap two cities in the tour
            if len(tour) > 2:
                i, j = random.sample(range(1, len(tour)), 2)
                tour[i], tour[j] = tour[j], tour[i]
        
        # Calculate new cost
        new_cost = calculate_total_distance(new_tours)
        
        # If new configuration is better, accept it
        if new_cost < best_cost or random.random() < math.exp(-(new_cost - best_cost) / current_temp):
            best_tours, best_cost = new_tours, new_cost
        
        # Cooling down
        current_temp *= cooling_rate

    return best_tours, best_cost

cities = initialize_cities()
best_tours, best_cost = simulated_annealing(cities)

# Output results
total_cost = 0
for idx, tour in enumerate(best_tours):
    tour_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    tour.append(0)  # Returning to the starting depot city 0
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost:.2f}")