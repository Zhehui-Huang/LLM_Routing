import math
import random

# Coordinates of all cities (including depots)
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Simulated Annealing to minimize the travel distance
def simulated_annealing(cities, initial_temperature, cooling_rate, number_of_iterations):
    current_solution = random.sample(range(2, len(cities)), len(cities) - 2)
    current_solution = [0] + current_solution  # Robot 0 starts from depot 0
    current_cost = calculate_cost(current_solution)
    
    best_solution = current_solution[:]
    best_cost = current_cost
    
    temperature = initial_temperature
    
    for _ in range(number_of_iterations):
        for _ in range(len(cities) - 1):
            new_solution = current_solution[:]
            # Create new solution: swap two cities randomly (excluding the depot)
            city1, city2 = random.sample(range(1, len(cities) - 1), 2)
            new_solution[city1], new_solution[city2] = new_solution[city2], new_solution[city1]
            
            new_cost = calculate_cost(new_solution)
            
            # Acceptance probability
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
                current_solution, current_cost = new_solution, new_cost
                if current_cost < best_cost:
                    best_solution, best_cost = current_solution[:], current_cost
        
        temperature *= cooling_rate  # Decrease temperature
    
    return best_solution, best_cost

def calculate_cost(solution):
    cost = 0
    for i in range(len(solution) - 1):
        cost += distance(cities[solution[i]], cities[solution[i+1]])
    return cost

# Parameters for Simulated Annealing
initial_temperature = 10000
cooling_rate = 0.995
number_of_iterations = 1000

# Perform Simulated Annealing
tour, tour_cost = simulated_annealing(cities, initial_temperature, cooling_rate, number_of_iterations)

# Display the results
print(f"Robot 0 Tour: {tour}")
print(f"Robot 0 Total Travel Cost: {tour_cost:.2f}")

# Since only one robot is utilized in this example solution (and no specified tasks for the second robot),
# additional implementation would be required to optimally utilize the second robot.
overall_cost = tour_cost
print(f"Overall Total Travel Cost: {overall_cost:.2f}")