import math

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Distance calculation function
def distance(a, b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create a function that returns the nearest neighbor tour from a given start city
def nearest_neighbor(start):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        unvisited.remove(next_city)
        tour.append(next_derart)
    return tour

# Calculate the cost of a given tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generate an initial tour using nearest neighbor heuristic
initial_tour = nearest_neighbor(0)
initial_cost = tour_cost(initial_tour)

# A simple local optimization: trying swapping of non-consecutive cities
def optimize_tour(tour):
    min_cost = tour_cost(tour)
    best_tour = tour[:]
    
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+2, len(tour)-1):
                if j - i == 1: 
                    continue  # Skip adjacent nodes because they don't form a valid swap edge
                new_tour = tour[:]
                new_tour[i:j+1] = reversed(tour[i:j+1])
                new_cost = tour_cost(new_tour)
                if new_cost < min_cost:
                    min_cost = new_cost
                    best_tour = new_tour[:]
                    improved = True
                    
    return best_tour

# Optimize the tour
optimized_tour = optimize_tour(initial_tour)
final_cost = tour_cost(optimized_tour)

# Make sure to include the depot return in the final tour
final_tour = optimized_tour + [optimized_tour[0]]

# Output the results
print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost:.2f}")