import math

# Given city coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Tours described in the solution
robot_tours = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]

# Function to calculate Euclidean distance
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Check if each city is visited once
visited_cities = [0] * 16
try:
    for tour in robot_tours:
        for i in range(len(tour) - 1):  # Iterating till the second last element
            city = tour[i]
            visited_cities[city] += 1
            if i == 0:  # Start depot check
                if tour[i] != 0:
                    raise Exception("Tours should start from the designated depot, which is depot city 0.")
            if calculate_distance(cities[tour[i]], cities[tour[i+1]]) == 0 and i < len(tour) - 2:
                raise Exception("Distance calculation error or repetitive non-contributive movement.")
except Exception as e:
    print("FAIL:", e)
    exit()

# Check uniqueness and complete visitation
if any(count != 1 for count in visited_cities):
    print("FAIL: Not all cities are visited exactly once.")
    exit()

# If everything is okay
print("CORRECT")