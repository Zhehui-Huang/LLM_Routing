import math
import random

# Define the coordinates for each city, including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69),
    18: (45, 35)
}

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(tour):
    """Calculate the total distance of the tour."""
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def simulated_annealing(cities, depot, num_iterations=10000, start_temp=100, alpha=0.99):
    """Perform the Simulated Annealing algorithm to find the optimal tour starting from a special depot."""
    # Start with an initial solution (random tour)
    city_indices = list(cities.keys())
    city_indices.remove(depot)
    initial_tour = [depot] + random.sample(city_indices, len(city_indices)) + [depot]
    
    current_tour = initial_tour[:]
    current_distance = total_distance(current_tour)
    best_tour = current_tour[:]
    best_distance = current_distance
    temperature = start_temp

    for i in range(num_iterations):
        # Lower the temperature
        temperature *= alpha
        
        # Create a new tour by swapping two cities
        new_tour = current_tour[:]
        left_idx = random.randint(1, len(new_tour) - 3)
        right_idx = random.randint(left_idx + 1, len(new_tour) - 2)
        new_tour[left_idx], new_tour[right_idx] = new_tour[right_idx], new_tour[left_idx]

        # Calculate the tour's distance
        new_distance = total_partition_distance(new_tour)

        # Acceptance probability to possibly accept a worse solution
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_tour = new_tour[:]
            current_distance = new_distance
        
        # Check if the new solution is the best found so far
        if current_distance < best_distance:
            best_tour = current_tour[:]
            best_distance = current_distance

    return best_tour, best_distance

# Run Simulated Annealing for each robot starting from its depot
robot_0_tour, robot_0_cost = simulated_annealing(cities, 0)
robot_1_tour, robot_1_cost = simulated_annealing(cities, 1)

overall_cost = robot_0_cost + robot_1_cost

# Output results
print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost:.2f}\n")
print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost:.2f}\n")
print(f"Overall Total Travel Cost: {overall_cost:.2f}")