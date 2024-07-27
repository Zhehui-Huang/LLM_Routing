import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def construct_full_distance_matrix(coords):
    num_cities = len(coords)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean_distance(coords[i], coords[j])
    return distances

def select_cities_to_visit(distances, num_cities_to_visit, start_city):
    # Greedy heuristic to select cities closest to the start city
    num_cities = len(distances)
    selected = [False] * num_cities
    tour = [start_city]
    selected[start_city] = True
    
    current_city = start_city
    while len(tour) < num_cities_to_visit:
        next_city = None
        min_dist = float('inf')
        for city in range(num_cities):
            if not selected[city] and distances[current_city][city] < min_dist:
                next_city = city
                min_dist = distances[current_city][city]
        if next_city is not None:
            tour.append(next_city)
            selected[next_city] = True
            current_city = next_city

    return tour

def find_tour(distances, city_order):
    tour = city_order[:] + [city_order[0]]  # return to the start
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distances[tour[i]][tour[i + 1]]
    return tour, total_cost

def main():
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
        (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
        (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
        (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]

    distances = construct_full_distance_matrix(cities)
    num_cities_to_visit = 16
    
    selected_cities = select_cities_to_visit(distances, num_cities_to_visit, 0)
    tour, total_cost = find_tour(distances, selected_cities)
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")

main()