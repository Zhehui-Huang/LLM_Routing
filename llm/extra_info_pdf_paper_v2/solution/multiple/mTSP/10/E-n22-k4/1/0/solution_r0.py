import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.utils import shuffle

# Define the coordinates for the depot and the cities
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Initialize the number of robots
num_robots = 4

# Function to calculate the total travel cost of a tour
def calculate_cost(tour, city_coords):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean(city_coords[tour[i]], city_coords[tour[i+1]])
    return total_cost

# Heuristic function to generate initial solution
def generate_initial_solution(city_coords, num_robots):
    all_cities = list(range(1, len(city_coords)))  # Exclude the depot city
    shuffle(all_cities)
    split_size = len(all_cities) // num_robots
    tours = [all_cities[i * split_size:(i + 1) * split_size] for i in range(num_robots)]
    
    # Ensuring all cities are covered
    leftover = all_cities[num_robots * split_size:]
    for i, city in enumerate(leftover):
        tours[i].append(city)
    
    # Adding depot start and end
    for tour in tours:
        tour.insert(0, 0)
        tour.append(0)
        
    return tours

# Improve solution with simulated annealing
def optimize_tours(tours, city_coords):
    best_tours = tours
    best_total_cost = sum(calculate_cost(tour, city_coords) for tour in tours)
    
    for _ in range(1000):  # Increase or adjust as needed for optimization
        # Try random swaps
        robot_1, robot_2 = np.random.choice(range(num_robots), 2, replace=False)
        if len(tours[robot_1]) > 2 and len(tours[robot_2]) > 2:  # Ensuring valid swaps
            idx_1, idx_2 = np.random.randint(1, len(tours[robot_1]) - 1), np.random.randint(1, len(tours[robot_2]) - 1)
            tours[robot_1][idx_1], tours[robot_2][idx_2] = tours[robot_2][idx_2], tours[robot_1][idx_1]
        
        # Calculate new total cost
        total_cost = sum(calculate_cost(tour, city_coords) for tour in tours)
        
        # Acceptance criterion for Simulated Annealing
        if total_cost < best_total_cost:
            best_total_cost = total_cost
            best_tours = [list(tour) for tour in tours]
        else:  # Revert the swap if not better
            tours[robot_1][idx_1], tours[robot_2][idx_2] = tours[robot_2][idx_2], tours[robot_1][idx_1]

    return best_tours, best_total_cost

# Main execution function
def main():
    initial_tours = generate_initial_solution(cities, num_robots)
    optimized_tours, best_total_cost = optimize_tours(initial_tours, cities)
    
    # Output results
    for idx, tour in enumerate(optimized_tours):
        tour_cost = calculate_cost(tour, cities)
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost}")
    
    print(f"Overall Total Travel Cost: {best_total_cost}")

# Run the main function
main()