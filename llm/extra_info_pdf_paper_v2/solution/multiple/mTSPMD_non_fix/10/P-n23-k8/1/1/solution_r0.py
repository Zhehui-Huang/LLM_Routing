import math
import random

# Coordinates of all cities including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37) 
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initial naive solution split equitably among the robots
def initial_solution(num_robots, depot, cities):
    cities_to_visit = list(cities.keys())[depot:]
    chunk_size = len(cities_to_visit) // num_robots
    return [cities_to_visit[i*chunk_size:(i+1)*chunk_size] for i in range(num_robots)]

# Total cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Simulated Annealing process
def simulated_annealing(tours, num_robots, temperature, cooling_rate):
    current_tours = tours
    current_cost = sum(tour_cost(tour) for tour in current_tours)
    best_tours = current_tours
    best_cost = current_cost
    
    while temperature > 1:
        for _ in range(100):  # Number of iterations at current temperature
            new_tours = current_tours[:]  # Copy current tours
            for i in range(num_robots):  # Modify each robot's tour
                if len(new_tours[i]) > 2:  # At least three cities to make a swap meaningful
                    a, b = random.sample(range(1, len(new_tours[i])-1), 2)
                    new_tours[i][a], new_tours[i][b] = new_tours[i][b], new_tours[i][a]
            
            new_cost = sum(tour_cost(tour) for tour in new_tours)
            if new_cost < current_cost or math.exp((current_cost - new_cost) / temperature) > random.random():
                current_tours = new_tours
                current_cost = new_cost
                
                if current_cost < best_cost:
                    best_tours = current_tours
                    best_cost = current_cost
                    
        temperature *= cooling_rate  # Cooling down
    
    return best_tours, best_cost

# Number of robots and depot city (starting points for all robots)
num_robots = 8
depot = 0

# Obtain initial tours
initial_tours = initial_solution(num_robots, depot, cities)
tours, total_cost = simulated_annealing(initial_tours, num_robots, temperature=1000, cooling_rate=0.995)

# Output the results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {[depot] + tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost([depot] + tour)}")

print(f"\nOverall Total Travel Cost: {total_cost}")