import numpy as np

# Coordinates of all cities including the depot
coordinates = [
    (145, 215), # Depot city 0
    (151, 264), # City 1
    (159, 261), # City 2
    (130, 254), # City 3
    (128, 252), # City 4
    (163, 247), # City 5
    (146, 246), # City 6
    (161, 242), # City 7
    (142, 239), # City 8
    (163, 236), # City 9
    (148, 232), # City 10
    (128, 231), # City 11
    (156, 217), # City 12
    (129, 214), # City 13
    (146, 208), # City 14
    (164, 208), # City 15
    (141, 206), # City 16
    (147, 193), # City 17
    (164, 193), # City 18
    (129, 189), # City 19
    (155, 185), # City 20
    (139, 182)  # City 21
]

# City-to-city Euclidean distance calculator
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Tours given by the solution
tours = [
    [0, 12, 0],
    [0, 14, 0],
    [0, 15, 18, 20, 17, 21, 19, 13, 11, 4, 3, 1, 2, 5, 7, 9, 6, 8, 10, 0],
    [0, 16, 0]
]

# Check for subtour constraint and if each city is visited exactly once
visited = [False] * len(coordinates)
all_tours_testing = []

for tour in tours:
    subtour_check = {}
    for i in range(len(tour) - 1):
        from_city = tour[i]
        to_city = tour[i + 1]
        if to_city == tour[-1] and to_city != 0:
            print("FAIL: Subtour should end at the depot")
        if from_city == to_city:
            print("FAIL: Move from and to the same city")
        if from_city in subtour_check:
            print("FAIL: Subtour elimination constraint violated")
        subtour_check[from_city] = True
        visited[to_city] = True
    all_tours_testing.extend(tour[1:-1])

if len(set(all_tours_testing)) != (len(coordinates) - 1):
    print("FAIL: Not all cities are visited exactly once.")
else:
    print("CORRECT")