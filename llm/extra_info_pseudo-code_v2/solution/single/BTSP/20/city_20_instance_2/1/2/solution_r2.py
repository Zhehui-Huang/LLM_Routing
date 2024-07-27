import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def find_tour(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    current_city = 0

    # Nearest Neighbor heuristic implementation
    for _ in range(1, n):
        nearest_distance = float('inf')
        nearest_city = None
        for i in range(n):
            if not visited[i]:
                distance = euclidean_distance(cities[current_city], cities[i])
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_city = i
        current_city = nearest_city
        visited[current_city] = True
        tour.append(current_city)
    
    # Close the tour by returning to the starting point
    tour.append(0)
    return tour

def calculate_metrics(tour, cities):
    total_distance = 0
    max_segment_distance = 0
    for i in range(len(tour) - 1):
        segment_distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_distance += segment_distance
        if segment_distance > max_segment_distance:
            max_segment_distance = segment_distance
    return total_distance, max_segment_distance

# Define the cities based on the coordinates provided
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92),
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Find a tour and calculate its costs
tour = find_tour(cities)
total_cost, max_distance = calculate_metrics(tour, cities)

# Output the desired metrics and tour
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")