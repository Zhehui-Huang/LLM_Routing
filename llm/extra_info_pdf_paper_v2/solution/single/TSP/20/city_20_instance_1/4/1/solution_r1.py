import math

def calculate_distance(city_a, city_b):
    x1, y1 = city_coords[city_a]
    x2, y2 = city_coords[city_b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def initial_tour():
    cities = list(range(1, len(city_coords)))  # exclude the depot city for initial path
    tour = [0]  # start at the depot
    current_city = 0
    while cities:
        # Find the nearest unvisited city
        nearest_city = min(cities, key=lambda city: calculate_distance(current_city, city))
        tour.append(nearest_city)
        cities.remove(nearest_city)
        current_city = nearest_city
    tour.append(0)  # return to the depot
    return tour

def improve_tour(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 2, len(tour) - 1):
                if calculate_distance(tour[i - 1], tour[i]) + calculate_distance(tour[j], tour[j + 1]) > calculate_distance(tour[i - 1], tour[j]) + calculate_distance(tour[i], tour[j + 1]):
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improved = True
    return tour

# Fixed the definition of city coordinates based on the provided data
city_coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Calculate tour and improve using a simple heuristic
initial_path = initial_tour()
improved_path = improve_tour(initial_path)
total_cost = sum(calculate_distance(improved_path[i], improved_path[i+1]) for i in range(len(improved_path) - 1))

# Output the solution
print("Tour:", improved_path)
print("Total travel cost:", total_cost)