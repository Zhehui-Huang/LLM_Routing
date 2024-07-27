import math

# Define the function to calculate the Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the cities' coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 192), (129, 189), 
    (155, 185), (139, 182)
]

# Define the tours provided
tours = [
    [0, 14, 16, 12, 15, 18, 0],
    [0, 10, 8, 6, 3, 4, 11, 0],
    [0, 13, 19, 21, 17, 20, 0],
    [0, 9, 7, 5, 2, 1, 0]
]

# Check Requirement 1: Each city visited exactly once excluding depot
visited_cities = set()
for tour in tours:
    for city in tour:
        if city != 0:  # Exclude depot from checking unique visit
            if city in visited_cities:
                print("FAIL")
                exit()
            visited_cities.add(city)
if len(visited_cities) != 21:  # 21 cities excluding depot
    print("FAIL")
    exit()

# Check Requirement 2: Each robot starts and ends at the depot
for tour in tours:
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL")
        exit()

# Check Requirement 3: Minimize the maximum distance traveled by any robot
calculated_max_distance = 0
for tour in tours:
    tour_distance = 0
    for i in range(len(tour) - 1):
        tour_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    calculated_max_distance = max(calculated_max_distance, tour_distance)

# Compare calculated maximum distance with the given value
if math.isclose(calculated_max_distance, 111.83855721201843, rel_tol=1e-5):
    print("CORRECT")
else:
    print("FAIL")