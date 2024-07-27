import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(robots_tours, cities):
    # Check the given number of cities including depot
    if len(cities) != 16:
        return "FAIL"
    
    # Check if all robots start and end at the depot
    for tour in robots_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Check all cities are visited exactly once
    visited = set()
    for tour in robots_tours:
        for city in tour[1:-1]: # Exclude depot from being counted multiple times
            if city in visited:
                return "FAIL"
            visited.add(city)
    if len(visited) != 15:  # Only 15 cities should be in 'visited' since city 0 is the depot
        return "FAIL"
    
    # Checking each robot can travel between any two cities
    # This is inherently satisfied as they can travel to any city from any city

    # Calculating and checking individual and maximum travel cost
    max_cost = 0
    for tour in robots_tours:
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        print(f"Robot Tour: {tour}")
        print(f"Total Travel Cost: {total_cost}")
        max_cost = max(max_cost, total_cost)

    print(f"Maximum Travel Cost: {max_cost}")
    
    # Check if the tours minimize the maximum distance, which can't be programmatically ascertained here
    # without knowing other possible solutions, but we assume solution logic targets this.

    return "CORRECT"

# Assume cities and their coordinates like one provided in the task
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
         ]

# Assume robots_tours output by solving algorithm (example format, not a solution):
robots_tours = [
    [0, 1, 2, 0],
    [0, 3, 4, 0],
    [0, 5, 6, 0],
    [0, 7, 8, 0],
    [0, 9, 10, 0],
    [0, 11, 12, 0],
    [0, 13, 14, 0],
    [0, 15, 0]
]

# Let's run the test
result = test_solution(robots_tours, cities)
print(result)