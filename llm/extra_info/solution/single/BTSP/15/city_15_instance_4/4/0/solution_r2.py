import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor_tour(cities):
    num_cities = len(cities)
    unvisited = list(range(1, num_cities))
    tour = [0]
    current_city = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(0)  # Return to the depot
    return tour

def calculate_tour_information(tour, cities):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return total_cost, max_distance

def two_opt(tour, cities, max_iterations=1000):
    for _ in range(max_iterations):
        found_improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                # Calculate the current distances
                old_dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]]) + \
                           euclidean_distance(cities[tour[j]], cities[tour[j+1]])
                # Calculate the proposed new distances
                new_dist = euclidean_distance(cities[tour[i-1]], cities[tour[j]]) + \
                           euclidean_distance(cities[tour[i]], cities[tour[j+1]])
                # If the new total distance is less, perform the swap
                if new_dist < old_dist:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    found_improvement = True
                    break
            if found_improvement:
                break
        if not found_improvement:
            break
    return tour

# Define the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Get the tour using the Nearest Neighbor heuristic
initial_tour = nearest_neighbor_tour(cities)

# Optimize the tour with the 2-Opt algorithm
optimized_tour = two_opt(initial_tour, cities)

# Calculate the cost and max distance
total_cost, max_distance = calculate_tour_information(optimized_tour, cities)

# Output the results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")