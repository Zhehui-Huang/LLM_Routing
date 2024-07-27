import math

# Coordinates of the depot and the cities
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Calculating the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def find_tour():
    n = len(coordinates)
    unvisited = set(range(1, n))
    tour = [0]
    max_distance = 0
    
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distance(last, x))
        tour_distance = distance(last, next_city)
        max_distance = max(max_distance, tour_distance)
        tour.append(next_city)
        unvisited.remove(next_city)
        
    # Close the tour by returning to starting point, the depot
    final_leg_distance = distance(tour[-1], 0)
    max_distance = max(max_distance, final_leg_distance)
    tour.append(0)
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

# Get the best tour details
best_tour, total_cost, max_consecutive_distance = find_tour()

# Display the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")