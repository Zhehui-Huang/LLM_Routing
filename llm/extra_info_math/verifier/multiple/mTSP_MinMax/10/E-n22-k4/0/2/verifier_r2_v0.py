import numpy as np

# Data for the solution
tours = [
    [0, 1, 5, 9, 13, 17, 21, 0],
    [0, 2, 6, 10, 14, 18, 0],
    [0, 3, 7, 11, 15, 19, 0],
    [0, 4, 8, 12, 16, 20, 0]
]

# Using a set to check if all cities are visited exactly once
visited_cities = set()
for tour in tours:
    visited_cities.update(tour[1:-1])  # not including the depot in the middle of the tour

# Check if each city is visited exactly once
def check_cities_visited_once():
    return len(visited_cities) == 21  # There are 21 cities excluding the depot

# Check flow conservation for each robot tour
def check_flow_conservation():
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:  # check if each tour starts and ends at the depot
            return False
        for idx in range(1, len(tour) - 1):
            if tour[idx] in tour[idx+1:]:  # check if any city in the tour appears more than once
                return False
    return True

# Check if each salesman starts from and returns to the depot
def check_depot_visitation():
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return False
    return True

# Check if any subtour exists that doesn't include depot
def check_subtour_elimination():
    for tour in tours:
        depot_indices = [i for i, x in enumerate(tour) if x == 0]
        if len(depot_indices) != 2 or depot_indices != [0, len(tour)-1]:
            return False
    return True

# Execute checks
if (check_cities_visited_once()
    and check_flow_conservation()
    and check_depot_visitation()
    and check_subtour_elimination()):
    print("CORRECT")
else:
    print("FAIL")