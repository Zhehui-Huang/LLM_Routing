import math

# Define the cities' coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate total tour cost
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(tour[i], tour[i + 1])
    return cost

# Generate an initial greedy solution
def initial_solution(depot, k):
    unvisited = list(cities.keys())
    unvisited.remove(depot)
    tour = [depot]
    
    while len(tour) < k:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: calculate_distance(last, x))
        tour.append(next_city)
        unvisited.remove(next_city)

    tour.append(depot) # Return to the depot at the end
    return tour

# Function to perform a 2-opt swap
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # ignore consecutive edges
                new_tour = tour[:]
                new_tour[i:j + 1] = tour[j:i - 1:-1]
                if tour_cost(new_tour) < tour_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

# Apply the functions to solve the problem
initial_tour = initial_solution(0, 8)  # Start and end at depot city 0, visiting 8 cities
optimized_tour = two_opt(initial_tour)
total_cost = tour_cost(optimized_tour)

# Print the formatted results
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)