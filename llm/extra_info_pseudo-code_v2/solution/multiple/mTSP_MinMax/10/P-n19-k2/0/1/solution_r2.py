import math

# Data for cities and coordinates
coordinates = [
    (30, 40),  # Depot City 0
    (37, 52),  # City 1
    (49, 43),  # City 2
    (52, 64),  # City 3
    (31, 62),  # City 4
    (52, 33),  # City 5
    (42, 41),  # City 6
    (52, 41),  # City 7
    (57, 58),  # City 8
    (62, 42),  # City 9
    (42, 57),  # City 10
    (27, 68),  # City 11
    (43, 67),  # City 12
    (58, 27),  # City 13
    (37, 69),  # City 14
    (61, 33),  # City 15
    (62, 63),  # City 16
    (63, 69),  # City 17
    (45, 35)   # City 18
]

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Creating tours for each robot
def create_initial_tours(num_robots=2, depot=0):
    n = len(coordinates)
    cities = list(range(1, n))  # excluding the depot city
    tours = [[depot] for _ in range(num_robots)]
    tour_costs = [0] * num_robots
    while cities:
        for r in range(num_robots):
            if not cities:
                break
            # Choose the closest city to the current city in the tour
            last_city = tours[r][-1]
            next_city = min(cities, key=lambda city: euclidean_distance(coordinates[last_city], coordinates[city]))
            tours[r].append(next_city)
            tour_costs[r] += euclidean_distance(coordinates[last_city], coordinates[next_city])
            cities.remove(next_city)
    
    # Each robot returns to the depot, closing the tour loop
    for r in range(num_robots):
        tour_costs[r] += euclidean_distance(coordinates[tours[r][-1]], coordinates[depot])
        tours[r].append(depot)
    
    max_cost = max(tour_costs)
    return tours, tour_costs, max_cost

# Get the tours, cost and max cost
num_robots = 2
tours, tour_costs, max_cost = create_initial_tours(num_robots=num_robots, depot=0)

# Output results
for idx, (tour, cost) in enumerate(zip(tours, tour_cost)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")