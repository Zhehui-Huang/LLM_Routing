import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64),
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(city1, city2):
    """Calculate euclidean distance between two cities based on their indices."""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_tour_cost(tour):
    """Calculate the total cost of the tour including return to the start."""
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i-1], tour[i])
    cost += euclidean_distance(tour[-1], tour[0])
    return cost

def partition_cities():
    """Simple heuristic to partition cities to minimize maximum route length."""
    cities = list(range(1, 19))  # Exclude the depot
    # Simple partitioning - could be improved by a more sophisticated method
    robot1_cities = cities[0:9]
    robot2_cities = cities[9:]
    return robot1_cities, robot2_cities

def create_tours(partitions):
    """Create tours from given partitions."""
    tours = []
    tour_costs = []
    for partition in partitions:
        tour = [0] + partition + [0]
        cost = calculate_tour_cost(tour)
        tours.append(tour)
        tour_costs.append(cost)
    return tours, tour_costs

def solve_mTSP():
    """Solve the mTSP problem and print the results."""
    # Partition cities among the robots
    robot1_cities, robot2_cities = partition_cities()
    
    # Create tours
    tours, tour_costs = create_tours((robot1_cities, robot2_cities))
    
    # Find maximum travel cost
    max_cost = max(tour_costs)
    
    # Output the results
    for i, (tour, cost) in enumerate(zip(tour_costs, tours)):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")
    
    print(f"Maximum Travel Cost: {max_cost}")

# Run the solution
solve_mTSP()