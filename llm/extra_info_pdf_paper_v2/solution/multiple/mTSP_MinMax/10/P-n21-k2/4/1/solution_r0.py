import math
from typing import List, Tuple

# Coordinates of cities, including the depot city at index 0
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_tour_cost(tour: List[int]) -> float:
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def initial_solution(n_robots: int, n_cities: int) -> List[List[int]]:
    tours = [[] for _ in range(n_robots)]
    
    # Distribute cities in a round-robin fashion
    for i in range(1, n_cities):
        tours[i % n_robots].append(i)
        
    return tours

def heuristic_minmax_mTSP(n_robots: int, cities: List[Tuple[int, int]]) -> Tuple[List[List[int]], List[float], float]:
    tours = initial_solution(n_robots, len(cities))
    changes = True
    
    while changes:
        changes = False
        # Calculate the best rearrangement of cities between tours to minimize maximum tour length
        current_max_cost = max([calculate_tour_cost([0] + tour + [0]) for tour in tours])

        for i in range(n_robots):
            for j in range(n_robots):
                if i != j:
                    for city in tours[i]:
                        # Try moving city from tour i to tour j
                        new_tour_i = tours[i][:]
                        new_tour_j = tours[j][:]
                        new_tour_i.remove(city)
                        new_tour_j.append(city)
                        
                        # Calculate new costs
                        new_cost_i = calculate_tour_cost([0] + new_tour_i + [0])
                        new_cost_j = calculate_tour_cost([0] + new_tour_j + [0])
                        new_max_cost = max(new_cost_i, new_cost_j, *[calculate_tour_cost([0] + tours[k] + [0]) for k in range(n_robots) if k != i and k != j])
                        
                        # If improvement, update tours
                        if new_max_cost < current_max_cost:
                            tours[i], tours[j] = new_tour_i, new_tour_j
                            current_max_cost = new_max_cost
                            changes = True
                            break
                if changes:
                    break
            if changes:
                break
    
    formatted_tours = [[0] + tour + [0] for tour in tours]
    costs = [calculate_tour_cost(tour) for tour in formatted_tours]
    max_cost = max(costs)
    
    return formatted_tours, costs, max_cost

# Solving the problem with 2 robots
tours, costs, max_cost = heuristic_minmax_mTSP(2, cities)

# Output results
for idx, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")
print(f"Maximum Travel Cost: {max_cost:.2f}")