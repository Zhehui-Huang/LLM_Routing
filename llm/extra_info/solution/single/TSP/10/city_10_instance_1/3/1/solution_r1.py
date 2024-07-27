import math

# City coordinates with city index as key
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

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def nearest_neighbor():
    """Nearest Neighbor algorithm to solve the TSP."""
    unvisited = list(cities.keys())[1:]
    tour = [0]
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda c: calculate_distance(current_city, c))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(0)  # return to the depot city
    
    return tour

def calculate_tour_cost(tour):
    """Calculate the total travel cost of the tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

# Solve the TSP
tour = nearest_neighbor()

# Calculate the cost of the tour
total_cost = calculate_tour_cost(tour)

# Output the required format
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")