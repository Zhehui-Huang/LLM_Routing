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

# Function to calculate a tour starting at the depot
def nearest_neighbor(start=0):
    unvisited = set(cities) - {start}
    tour = [start]
    
    while unvisited:
        nearest = min(unvisited, key=lambda city: distance(tour[-1], city))
        tour.append(nearest)
        unvisited.remove(nearest)
    
    tour.append(start)  # Return to the depot
    return tour

# Calculate the cost of the tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate initial tour
initial_tour = nearest_neighbor()
initial_cost = calculate_tour_cost(initial_tour)

# Output initial configuration and cost
print("Initial Tour:", initial_tour)
print("Initial Tour Cost:", initial_cost)

# Let's attempt an optimization
def optimize_tour(tour):
    improved = True
    while improved:
        improved = False
        # Try swapping every pair of non-adjacent edges/cities
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if j != len(tour) -1 or i != 1:
                    new_tour = tour[:]
                    new_tour[i:j] = reversed(tour[i:j])  # reverse the segment between i and j
                    new_cost = calculate_tour_cost(new_tour)
                    if new_cost < calculate_tour_cost(tour):
                        tour = new_tour
                        improved = True
    return tour

# Optimize the tour
optimized_tour = optimize_tour(initial_tour)
optimized_cost = calculate_tour_cost(optimized_tour)

# Output the solution
print("Optimized Tour:", optimized_tour)
print("Optimized Tour Cost:", optimized_cost)