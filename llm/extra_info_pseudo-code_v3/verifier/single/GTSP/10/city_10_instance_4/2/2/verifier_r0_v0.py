import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    cities = {
        0: (79, 15),  # Depot
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }
    
    groups = {
        0: [1, 4],
        1: [2, 6],
        2: [7],
        3: [5],
        4: [9],
        5: [8],
        6: [3]
    }
    
    tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
    reported_total_cost = 371.19
    
    # Check if tour starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL - Tour does not start and end at the depot."
    
    # Check groups
    visited_groups = set()
    for i in range(1, len(tour) - 1):
        city_id = tour[i]
        found_group = False
        for group_id, group_cities in groups.items():
            if city_id in group_cities:
                if group_id in visited_groups:
                    return f"FAIL - Group {group_id} visited more than once."
                visited_groups.add(group_id)
                found_group = True
                break
        if not found_group:
            return f"FAIL - City {city_id} not found in any group."
    
    # Check if all groups are visited
    if visited_groups != set(groups.keys()):
        return "FAIL - Not all groups are visited."
    
    # Check tour total cost
    total_cost = 0
    for j in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[j]], cities[tour[j + 1]])
    
    # Allow small floating-point arithmetic discrepancies
    if not math.isclose(total_cost, reported_total_cost, rel_tol=1e-3):
        return f"FAIL - Reported cost is incorrect. Calculated: {total_cost}, Reported: {reported_total_today}"
    
    return "CORRECT"

# Check the correctness of the solution
print(test_solution())