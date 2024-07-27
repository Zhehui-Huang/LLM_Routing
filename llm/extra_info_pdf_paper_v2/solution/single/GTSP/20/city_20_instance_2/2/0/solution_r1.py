import math

# Cities coordinates
cities = [
    (3, 26),   # Depot 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# Groups
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_optimal_tour():
    tour = [0]  # Start at depot
    
    # Choose one city from each group; simplest is to choose the first one, but let's choose the nearest to last city visited
    for group in groups:
        last_city_idx = tour[-1]
        last_city = cities[last_city_idx]
        
        # Find the closest city in the current group
        min_distance = float('inf')
        selected_city = group[0]
        for city_idx in group:
            distance = euclidean_data(last_city, cities[city_idx])
            if distance < min_distance:
                min_distance = distance
                selected_city = city_idx
        
        tour.append(selected_city)
    
    # Return to depot
    tour.append(0)
    
    # Calculate total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    return tour, total_cost

# Get the optimal tour and cost
optimal_tour, total_travel_cost = find_optimal_tour()

print('Tour:', optimal_tour)
print('Total travel cost:', total_travel_cost)