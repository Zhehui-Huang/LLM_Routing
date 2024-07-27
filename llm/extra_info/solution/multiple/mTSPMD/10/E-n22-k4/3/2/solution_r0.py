import math
import itertools

# All city coordinates including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Matrix of distances between every pair of cities
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Number of robots and their respective start/end depots
num_robots = 4
depots = [0, 1, 2, 3]

# Function to solve the problem
def solve_mTSP():
    # Assign cities to each depot robot
    cities = list(range(4, len(coordinates)))
    assignments = [[] for _ in range(num_robots)]
    for i, city in enumerate(cities):
        assignments[i % num_robots].append(city)

    # Add the depot city to each robot's tour
    tours = [[depots[i]] + assignments[i] for i in range(num_robots)]

    # Append the depot back to complete the tour
    for i in range(num_robots):
        tours[i].append(depots[i])

    # Calculate total costs
    def tour_cost(tour):
        return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

    costs = [tour_cost(tour) for tour in tours]
    overall_cost = sum(costs)

    return tours, costs, overall_cost

# Find solution
tours, costs, overall_cost = solve_mTSP()

# Output the results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {round(costs[i], 2)}")
print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")