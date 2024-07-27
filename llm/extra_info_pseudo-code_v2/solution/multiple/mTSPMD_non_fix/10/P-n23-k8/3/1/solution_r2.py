import random
import math
from typing import List, Tuple

# Coordinates for each city including depots
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

def euclidean_distance(city1: int, city2: int) -> float:
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def initialize_population(pop_size: int, num_cities: int, num_robots: int) -> List[List[int]]:
    population = []
    for _ in range(pop_size):
        tour = list(range(8, num_cities))  # including depots initially only for the first city
        random.shuffle(tour)
        tour = [0] + tour  # Start each at the first depot
        partition_sizes = random_partition(len(tour) - 1, num_robots)
        new_individual = []
        index = 1
        
        for size in partition_sizes:
            new_individual.extend(tour[index:index + size])
            index += size
            if index < len(tour):
                new_individual.append(-(len(new_individual) // len(partition_sizes)))
        
        population.append(new_individual)
    return population

def random_partition(total_cities: int, num_robots: int) -> List[int]:
    partitions = [1] * num_robots
    for _ in range(total_cities - num_robots):
        partitions[random.randint(0, num_robots - 1)] += 1
    return partitions

def decode_solution(solution: List[int], num_robots: int) -> List[Tuple[List[int], int]]:
    tours = []
    current_tour = []
    current_depot = 0
    
    for city in solution:
        if city >= 0:
            current_tour.append(city)
        else:
            tours.append((current_tour, current_depot))
            current_depot = abs(city) % 8  # Determine new depot, feeded by the chromosome structure
            current_tour = [current_depot]
    
    if current_tour:
        tours.append((current_tour, current_depot))
    
    return tours

def calculate_tours_length(tours: List[Tuple[List[int], int]]) -> Tuple[List[float], float]:
    total_costs = []
    overall_cost = 0
    
    for tour, depot in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(tour[i], tour[i+1])
        total_costs.append(cost)
        overall_cost += cost
    
    return total_costs, overall_cost

def main():
    num_cities = len(cities)
    num_robots = 8
    population_size = 100
    
    population = initialize_population(population_size, num_cities, num_robots)

    for individual in population:
        tours = decode_solution(individual, num_robots)
        tour_costs, total_cost = calculate_tours_length(tours)
        for i, (tour, cost) in enumerate(zip(tours, tour_costs)):
            print(f"Robot {i} Tour: {[cities[idx] for idx, _ in tour]}")
            print(f"Robot {i} Total Travel Cost: {cost}")
        print(f"Overall Total Travel Cost: {total_cost}")

if __name__ == '__main__':
    main()