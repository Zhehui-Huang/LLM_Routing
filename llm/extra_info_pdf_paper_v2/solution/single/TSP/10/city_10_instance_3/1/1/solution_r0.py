import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def nearest_neighbour_tour(num_cities, distance_matrix):
    current_city = 0
    unvisited = set(range(1, num_cities))
    tour = [0]
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current_city][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(0)  # returning to the depot
    return tour

def two_opt_swap(tour, i, k):
    return tour[:i] + tour[i:k+1][::-1] + tour[k+1:]

def two_opt(tour, distance_matrix):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for k in range(i + 1, len(tour) - 1):
                new_tour = two_opt_swap(tour, i, k)
                if total_distance(new_tour, distance_matrix) < total_distance(tour, distance_matrix):
                    tour = new_tour
                    improvement = True
        if not improvement:
            break
    return tour

cities = [
    [84, 67],
    [74, 40],
    [71, 13],
    [74, 82],
    [97, 28],
    [0, 31],
    [8, 62],
    [74, 56],
    [85, 71],
    [6, 76]
]

num_cities = len(cities)
distance_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

initial_tour = nearest_neighbour_tour(num_cities, distance_matrix)
improved_tour = two_opt(initial_tour, distance_matrix)

cost = total_distance(improved_tour, distance_matrix)

result = {
    "Tour": improved_tour,
    "Total travel cost": cost
}

print("Tour:", result["Tour"])
print("Total travel cost:", result["Total travel cost"])