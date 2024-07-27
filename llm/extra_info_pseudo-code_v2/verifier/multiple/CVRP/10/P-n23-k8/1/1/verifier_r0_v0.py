import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def unit_tests():
    cities = {
        0: {'coord': (30, 40), 'demand': 0},
        1: {'coord': (37, 52), 'demand': 7},
        2: {'coord': (49, 49), 'demand': 30},
        3: {'coord': (52, 64), 'demand': 16},
        4: {'coord': (31, 62), 'demand': 23},
        5: {'coord': (52, 33), 'demand': 11},
        6: {'coord': (42, 41), 'demand': 19},
        7: {'coord': (52, 41), 'demand': 15},
        8: {'coord': (57, 58), 'demand': 28},
        9: {'coord': (62, 42), 'demand': 8},
        10: {'coord': (42, 57), 'demand': 8},
        11: {'coord': (27, 68), 'demand': 7},
        12: {'coord': (43, 67), 'demand': 14},
        13: {'coord': (58, 48), 'demand': 6},
        14: {'coord': (58, 27), 'demand': 19},
        15: {'coord': (37, 69), 'demand': 11},
        16: {'coord': (38, 46), 'demand': 12},
        17: {'coord': (61, 33), '(demand': 26)},
        18: {'coord': (62, 63), 'demand': 17},
        19: {'coord': (63, 69), 'demand': 6},
        20: {'coord': (45, 35), 'demand': 15},
        21: {'coord': (32, 39), 'demand': 5},
        22: {'coord': (56, 37), 'demand': 10}
    }
    robot_tours = [
        [0, 18, 19, 19, 13, 21, 0]
    ]
    robot_capacity = 40

    # Check correct tour starting and ending at depot
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL")
            return

    # Check demand fulfillment and capacity constraints
    all_cities_delivered = set()
    for tour in robot_tours:
        capacity_used = 0
        for i in range(1, len(tour) - 1):
            city = tour[i]
            capacity_used += cities[city]['demand']
            all_cities_delivered.add(city)
        if capacity_used > robot_capacity:
            print("FAIL")
            return

    # Every city except depot should be part of a delivery
    if len(all_cities_delivered) != len(cities) - 1:
        print("FAIL")
        return

    # Check total travel cost
    expected_total_cost = 96.82761762759218
    total_cost = 0
    for tour in robot_tours:
        tour_cost = 0
        for j in range(len(tour)-1):
            tour_cost += calculate_distance(cities[tour[j]]['coord'], cities[tour[j+1]]['coord'])
        total_cost += tour_cost

    # Allow small floating-point discrepancies
    if not math.isclose(total_cost, expected_total_cost, rel_tol=1e-5):
        print("FAIL")
        return

    print("CORRECT")

unit_tests()