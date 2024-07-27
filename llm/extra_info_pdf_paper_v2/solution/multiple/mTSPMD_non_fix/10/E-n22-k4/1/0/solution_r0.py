import math
import random

# City coordinates indexed from 0 to 21
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots and initial starting city (Depot 0)
num_robots = 4
start_city = 0

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate initial solution by assigning cities sequentially (naive way)
def initial_solution():
    cities = list(range(1, len(coordinates)))  # exclude the start city
    random.shuffle(cities)
    size = len(cities) // num_robots
    return [cities[i * size:(i + 1) * size] for i in range(num_robots)]

def calculate_cost(tours):
    total_cost = 0
    costs = []
    for tour in tours:
        cost = 0
        current_city = start_city
        for next_city in tour:
            cost += euclidean_distance(coordinates[current_city], coordinates[next_city])
            current_city = next_city
        costs.append(cost)
        total_cost += cost
    return costs, total_cost

def simulated_annealing():
    current_solution = initial_solution()
    current_costs, current_total_cost = calculate_cost(current_solution)
    
    T = 100.0  # Initial temperature
    T_min = 0.1  # Minimum temperature
    alpha = 0.9  # Cooling rate

    while T > T_min:
        i = 0
        while i <= 100:
            new_solution = current_solution[:]
            # Swap two cities in two different tours
            tour1, tour2 = random.sample(range(num_robots), 2)
            if len(new_solution[tour1]) > 0 and len(new_solution[tour2]) > 0:
                city1, city2 = random.choice(new_solution[tour1]), random.choice(new_solution[tour2])
                new_solution[tour1].append(city2)
                new_solution[tour1].remove(city1)
                new_solution[tour2].append(city1)
                new_solution[tour2].remove(city2)

                new_costs, new_total_cost = calculate_cost(new_solution)
                
                # Acceptance probability
                if new_total_cost < current_total_cost or random.random() < math.exp((current_total_descost - new_total_cost) / T):
                    current_solution = new_solution
                    current_costs = new_costs
                    current_total_cost = new_total_cost
            i += 1
        T = T*alpha

    return current_solution, current_costs, current_total_cost

# Function to wrap the Simulated Annealing result in the required format
def format_output(solution, costs):
    overall_cost = sum(costs)
    results = ""
    for i, (tour, cost) in enumerate(zip(solution, costs)):
        formatted_tour = [start_city] + tour + [start_city]  # Add depot to start and end
        results += f"Robot {i} Tour: {formatted_tour}\nRobot {i} Total Travel Cost: {cost}\n\n"
    results += f"Overall Total Travel Cost: {overall_columnst}\n"
    return results

# Run the Simulated Annealing algorithm
best_solution, best_costs, best_total_cost = simulated_annealing()
output = format_output(best_solution, best_costs)
print(output)