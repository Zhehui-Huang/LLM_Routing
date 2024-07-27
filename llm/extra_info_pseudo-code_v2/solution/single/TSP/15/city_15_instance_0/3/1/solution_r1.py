import math

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def get_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function for calculating total tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += get_distance(tour[i], tour[i + 1])
    return cost

# Simple nearest neighbor tour from the depot
def generate_initial_tour(depot=0):
    visited = {depot}
    tour = [depot]
    current_city = depot

    while len(visited) < len(cities):
        next_city = min((city for city in cities if city not in visited), 
                        key=lambda city: get_distance(current_city, city))
        tour.append(next_city)
        visited.add(next_city)
        current_city = next_city

    tour.append(depot)  # return to the starting city
    return tour

# Applying 2-opt swap to optimize the tour
def apply_two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1:
                    continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour) < calculate_tour_cost(tour):
                    tour = new_tour
                    improved = True
        if not improved:
            break
    return tour

# Generate initial tour and optimize it
initial_tour = generate_initial_tour()
optimized_tour = apply_two_opt(initial_tour)
total_cost = calculate_tour_cost(optimized_tour)

# Output the optimized tour and the corresponding travel cost
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost:.2f}")