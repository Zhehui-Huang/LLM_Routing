import sys
from typing import List, Tuple
import math

from utils import read_all_files, read_file
from verify_utils import extract_solution_with_separation

# Define city coordinates with city index starting from 1
cities = {
    1: (9, 4),
    2: (4, 6),
    3: (4, 4),  # Depot
    4: (3, 4),
    5: (4, 8),
    6: (4, 3),
    7: (7, 5),
    8: (5, 0),
    9: (1, 5),
    10: (9, 3)
}

reflect_num = 4
test_file_num = 3


# Function to calculate Euclidean distance between two cities
def calculate_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def calculate_tour_cost(tour: List[int]) -> float:
    cost = 0.0
    for i in range(len(tour) - 1):
        cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost


# Detailed constraint check function
def detailed_constraint_check(tours: dict, cities: dict, robot_costs: dict) -> str:
    # Check 1: Each robot starts and ends at the depot
    for robot, tour in tours.items():
        if len(tour) == 0:
            return f"Constraint Violated: Each robot must have a tour, but {robot} does not."
        if tour[0] != 3 or tour[-1] != 3:
            return f"Constraint Violated: Each robot starts and ends at the depot, but {robot} does not."

    # Check 2: Each city must be visited exactly once
    all_visited_cities = [city for tour in tours.values() for city in tour[1:-1]]  # Excluding depot at start/end
    if len(all_visited_cities) != len(set(all_visited_cities)) or len(all_visited_cities) != len(cities) - 1:
        for city in range(1, len(cities) + 1):
            if city != 3 and all_visited_cities.count(city) != 1:
                return f"Constraint Violated: Each city must be visited exactly once by one of the robots, and city {city} is not visited correctly."

    # Constraints 3 & 4: Primary and Secondary Objectives
    # These are optimization goals rather than binary constraints, so we acknowledge their consideration without specific checks.

    # Check 6: Number of robots
    if len(tours) != 4:
        return "Constraint Violated: There are only four robots available for the task, but the solution does not use four robots."

    # Check 7: total cost
    for robot, tour in tours.items():
        # Assuming calculate_tour_cost is a function that you've defined elsewhere
        calculated_cost = calculate_tour_cost(
            tour)  # You might need to pass 'cities' or other arguments based on your implementation
        robot_cost_key = robot.replace('Tour', 'Cost')  # Adjust the key to match the corresponding cost entry
        provided_cost = robot_costs[robot_cost_key]

        # Check if the calculated cost matches the provided cost (within a small margin of error)
        if not math.isclose(round(calculated_cost, 2), round(provided_cost, 2), rel_tol=1e-2):
            return f"Constraint Violated: Tour cost for {robot} is incorrect. Expected: {provided_cost}, Calculated: {calculated_cost}."

    # If all checks pass
    return "** YES!!! **"


def main():
    valid_final_cost = {}
    text_files_loc = read_all_files(root_directory='../../evaluate/1_direct_reflect_v3/4-tsp/B-BTSP')
    print('file number:', len(text_files_loc), sep='\n')

    for i in range(reflect_num):
        valid_final_cost[i] = {j: -1 for j in range(test_file_num)}

    for file_path in text_files_loc:
        # print('file_path: ', file_path, '\n')
        robot_tours, robot_costs, final_cost = extract_solution_with_separation(file_path=file_path)
        # print(robot_tours)
        # print(robot_costs)
        # Running the detailed constraint check on the provided solution
        constraint_check_message = detailed_constraint_check(robot_tours, cities, robot_costs)

        if constraint_check_message == "** YES!!! **":
            # print('file_path: ', file_path, '\n')
            reflect_id = int(file_path.split('/')[6].split('_')[1])
            file_id = int(file_path.split('/')[7].split('.')[0][-1])

            for i in range(reflect_id, reflect_num):
                valid_final_cost[i][file_id] = final_cost
        else:
            print(
                '====================================================================================================')
            print('file_path: ', file_path, '\n')
            print(constraint_check_message)
            print(
                '====================================================================================================')

    print('valid_final_cost:', valid_final_cost, sep='\n')


if __name__ == '__main__':
    sys.exit(main())
