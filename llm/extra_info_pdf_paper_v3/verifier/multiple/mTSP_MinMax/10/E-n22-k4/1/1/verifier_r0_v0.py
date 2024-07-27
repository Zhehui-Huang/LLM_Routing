import math

def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def verify_solution(tours, cities):
    # Verify each city is visited exactly once excluding depot
    visited = set()
    for tour in tours:
        for city in tour:
            if city != 0:
                if city in visited:
                    return False
                visited.add(city)
    if len(visited) != len(cities) - 1:
        return False
    
    # Verify all cities visited and tours start and end at the depot (city 0)
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return False
    
    # Verify the number of robots
    if len(tours) != 4:
        return False
    
    return True

def compute_costs(tours, city_coordinates):
    costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        costs.append(cost)
    
    max_cost = max(costs)
    return costs, max_cost

# City coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Provided robot tours solution
tours = [
    [0, 12, 14, 15, 16, 18, 0],
    [0, 3, 4, 6, 8, 10, 11, 0],
    [0, 13, 17, 19, 20, 21, 0],
    [0, 1, 2, 5, 7, 9, 0]
]

if verify_solution(tours, city_coordinates):
    costs, max_cost = compute_costs(tours, city_coordinates)
    print("CORRECT")
    for i, cost in enumerate(costs):
        print(f"Robot {i} Tour: {tours[i]}")
        print(f"Robot {i} Total Travel Cost: {cost}")
    print(f"Maximum Travel Cost: {max_cost}")
else:
    print("FAIL")