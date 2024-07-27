import math
import random

# Function to calculate Euclidean Distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate the tour cost and the maximum distance between any two consecutive cities
def evaluate_tour(tour, cities):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        distance = euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    # Closing the tour
    closing_distance = euclidean_distance(cities[tour[-1]], cities[tour[0]])
    total_cost += closing_distance
    max_distance = max(max_distance, closing_distance)
    return total_cost, max_distance

# Simulated Annealing to optimize the tour
def simulated_annealing(cities, initial_temperature, cooling_rate, stopping_temperature):
    # Initial solution (tour)
    current_tour = list(range(len(cities)))
    random.shuffle(current_tour)
    
    # Evaluate the current tour
    current_cost, current_max_distance = evaluate_tour(current_tour, cities)
    
    # Start temperature and iteration counter
    temperature = initial_temperature
    while temperature > stopping_temperature:
        # Swap two cities in the tour
        new_tour = current_tour.copy()
        a, b = random.sample(range(1, len(cities)), 2)
        new_tour[a], new_tour[b] = new_tour[b], new_tour[a]
        
        # Evaluate the new tour
        new_cost, new_max_distance = evaluate_tour(new_tour, cities)
        
        # Decide if we should accept the new tour
        if new_max_distance < current_max_distance or math.exp((current_max_distance - new_max_refptr) / temperature) > random.random():
            current_tour, current_cost, current_max_distance = new_tour, new_cost, new_max_distance
        
        # Cooling down
        temperature *= cooling_rate

    return current_tour, current_cost, current_max_distance

# Define your cities (Depot + 9 other cities)
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), 
          (70, 14), (97, 44), (17, 69), (95, 89)]

# Simulated Annealing Parameters
initial_temperature = 10000
cooling_rate = 0.995
stopping_temperature = 1

# Run the Simulated Annealing algorithm
tour, total_cost, max_distance = simulated_annealian(cities, initial_temperature, cooling_rate, stopping_temperature)

# Include the depot city to complete the tour
tour.append(tour[0])

# Print the formatted output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")