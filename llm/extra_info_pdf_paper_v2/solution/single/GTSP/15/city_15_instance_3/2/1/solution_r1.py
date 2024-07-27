import math
import random

# Coordinates for each city
coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Groups of cities to be visited by the robot
groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to calculate total travel cost of a given tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Function to generate an initial feasible tour
def generate_initial_tour():
    tour = [0]  # start at the depot
    for group in groups:
        tour.append(random.choice(group))  # pick a random city from each group
    tour.append(0)  # end at the depot
    return tour

# Simulated annealing to find a better solution
def simulated_annealing(initial_tour, max_iterations=1000, start_temp=1000, end_temp=1, cooling_factor=0.995):
    current_tour = initial_tour
    current_cost = calculate_tour_cost(current_tour)
    temp = start_temp
    
    while temp > end_temp:
        for _ in range(max_iterations):
            # Generate a new candidate solution
            new_tour = current_tour[:]
            group_index = random.randint(1, len(groups) - 1)
            new_tour[group_index] = random.choice(groups[group_index - 1])
            
            new_cost = calculate_tour_cost(new_tour)
            
            # Decide whether to accept the new solution
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                current_tour, current_cost = new_tour, new_cost
        
        # Cool down
        temp *= cooling_factor

    return current_tour, current_cost

# Main execution
initial_tour = generate_initial_tour()
optimized_tour, optimized_cost = simulated_annealing(initial_tour)

# Results
print("Tour:", optimized_tour)
print("Total travel cost:", optimized_cost)