import math
import random

# Cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

# Number of robots and their corresponding depot city
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def initial_solution(depots, num_robots, cities):
    non_depots = [city for city in cities if city not in depots]
    random.shuffle(non_depots)
    chunks = [non_depots[i::num_robots] for i in range(num_robots)]
    tours = [[depots[i]] + chunks[i] for i in range(num_robots)]
    return tours

def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def simulated_annealing(initial_tours, num_iterations=10000, initial_temp=1000, cooling_rate=0.995):
    current_tours = initial_tours
    current_cost = sum(calculate_tour_cost(tour) for tour in current_tours)
    best_tours = current_tours
    best_cost = current_cost
    temperature = initial_temp

    for _ in range(num_iterations):
        for tour_index in range(len(current_tours)):
            i = random.randint(1, len(current_tours[tour_index]) - 1)  # Skip depot
            j = random.randint(1, len(current_tours[tour_index]) - 1)  # Skip depot
            current_tours[tour_index][i], current_tours[tour_index][j] = current_tours[tour_index][j], current_tours[tour_index][i]

            new_cost = sum(calculate_tour_cost(tour) for tour in current_tours)

            if new_cost < best_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
                current_cost = new_cost
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tours = [list(tour) for tour in current_tours]
            else:
                # revert swap
                current_tours[tour_index][i], current_tours[tour_index][j] = current_tours[tour_index][j], current_tours[tour_index][i]

        temperature *= cooling_rate

    return best_tours, best_cost

# Initialize the problem
depots = [0, 1, 2, 3]
num_robots = 4
initial_tours = initial_solution(depots, num_robots, list(cities.keys()))
optimized_tours, overall_cost = simulated_annealing(initial_tours)

# Display the results
for index, tour in enumerate(optimized_tours):
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")