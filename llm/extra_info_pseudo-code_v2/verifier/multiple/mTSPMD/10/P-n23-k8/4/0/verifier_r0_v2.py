import numpy as np

# Define city coordinates for calculating distances
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
    21: (32, 39), 22: (56, 37)
}

# Define the tours undertaken by each robot and their alleged costs
robot_data = {
    0: ([0, 21, 20, 14, 17, 22, 9, 13, 8, 18, 19, 12, 15, 11, 10, 16, 0], 159.22),
    1: ([1, 16, 21, 20, 14, 17, 22, 9, 13, 8, 18, 19, 12, 15, 11, 10, 1], 157.65),
    2: ([2, 16, 21, 20, 14, 17, 22, 9, 13, 8, 18, 19, 12, 15, 11, 10, 2], 166.53),
    3: ([3, 12, 15, 11, 10, 16, 21, 20, 14, 17, 22, 9, 13, 8, 18, 19, 3], 156.89),
    4: ([4, 14, 17, 22, 9, 13, 8, 18, 19, 12, 15, 11, 10, 16, 21, 20, 4], 156.70),
    5: ([5, 14, 17, 22, 9, 13, 8, 18, 19, 12, 15, 11, 10, 16, 21, 20, 5], 159.51),
    6: ([6, 20, 14, 17, 22, 9, 13, 8, 18, 19, 12, 15, 11, 10, 16, 21, 6], 163.53),
    7: ([7, 22, 17, 14, 9, 13, 8, 18, 19, 12, 15, 11, 10, 16, 21, 20, 7], 159.87)
}

overall_cost_reported = 1277.70

def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def verify_tour(tour, start_end):
    # Verify start and end at the correct depot
    if tour[0] != start_end or tour[-1] != start_end:
        return False
    # Verify consecutive city distance calculation
    tour_length = sum(euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    return tour_length

verified_data = {}
total_calculated_cost = 0.0

for robot, (tour, reported_cost) in robot_data.items():
    calculated_cost = verify_tour(tour, robot)
    if calculated_cost is False:
        print(f"Robot {robot} failed verification: Incorrect start or end city.")
    else:
        total_calculated_cost += calculated_cost
        verified_data[robot] = {
            "Tour length matches": np.isclose(calculated_cost, reported_cost, atol=0.01),
            "Reported cost": reported_cost,
            "Calculated cost": calculated_cost
        }

# Output verified results
for robot, data in verified_data.items():
    print(f"Robot {robot} verification: {data}")

# Check overall cost
if np.isclose(total_calculated_cost, overall_cost_reported, atol=0.01):
    print("Overall cost verification: CORRECT")
else:
    print(f"Overall cost verification: FAIL. Reported: {overall_cost_reported}, Calculated: {total_calculated_cost}")