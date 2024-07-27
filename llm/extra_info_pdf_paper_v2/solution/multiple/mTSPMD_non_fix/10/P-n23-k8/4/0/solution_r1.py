import math
import random

# Defining the coordinates for each city
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initialize initial solution where each robot starts at depot city 0
def initial_solution(num_robots, num_cities):
    tours = [[] for _ in range(num_robots)]
    city_indices = list(range(num_cities))
    random.shuffle(city_indices)  # Shuffle cities to randomize assignment (except depots)
    depot = 0  # Single starting depot city index

    city_iterator = iter(city_indices)
    for tour in tours:
        tour.append(depot)  # Start from the depot
    
    for city in city_iterator:
        if city != depot:  # Avoid re-adding the depot
            min_length_tour = min(tours, key=len)
            min_length_tour.append(city)

    return tours

# Calculate the total travel cost for a specific tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Simulated Annealing to improve the solution
def simulated_annealing(tours, temp=10000, cooling_rate=0.995, stopping_temp=1):
    best_tours = [tour[:] for tour in tours]
    current_temp = temp

    while current_temp > stopping_temp:
        next_tours = [tour[:] for tour in best_tours]
        # Select a random tour to modify
        selected_tour = random.choice(next_tours)
        if len(selected_tour) > 2:  # Need at least 3 nodes to make a swap (depot and two others)
            i, j = sorted(random.sample(range(1, len(selected_tour)), 2))  # Choose two different cities to swap, excluding depot
            selected_tour[i], selected_tour[j] = selected_tour[j], selected_tour[i]

            current_cost = sum(tour_cost(tour) for tour in best_tours)
            next_cost = sum(tour_cost(tour) for tour in next_tours)
            
            if next_cost < current_cost or random.random() < math.exp((current_cost - next_cost) / current_temp):
                best_tours = next_tours

        current_temp *= cooling_rate

    return best_tours

# Define the number of cities and robots
num_cities = len(cities)
num_robots = 8

# Get initial and optimized tours
initial_tours = initial_solution(num_robots, num_cities)
optimized_tours = simulated_annealing(initial_tours)

# Display results
overall_total_cost = 0
for i, tour in enumerate(optimized_tours):
    cost = tour_cost(tour)
    overall_total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")