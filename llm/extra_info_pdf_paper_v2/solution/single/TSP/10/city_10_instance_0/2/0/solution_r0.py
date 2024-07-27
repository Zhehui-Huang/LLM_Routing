import math

# Define the coordinates of each city
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Construct an initial path (simple and naive solution, e.g., nearest neighbor heuristic)
def initial_solution(depot, cities):
    unvisited = list(cities.keys())
    unvisited.remove(depot)
    path = [depot]
    current_city = depot
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        path.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
        
    path.append(depot) # return to depot city
    return path

# Calculate the total cost of a tour
def calculate_total_cost(path):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += calculate_distance(path[i], path[i+1])
    return total_cost

# Potential improvement function (for simplicity using a naive two-opt swap heuristic iteration)
def improve_solution(path):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path) - 1):
                if calculate_distance(path[i - 1], path[i]) + calculate_distance(path[j], path[j + 1]) > \
                   calculate_distance(path[i - 1], path[j]) + calculate_distance(path[i], path[j + 1]):
                    path[i:j+1] = path[i:j+1][::-1]
                    improved = True
    return path

# Main process function to find the shortest tour
def find_shortest_tour():
    initial_path = initial_solution(0, cities)
    improved_path = improve_solution(initial_path)
    total_cost = calculate_total_cost(improved_path)
    return improved_path, total_cost

# Find the shortest tour and total travel cost
tour, total_cost = find_shortest_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)