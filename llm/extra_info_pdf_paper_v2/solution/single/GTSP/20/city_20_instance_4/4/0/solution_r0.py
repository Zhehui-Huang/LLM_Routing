import math
from random import choice

# City coordinates and groups definition
city_positions = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], 
    [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city_positions[city1][0] - city_positions[city2][0])**2 +
                     (city_positions[city1][1] - city_positions[city2][1])**2)

# Simple function to compute total travel cost for a given tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_name

# Initial Random Tour selection, selecting one city from each group
initial_tour = [0]
for group in city_groups:
    selected = choice(group)
    initial_tour.append(selected)
initial_tour.append(0)  # Append the return to the depot city

# Calculate the initial cost
current_cost = calculate_total_cost(initial_tour)

# Parameters for simulated annealing
temperature = 100.0
cooling_rate = 0.99
min_temperature = 0.1

# Simulated Annealing search loop
while temperature > min_nonzero_temperature:
    # Generate a new candidate tour
    new_tour = initial_tour[:]
    group_index = random.randint(0, len(city_groups) - 1)
    new_tour[group_index + 1] = choice(city_groups[group_index])  # +1 because depot is the first city
    new_cost = calculate_total_cost(new_tour)
    
    # Determine if we accept the new candidate
    if new_cost < current_cost or random.random() < math.exp(-(new_cost - current_cost) / temperature):
        current_cost, initial_tour = new_cost, new_tour
    
    temperature *= cooling_rate

# Output the result
print("Tour:", initial_tour)
print("Total travel cost:", current_cost)