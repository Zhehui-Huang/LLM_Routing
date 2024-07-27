import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_tour(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    
    current_city = 0
    while len(tour) < n:
        closest_city = None
        shortest_distance = float('inf')

        for i in range(n):
            if not visited[i]:
                distance = euclidean_distance(cities[current_city], cities[i])
                if distance < shortest_distance:
                    closest_city = i
                    shortest_distance = distance

        visited[closest_city] = True
        tour.append(closest_city)
        current_city = closest_city

    tour.append(0)  # Return to the depot
    
    return tour

def calculate_tour_cost_and_max_distance(cities, tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return total_cost, max_distance

# Define cities given in the problem
cities = [
    (79, 15), # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Find a tour using the greedy approach
tour = find_tour(cities)

# Calculate the total travel cost and the maximum distance between consecutive cities
total_cost, max_distance = calculate_tour_cost_and_max_distance(cities, tour)

# Output the required results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")