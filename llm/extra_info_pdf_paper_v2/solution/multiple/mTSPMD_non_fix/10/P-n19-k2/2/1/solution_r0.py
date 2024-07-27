import math
import random

# Define the city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initial solution (random partition)
def initial_solution(cities, k=2):
    all_cities = list(cities.keys())[2:]  # Exclude depots from initial random partition
    random.shuffle(all_cities)
    partition_size = len(all_cities) // k
    return [all_cities[i * partition_size:(i + 1) * partition_size] for i in range(k)]

# Cost of a single tour starting and ending at a depot
def tour_cost(tour, depot):
    total_distance = distance(depot, tour[0])
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i + 1])
    total_distance += distance(tour[-1], depot)
    return total_distance

# Total cost for all tours
def total_cost(tours, depots):
    return sum(tour_cost(tour, depot) for tour, depot in zip(tours, depots))

# Simulated annealing to optimize the tours
def simulated_annealing(cities, depots=[0, 1], Tmax=10000, Tmin=1, cooling_rate=0.95):
    current_solution = initial_solution(cities, k=len(depots))
    current_cost = total_cost(current_solution, depots)
    T = Tmax

    while T > Tmin:
        i = random.randint(0, len(depots) - 1)  # Choose a random robot
        if len(current_solution[i]) > 1:
            a, b = random.sample(range(len(current_solution[i])), 2)
            new_solution = [current_solution[j][:] for j in range(len(depots))]
            new_solution[i][a], new_solution[i][b] = new_solution[i][b], new_solution[i][a]  # Swap two cities
            
            new_cost = total_cost(new_solution, depots)
            
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
                current_solution, current_cost = new_solution, new_cost
        
        T *= cooling_rate

    return current_solution, current_cost

# Run simulated annealing
solution, solution_cost = simulated_annealing(cities)

# Format and provide output
print("Overall Total Travel Cost:", solution_cost)
for idx, tour in enumerate(solution):
    depot = idx
    tour_with_depot = [depot] + [2 + city for city in tour] + [depot]
    cost = tour_cost(tour, depot)
    print(f"Robot {idx} Tour: {tour_with_depot}")
    print(f"Robot {idx} Total Travel Cost: {cost}")