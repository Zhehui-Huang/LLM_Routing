import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour_and_cost(tour, total_cost, city_group, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot."

    selected_groups = set()
    total_calculated_cost = 0

    for i in range(len(tour) - 1):
        # Calculate the distance for this leg of the journey
        city_index_a, city_index_b = tour[i], tour[i+1]
        total_calculated_cost += calculate_distance(cities[city_index_a], cities[city_index_b])

        # Check if city belongs to one of the groups only once
        for index, group in enumerate(city_group):
            if city_index_a in group:
                if index in selected_groups:
                    return "FAIL: City group visited more than once."
                selected_groups.add(index)

    if len(selected_groups) != len(city_group):
        return "FAIL: Not all city groups were visited."
    
    # Check if the tour total cost is correct
    if not math.isclose(total_calculated_cost, total_cost, rel_tol=1e-05):
        return f"FAIL: Provided cost is incorrect. Calculated cost: {total_calculated_cost}"

    return "CORRECT"

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40),
    4: (54, 42), 5: (36, 30), 6: (52, 82), 7: (93, 44),
    8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Grouping of cities
city_groups = [
    [8, 12, 14],  # Group 0
    [7, 10, 11],  # Group 1
    [4, 6, 9],    # Group 2
    [1, 3, 13],   # Group 3
    [2, 5]        # Group 4
]

# Input solution
tour = [0, 12, 10, 4, 3, 2, 0]
total_travel_cost = 138.15

# Verify solution
result = verify_tour_and_cost(tour, total_travel_cost, city_groups, cities)
print(result)