import math

# City coordinates and demands
cities = {
    0: {'coord': (30, 40), 'demand': 0},
    1: {'coord': (37, 52), 'demand': 19},
    2: {'coord': (49, 49), 'demand': 30},
    3: {'coord': (52, 64), 'demand': 16},
    4: {'coord': (31, 62), 'demand': 23},
    5: {'coord': (52, 33), 'demand': 11},
    6: {'coord': (42, 41), 'demand': 31},
    7: {'coord': (52, 41), 'demand': 15},
    8: {'coord': (57, 58), 'demand': 28},
    9: {'coord': (62, 42), 'demand': 8},
    10: {'coord': (42, 57), 'demand': 8},
    11: {'coord': (27, 68), 'demand': 7},
    12: {'coord': (43, 67), 'demand': 14},
    13: {'coord': (58, 48), 'demand': 6},
    14: {'coord': (58, 27), 'demand': 19},
    15: {'coord': (37, 69), 'demand': 11}
}
robot_capacity = 35

# Robot tours
robot_tours = [
    [0, 6, 0],
    [0, 1, 10, 13, 0],
    [0, 2, 0],
    [0, 4, 11, 0],
    [0, 7, 5, 9, 0],
    [0, 15, 12, 0],
    [0, 14, 3, 0],
    [0, 8, 0]
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Check each requirement
def test_tours():
    visited = set()
    total_system_cost = 0.0
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Robot tour does not start/end at depot."
        
        tour_cost = 0.0
        tour_demand = 0
        
        for i in range(len(tour) - 1):
            from_city = tour[i]
            to_city = tour[i + 1]
            visited.add(to_city)
            
            # Calculate travel cost
            distance = euclidean_distance(cities[from_city]['coord'], cities[to_city]['coord'])
            tour_cost += distance
            
            # Sum demands
            if to_city != 0:
                tour_demand += cities[to_city]['demand']
                
        total_system_cost += tour_cost
        
        # Capacity check
        if tour_demand > robot_capacity:
            return "FAIL: Robot tour exceeds capacity."
    
    # Check if all cities are visited exactly once
    if len(visited) != len(cities) - 1:  # minus 1 because depot (city 0) is not in visited list
        return "FAIL: Not all cities are visited exactly once."

    # If everything passes
    return "CORRECT"

# Run the test
result = test_tours()
print(result)