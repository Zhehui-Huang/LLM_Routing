import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
cities = {
    0: (9, 93),
    # Group 0
    2: (74, 99), 7: (63, 23), 10: (19, 65), 11: (11, 40), 14: (4, 39),
    # Group 1
    1: (8, 51), 3: (78, 50), 5: (88, 59), 8: (19, 76), 13: (60, 55),
    # Group 2
    4: (21, 23), 6: (79, 77), 9: (21, 38), 12: (3, 21)
}

groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

def find_representatives():
    representatives = [0]  # Starting and ending at depot city 0
    for group in groups.values():
        closest_city = None
        min_distance = float('inf')
        for city in group:
            distance = euclidean_distance(cities[0], cities[city])
            if distance < min_distance:
                min_distance = distance
                closest_city = city
        representatives.append(closest_city)
    return representatives

def find_optimal_tour(representatives):
    # Start with the simple insertion heuristic to form a basic tour
    tour = [representatives[0]]
    unvisited = representatives[1:]
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[tour[-1]], cities[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(representatives[0])  # Return to depot
    return tour

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_distance

# Sequential algorithm execution
representatives = find_representatives()
tour = find_optimal_tour(representatives)
total_distance = calculate_total_distance(tour)

# Display results
print("Tour:", tour)
print("Total travel cost:", round(total_distance, 2))