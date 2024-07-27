import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    cities = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
        4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
        8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
        12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
        16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
        20: (155, 185), 21: (139, 182)
    }

    demands = {
        1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400, 7: 800, 
        8: 100, 9: 500, 10: 600, 11: 1200, 12: 1300, 13: 1300, 
        14: 300, 15: 900, 16: 2100, 17: 1000, 18: 900, 19: 2500, 
        20: 1800, 21: 700
    }

    robot_tours = [
        [0, 14, 16, 17, 20, 21, 8, 0],
        [0, 12, 15, 18, 19, 6, 0],
        [0, 13, 11, 10, 9, 7, 2, 3, 0],
        [0, 5, 1, 4, 0]
    ]

    max_capacity = 6000
    visited_cities = set()
    
    # Check demand constraint
    total_demands = {city: 0 for city in demands}
    
    # Check routes start and end at depot, capacity and demand constraints
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL: Tour must start and end at the depot.")
            return

        load = 0
        for i in range(1, len(tour) - 1):
            city = tour[i]
            visited_cities.add(city)
            load += demands[city]
            total_demands[city] += demands[city]

        if load > max_capacity:
            print("FAIL: Exceeded robot capacity.")
            return

    # Check if all cities are visited and demands met
    if visited_cities != set(demands.keys()):
        print("FAIL: Not all cities were visited.")
        return

    for city, total in total_demands.items():
        if total != demands[city]:
            print("FAIL: City demands not met fully.")
            return

    print("CORRECT")

test_solution()