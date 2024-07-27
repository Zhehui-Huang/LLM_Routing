import math
import random

# Cities and coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
          (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
          (32, 39), (56, 37)]

# Euclidean distance calculation
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate an initial feasible solution: Sequential assignment
def initial_solution(depot, num_robots):
    tours = [[] for _ in range(num_robots)]
    assigned_cities = set(depot)
    city_indices = list(range(len(cities)))
    random.shuffle(city_indices)
    robot = 0
    
    for city in city_indices:
        if city not in assigned_cities:
            tours[robot].append(city)
            robot = (robot + 1) % num_robots
    for i in range(num_robots):
        tours[i].insert(0, depot[i])
    return tours

# Compute total tour cost
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

# Simulated Annealing to improve the solution
def simulated_annealing(tours, temp=10000, cooling_rate=0.995, stopping_temp=1):
    current_temp = temp
    current_tours = tours
    best_tours = tours
    best_cost = sum(tour_cost(tour) for tour in tours)
    
    while current_temp > stopping_temp:
        next_tours = [tour[:] for tour in current_tours]
        # Perform a swap in one of the tours
        sel_tour = random.choice(next_tours)
        i, j = random.sample(range(1, len(sel_tour)), 2)  # avoid swapping the depot
        sel_tour[i], sel_tour[j] = sel_tour[j], sel_tour[i]
        
        current_cost = sum(tour_cost(tour) for tour in current_tours)
        next_cost = sum(tour_cost(tour) for tour in next_tours)
        
        if next_cost < current_cost or random.random() <= math.exp((current_cost - next_cost) / current_temp):
            current_tours = next_tours
        
        if next_cost < best_cost:
            best_tours = next_tours
            best_cost = next_cost
        
        current_temp *= cooling_rate
    
    return best_tours

# Initialize robot tours
depots = [0, 1, 2, 3, 4, 5, 6, 7]
num_robots = len(depots)
initial_tours = initial_solution(depots, num_robots)
optimized_tours = simulated_annealing(initial_tours)

# Calculate and display results
total_travel_cost = 0
for i, tour in enumerate(optimized_tours):
    cost = tour_cost(tour)
    total_travel_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")
print(f"Overall Total Travel.AutowiredFra: {total_travel_cost:.2f}")