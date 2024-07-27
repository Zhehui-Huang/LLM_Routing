import math
from typing import List, Tuple

def euclidean_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def initialize_distances(cities: List[Tuple[int, int]]) -> List[List[float]]:
    num_cities = len(cities)
    distances = [[0.0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

def nearest_neighbor_tour(start: int, cities_to_visit: List[int], distances: List[List[float]]) -> List[int]:
    tour = [start]
    unvisited = set(cities_to_visit)
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)  # returning to depot
    return tour

def calculate_tour_cost(tour: List[int], distances: List[List[float]]) -> float:
    cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return cost

def two_opt(tour: List[int], distances: List[List[float]]) -> List[int]:
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if distances[tour[i-1]][tour[i]] + distances[tour[j]][tour[j+1]] > distances[tour[i-1]][tour[j]] + distances[tour[i]][tour[j+1]]:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

def solve_mTSP(cities: List[Tuple[int, int]], num_robots: int) -> Tuple[List[List[int]], List[float]]:
    distances = initialize_distances(cities)
    num_cities = len(cities) - 1

    # Divide cities
    cities_per_robot = num_cities // num_robots
    assignments = []
    start_index = 1
    for r in range(num_robots):
        if r == num_robots - 1:
            assignments.append(list(range(start_index, num_cities + 1)))
        else:
            assignments.append(list(range(start_index, start_index + cities_per_robot)))
            start_index += cities_per_robot

    # Construct tours and improve them
    tours = []
    costs = []
    for r in range(num_robots):
        tour = nearest_neighbor_tour(0, assignments[r], distances)
        improved_tour = two_opt(tour, distances)
        tour_cost = calculate_tour_cost(improved_tour, distances)
        tours.append(improved_tour)
        costs.append(tour_cost)

    return tours, costs

def main():
    cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
              (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
              (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
              (61, 33), (62, 63), (63, 69), (45, 35)]
    num_robots = 2
    tours, costs = solve_mTSP(cities, num_robots)

    overall_cost = sum(costs)
    for r in range(num_robots):
        print(f"Robot {r} Tour: {tours[r]}")
        print(f"Robot {r} Total Travel Cost: {costs[r]}")
    print(f"Overall Total Travel Cost: {overall_cost}")

if __name__ == "__main__":
    main()