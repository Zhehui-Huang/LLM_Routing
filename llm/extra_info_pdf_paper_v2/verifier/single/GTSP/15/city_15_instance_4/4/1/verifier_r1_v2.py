import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, city_positions, city_groups):
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at the depot city (city 0)."

    visited_groups = set()
    for idx in range(1, len(tour) - 1):
        city = tour[idx]
        member = next((group for group, cities in enumerate(city_groups) if city in cities), -1)
        if member == -1:
            return False, f"City {city} is not in any group."
        if member in visited_groups:
            return False, f"Multiple cities from group {member} visited."
        visited_groups.add(member)
    
    if len(visited_groups) != len(city_groups):
        return False, "Not all city groups are visited exactly once."

    return True, "All constraints satisfied"

def calculate_total_travel_cost(tour, city_positions):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    return total_cost

def test_solution(tour, city_positions, city_groups):
    valid, message = validate_tour(tour, city_positions, city_groups)
    if not valid:
        return "FAIL", message
    
    total_travel_cost = calculate_total_travel_cost(tour, city_positions)
    return "CORRECT", f"Total Travel Cost: {total_travel_cost}"  # Corrected the reference to the variable name

# Mockup data of a given solution (Example tour is arbitrary and not the optimal solution)
city_positions = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), 
                  (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), 
                  (53, 80), (21, 21), (12, 39)]
city_groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]
example_tour = [0, 3, 4, 1, 6, 5, 7, 10, 0]  # Example tour of the robot

result, message = test_solution(example_tour, city_positions, city_groups)
print(result)
if result == "FAIL":
    print(message)