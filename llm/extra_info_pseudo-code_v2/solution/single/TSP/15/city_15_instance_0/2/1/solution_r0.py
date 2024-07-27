import math
import random

# Coordinates for the depot and cities
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initialize the tour
initial_tour = list(cities.keys())
random.shuffle(initial_tour)
initial_tour.remove(0)
initial_tour = [0] + initial_tour + [0]

def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def simulated_annealing(tour, initial_temp=1000, cooling_rate=0.995, num_iterations=1000):
    current_temp = initial_temp
    current_tour = tour[:]
    best_tour = tour[:]
    best_cost = tour_cost(tour)
    
    for _ in range(num_iterations):
        current_temp *= cooling_rate

        new_tour = current_tour[:]
        l = random.randint(1, len(new_tour) - 3)
        r = random.randint(l + 1, len(new_tour) - 2)
        new_tour[l:r] = reversed(new_tour[l:r])
        
        current_cost = tour_cost(current_tour)
        new_cost = tour_cost(new_tour)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / current_temp):
            current_tour = new_tour[:]
            if new_cost < best_cost:
                best_tour = new_tour[:]
                best_cost = new_cost

    return best_tour, best_cost

# Calculate the optimized tour and its cost
optimized_tour, optimized_cost = simulated_annealing(initial_tour)

# Output the results
print("Tour:", optimized_tour)
print("Total travel cost:", round(optimized_cost, 2))