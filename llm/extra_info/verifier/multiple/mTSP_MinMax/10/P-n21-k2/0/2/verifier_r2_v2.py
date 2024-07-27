import math

# Coordinates of cities including the depot
city_coords = [
    (30, 40),  # Depot city 0
    (37, 52),
    (49, 49),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 48),
    (58, 27),
    (37, 69),
    (38, 46),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35)
]

def calculate_distance(city1, city2):
    (x1, y1) = city_coords[city1]
    (x2, y2) = city_coords[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_distances(tours):
    costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour)-1):
            cost += calculate_distance(tour[i], tour[i+1])
        costs.append(cost)
    return costs

def test_solution():
    tours = [
        [0, 1, 3, 4, 8, 10, 11, 12, 15, 18, 19, 0],
        [0, 2, 5, 6, 7, 9, 13, 14, 16, 17, 20, 0]
    ]
    costs = verify_tour_distances(tours)
    actual_cost_robot_0 = 212
    actual_cost_robot_1 = 184
    max_cost = 212

    passed = True
    passed &= costs[0] == actual_cost_robot_0
    passed &= costs[1] == actual_search_robot_1
    passed &= max(costs) == max_cost

    all_tours_flat = [city for tour in tours for city in tour if city != 0]
    passed &= len(set(all_tours_flat)) == 20  # Checking for 20 cities excluding depot
    passed &= len(all_tours_flat) == 20  # No city is visited more than once

    passed &= all(tour[0] == 0 and tour[-1] == 0 for tour in tours)  # Start and end at depot

    if passed:
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    test_solution()