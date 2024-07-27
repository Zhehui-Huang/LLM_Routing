import math
import random

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# City groups
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(tour):
    """ Calculate the total cost of the given tour. """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean                                                                       istance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def generate_initial_tour():
    """ Generate a random initial tour visiting one city from each group. """
    tour = [0]  # start at depot
    for group in groups.values():
        tour.append(random.choice(group))  # choose random city from each group
    tour.append(0)  # end at depot
    return tour

def simulated_annealing(initial_tour):
    """ Perform simulated annealing to find a better solution. """
    current_tour = initial_tour[:]
    best_tour = current_tour[:]
    best_cost = calculate_tour_cost(current_tour)
    temperature = 100
    cooling_rate = 0.99
    
    while temperature > 1:
        # Create new tour as a neighbor of the current tour
        new_tour = current_tour[:]
        l = random.randint(1, len(new_tour) - 3)  # Random index of city to swap (not the depot)
        r = random.randint(1, len(new_tour) - 3)  # Another random index
        new_tour[l], new_tour[r] = new_tour[r], new_tour[l]  # Swap two cities
        
        current_cost = calculate_tour_cost(current_tour)
        new_cost = calculate_tour_cost(new_tour)
        cost_diff = new_cost - current_cost
        
        # Probability check to accept the new tour
        if cost_diff < 0 or random.random() < math.exp(-cost_diff / temperature):
            current_tour = new_tour[:]
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = new_tour[:]
        
        temperature *= cooling_rate

    return best_tour, best_cost

# Generate an initial tour and optimize it
initial_tour = generate_initial_tour()
optimized_tour, total_cost = simulated_annealing(initial_tour)

# Print the tour and its total cost
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost:.2f}")