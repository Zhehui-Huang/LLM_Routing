import math

# city coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23), (19, 76), 
          (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Greedy approach to find a feasible initial tour minimizing the bottleneck distance
def find_initial_tour(cities):
    num_cities = len(cities)
    unvisited = list(range(1, num_cities))
    tour = [0]  # start from depot
    last_city = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[last_city], cities[x]))
        tour.append(next_city)
        last_city = next_city
        unvisited.remove(next_city)

    tour.append(0)  # return to depot
    return tour

# Analyze the tour to calculate total cost and maximum distance between consecutive cities
def analyze_tour(tour, cities):
    max_distance = 0
    total_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

# Generate initial tour
initial_tour = find_initial_tour(cities)

# Analyze the initial tour
total_cost, max_consecutive_distance = analyze_tour(initial_tour, cities)

# Outputs
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_consecutive_distance, 2)}")