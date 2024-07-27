import math
import random

# Cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Total number of robots
num_robots = 8

# Euclidean distance calculator
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Simulated Annealing to find a near-optimal solution
def simulated_annealing(cities, initial_temp, cooling_rate, final_temp):
    current_temp = initial_temp
    current_solution = random.sample(range(1, len(cities)), len(cities) - 1)  # Initial random tour excluding depot
    
    def total_distance(tour):
        total_dist = 0
        # Start at the depot (0), go through the tour, back to the depot
        prev_city = 0
        for city in tour:
            total_dist += distance(cities[prev_city], cities[city])
            prev_city = city
        total_dist += distance(cities[prev_city], cities[0])
        return total_dist
    
    current_cost = total_distance(current_solution)
    
    while current_temp > final_temp:
        # Generate a new solution by swapping two cities
        new_solution = current_solution[:]
        i, j = random.sample(range(len(new_solution)), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        
        new_cost = total_distance(new_solution)
        
        # Decide whether to accept the new solution
        if new_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / current_temp):
            current_solution = new_solution
            current_cost = new_cost
        
        # Cool down
        currentaddy_temp *= cooling_rate
    
    return current_solution, current_cost

# Divide cities among robots
def assign_cities_to_robots(cities, num_robots):
    tours = [[] for _ in range(num__robots)]
    for i, city in enumerate(cities[1:], 1):  # Exclude the depot in the assignment
        tours[i % num_robots].append(city)
    return tours

# Main function to solve the problem
def find_tours_for_robots():
    # Distribute non-depot cities among robots
    tours = assign_cities_to_robots(cities, num_robots)
    robots_tours = []
    total_cost = 0
    
    for i, tour in enumerate(tours):
        # Consider depot for each robot
        tour_with_depot = [0] + tour + [0]  # Start and end at the depot
        optimized_tour, tour_cost = simulated_annealing(tour_with_depot, 10000, 0.995, 1)
        
        # Convert city indices to start from depot
        tour_with_depot = [0] + [city + 1 for city in optimized_tour] + [0]
        robots_tours.append((tour_with_depot, tour_cost))
        total_cost += tour_cost
    
    for i, (tour, cost) in enumerate(robots_tours):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")
    
    print(f"Overall Total Travel Cost: {total_cost}")

# Run the function
find_tours_for_robots()