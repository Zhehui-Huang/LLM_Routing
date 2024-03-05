import math
import re

from utils import fix_pattern

reflect_num = 7
test_file_num = 10

cities_5 = {
    1: (9, 4),
    2: (4, 6),
    3: (4, 4),  # Depot
    4: (3, 4),
    5: (4, 8),
}

cities_10 = {
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


def extract_solution_with_separation(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content by double newlines to find separated chunks
    # chunks = content.split('\n\n')

    chunks = re.split(r'\n\s*\n', content)
    # Assuming the solution chunk is well-defined and separated as indicated
    solution_chunk = ""
    for chunk in chunks:
        if "Robot" in chunk and "Tour" in chunk:
            solution_chunk = chunk
            break

    # Extract tours from the solution chunk
    tours = {}
    costs = {}
    final_cost = -1

    purchases = {}

    for line in solution_chunk.split('\n'):
        if line.startswith('Robot') and 'Tour' in line:
            parts = line.split(':')
            robot = parts[0].strip()
            tour = fix_pattern(parts[1].strip())
            tours[robot] = tour

        if line.startswith('Robot') and 'Cost' in line:
            parts = line.split(':')
            robot = parts[0].strip()
            try:
                if parts[1].strip() == 'inf' or parts[1].strip() == '-inf':
                    cost = float(1e9)
                else:
                    tmp_real_cost = parts[1].strip()
                    if tmp_real_cost[-1] == '.':
                        tmp_real_cost = tmp_real_cost[:-1]
                    cost = eval(tmp_real_cost)
            except:
                cost = 0
            costs[robot] = cost

        if line.startswith('Final cost') or line.startswith('Final Cost'):
            parts = line.split(':')
            tmp_real_cost = parts[1].strip()
            if tmp_real_cost[-1] == '.':
                tmp_real_cost = tmp_real_cost[:-1]

            if parts[1].strip() == 'inf' or parts[1].strip() == '-inf':
                final_cost = float(1e9)
            else:
                final_cost = eval(tmp_real_cost)

        if 'E-TPP' in file_path:
            try:
                if line.startswith('Robot') and 'Product' in line:
                    parts = line.split(':')
                    robot = parts[0].split('-')[0].strip()
                    city_amount = eval(parts[1].strip())
                    if isinstance(city_amount[0], tuple):
                        purchases[robot] = city_amount[0]
            except:
                purchases = {}

    return tours, costs, final_cost, purchases


def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def calculate_tour_cost(tour, cities):
    try:
        cost = 0.0
        for i in range(len(tour) - 1):
            cost += calculate_distance(cities[int(tour[i])], cities[int(tour[i + 1])])
    except:
        return -1

    return cost


def verify_start_end_depot(tours, depot=3):
    # Check 1: Each robot starts and ends at the depot
    for robot, tour in tours.items():
        try:
            if len(tour) == 0:
                return f"Constraint Violated: Each robot must have a tour, but {robot} does not."
            if tour[0] != depot or tour[-1] != depot:
                return f"Constraint Violated: Each robot starts and ends at the depot, but {robot} does not."
        except:
            return f"Constraint Violated: verify_start_end_depot, {tour} is not a list."

    return ""


def verify_visit_city_once(tours, cities):
    try:
    # Check 2: Each city must be visited exactly once
        all_visited_cities = [city for tour in tours.values() for city in tour[1:-1]]  # Excluding depot at start/end
        if len(all_visited_cities) != len(set(all_visited_cities)) or len(all_visited_cities) != len(cities) - 1:
            for city in range(1, len(cities) + 1):
                if city != 3 and all_visited_cities.count(city) != 1:
                    return (f"Constraint Violated: Each city must be visited exactly once by one of the robots, "
                            f"and city {city} is not visited correctly.")
    except:
        return f"Constraint Violated: verify_start_end_depot, {tours} is wrong."

    return ""


def verify_num_robots(tours):
    if len(tours) != 4:
        return ("Constraint Violated: There are only four robots available for the task, "
                "but the solution does not use four robots.")
    return ""


def verify_euclidean_dist(tours, cities, robot_costs):
    for robot, tour in tours.items():
        # Assuming calculate_tour_cost is a function that you've defined elsewhere
        calculated_cost = calculate_tour_cost(tour, cities)
        robot_cost_key = robot.replace('Tour', 'Cost')  # Adjust the key to match the corresponding cost entry
        try:
            provided_cost = robot_costs[robot_cost_key]
        except:
            return f"Constraint Violated: Tour cost for {robot} is incorrect. "
        # Check if the calculated cost matches the provided cost (within a small margin of error)
        if not math.isclose(round(calculated_cost, 2), round(provided_cost, 2), rel_tol=1e-2):
            return (f"Constraint Violated: Tour cost for {robot} is incorrect. "
                    f"Expected: {provided_cost}, Calculated: {calculated_cost}.")

    return ""


def verify_city_group_visitation(tours, city_groups):
    # Invert city_groups for easy lookup: which group does each city belong to?
    city_to_group = {city: group for group, cities in city_groups.items() for city in cities}

    # Track visited groups
    visited_groups = set()

    for robot, tour in tours.items():
        for city in tour:
            if city in city_to_group:  # If the city belongs to a group
                group = city_to_group[city]
                if group in visited_groups:
                    return f"Constraint Violated: Group {group} visited more than once."
                visited_groups.add(group)

    # Check if all groups were visited
    if len(visited_groups) != len(city_groups):
        missing_groups = set(city_groups.keys()) - visited_groups
        return f"Constraint Violated: Not all groups were visited. Missing: {missing_groups}"

    return ""


def verify_city_visitation_at_most_once(tours):
    # Initialize a dictionary to count visits for each city
    city_visit_counts = {}

    for tour in tours.values():
        for city in tour:
            # Exclude the depot (City 3) from this check
            if city == 3:
                continue
            if city in city_visit_counts:
                city_visit_counts[city] += 1
            else:
                city_visit_counts[city] = 1

    # Check for any city visited more than once
    for city, count in city_visit_counts.items():
        if count > 1:
            return f"Constraint Violated: City {city} is visited more than once."

    return ""


def verify_city_visitation_at_least_once(tours, cities):
    # Collect all visited cities from the tours, excluding the depot at the start/end
    all_visited_cities = [city for tour in tours.values() for city in tour[1:-1]]

    # Create a set of unique visited cities to remove duplicates
    unique_visited_cities = set(all_visited_cities)

    # Check if each city, except the depot, is visited at least once
    missing_cities = [city for city in cities if city not in unique_visited_cities and city != 3]

    if missing_cities:
        return (f"Constraint Violated: All cities must be visited at least once by the robots, "
                f"missing cities: {', '.join(map(str, missing_cities))}.")

    return ""


def verify_total_units_purchased(product):
    if product == {}:
        return f"Constraint Violated: product is {product}."
    total_units_purchased = sum(units for _, units in product.values())
    if total_units_purchased < 60:
        return (f"Constraint Violated: Total units purchased is {total_units_purchased}, "
                "but the minimum required is 60.")
    return ""


def verify_robot_capacity(robot_capacities, product):
    try:
        capacity_check = all(units <= robot_capacities[robot] for robot, (_, units) in product.items())
    except:
        robot_capacities = {'Robot 1': 10, 'Robot 2': 15, 'Robot 3': 20, 'Robot 4': 20}
        capacity_check = all(units <= robot_capacities[robot] for robot, (_, units) in product.items())

    if not capacity_check:
        return "Constraint Violated: At least one robot's capacity is exceeded by the purchased units."

    return ""


def verify_full_purchase_requirements(city_products, product):
    if product == {}:
        return f"Constraint Violated: product is {product}."
    full_purchase_check = all(city_products[city]['units'] == units for robot, (city, units) in product.items())

    if not full_purchase_check:
        return "Constraint Violated: The full purchase requirement is not met."

    return ""


def calculate_travel_cost(tour, cities):
    travel_cost = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        travel_cost += 10 * distance
    return travel_cost


def calculate_purchasing_cost(robot_name, purchases, city_products):
    city, units = purchases[robot_name]
    return city_products[city]['units'] * city_products[city]['price']


def calculate_total_cost(robot, tour, purchases, city_products, cities):
    # for robot, tour in tours.items():
    robot_name = robot.replace(' - Tour', '')
    travel_cost = calculate_travel_cost(tour, cities)
    purchasing_cost = calculate_purchasing_cost(robot_name, purchases, city_products)
    total_cost = travel_cost + purchasing_cost

    return total_cost


def verify_total_travel_prod_cost(tours, purchases, city_products, robot_costs, cities):
    for robot, robot_tour in tours.items():
        robot_name = robot.split(' - ')[0]
        try:
            calculated_cost = calculate_total_cost(robot, robot_tour, purchases, city_products, cities)
            provided_cost = robot_costs[robot_name + ' - Cost']
        except:
            return ""

        if not math.isclose(round(calculated_cost, 2), round(provided_cost, 2), rel_tol=1e-2):
            return (f"Constraint Violated: Tour cost for {robot} is incorrect. "
                    f"Expected: {provided_cost}, Calculated: {calculated_cost}.")

    return ""


def verify_visit_time_constraints(tours, time_windows, cities):
    for robot, tour in tours.items():
        time = 0  # Start time for each robot
        for i in range(len(tour) - 1):
            # Calculate travel time to the next city
            travel_time = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
            time += travel_time  # Update time with travel time

            # Check if arrival time is within the time window of the next city
            if not (time_windows[tour[i + 1]][0] <= time <= time_windows[tour[i + 1]][1]):
                return f"Constraint Violated: Arrival time at {tour[i + 1]} is not within the time window. "

    return ""


def verify_dist_given_matrix(tours, distance_matrix, robot_costs):
    for robot, tour in tours.items():
        # Adjusting city numbers for 0-indexing
        adjusted_tour = [city - 1 for city in tour]  # Subtract 1 for 0-based indexing
        travel_cost = 0
        for i in range(len(adjusted_tour) - 1):
            travel_cost += distance_matrix[adjusted_tour[i]][adjusted_tour[i + 1]]

        robot_cost_key = robot.replace('Tour', 'Cost')  # Adjust the key to match the corresponding cost entry
        provided_cost = robot_costs[robot_cost_key]
        # Check if the calculated cost matches the provided cost (within a small margin of error)
        if not math.isclose(round(travel_cost, 2), round(provided_cost, 2), rel_tol=1e-2):
            return (f"Constraint Violated: Tour cost for {robot} is incorrect. "
                    f"Expected: {provided_cost}, Calculated: {travel_cost}.")

    return ""


def verify_start_multi_end_depot(tours, start_depot=3, depot_lists=None):
    # Check if all robots start from City 3
    for robot, tour in tours.items():
        if isinstance(tour, int):
            return f"Constraint Violated: {tour} is not a list."
        if len(tour) == 0:
            return f"Constraint Violated: Each robot must have a tour, but {robot} does not."
        if tour[0] != start_depot:
            return f"Constraint Violated: Each robot starts at the depot, but {robot} does not."

    # Check if each robot ends at a depot
    for robot, tour in tours.items():
        if tour[-1] not in depot_lists:
            return f"Constraint Violated: Each robot ends at the depot, but {robot} does not."

    return ""


def verify_visit_city_multi_depots_once(tours, cities, depot_lists):
    # Initialize counters for city visits
    city_visit_counts = {city_id: 0 for city_id in cities.keys()}

    # Count visits for each city
    for tour in tours.values():
        for city in tour:
            try:
                city_visit_counts[city] += 1
            except:
                return f"Constraint Violated: City {city} does not exist."

    # Check if non-depot cities are visited exactly once and depots at least once
    for city_id, visits in city_visit_counts.items():
        is_depot = city_id in depot_lists

        if is_depot and visits < 1:
            return f"Constraint Violated: Depot city {city_id} is not visited at least once."
        elif not is_depot and visits != 1:
            return (f"Constraint Violated: Non-depot city {city_id} is visited {visits} times, "
                    f"but should be exactly once.")

    return ""


def verify_energy(tours, cities, ori_energy=11):
    segment_distances = []  # To store distances of each travel segment

    for robot, tour in tours.items():
        energy = ori_energy
        for i in range(len(tour) - 1):
            try:
                distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
            except:
                return f"Constraint Violated: City {tour[i], tour[i + 1]} does not exist."

            # If the robot visits a depot, reset energy and continue
            if tour[i] in [1, 3, 7]:
                energy = ori_energy
            else:
                # Subtract the traveled distance from the robot's energy
                energy -= distance
                # If energy goes below 0 before reaching the next depot, return failure
                if energy < 0:
                    return f"Constraint Violated: Robot {robot} ran out of energy before reaching the next depot."
                segment_distances.append(distance)

    return ""


def verify_color_match(robot_tours, city_colors, robot_colors, depot=3):
    for robot, tour in robot_tours.items():
        try:
            robot_id = robot.split(' ')[1]
            if robot_id in list(robot_colors.values()):
                robot_color = robot_id
            elif robot_id in list(['A', 'B', 'C', 'D']):
                tmp_r_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
                robot_id = tmp_r_dict[robot_id]
                robot_color = robot_colors[robot_id]
            else:
                robot_color = robot_colors[int(robot_id)]
        except:
            robot_id = robot.split(' ')[1][1]
            if robot_id in list(robot_colors.values()):
                robot_color = robot_id
            else:
                robot_color = robot_colors[int(robot_id)]

        for city in tour:
            try:
                city = int(city)
            except:
                return f"{city} is not int."
            if city == depot:  # Skip depot
                continue
            if robot_color not in city_colors[city]:
                return f"{robot} violates the color constraint at city {city}."
    return ""


def verify_selected_cities(tours):
    city_10_visited = any(10 in tour for tour in tours.values())
    if city_10_visited:
        return "Constraint Violated: City 10 should not be visited."

    cities_visited = []
    for tour in tours.values():
        cities_visited.extend(tour[1:-1])  # Exclude the depot from the beginning and end of each tour

    # Check if each city (except for the depot and city 10, which should not be visited) is visited exactly once
    cities_to_visit = set(range(1, 10))  # City 10 should not be visited, so it's excluded
    visited_once_check = all(cities_visited.count(city) == 1 for city in cities_to_visit if city != 3)

    if not visited_once_check:
        return "Constraint Violated: Each city (except city 3 and city 10) should be visited exactly once."

    return ""


def verify_sequence_constraints(tours, sequence_order):
    # Define the sequence order
    # sequence_order = [2, 4, 5, 6, 7]
    if isinstance(sequence_order, str):
        sequence_order = eval(sequence_order)

    try:
        for robot, tour in tours.items():
            # Filter the tour to only include cities that are part of the sequence constraint
            filtered_tour = [city for city in tour if city in sequence_order]

            # Check if the filtered tour is in the same order as the sequence order
            for i in range(len(filtered_tour) - 1):
                if sequence_order.index(filtered_tour[i]) > sequence_order.index(filtered_tour[i + 1]):
                    return (f"Constraint Violated: Sequence constraint violated in {robot}'s tour. {filtered_tour[i]} "
                            f"appears before {filtered_tour[i + 1]}")
    except:
        return f"Constraint Violated: verify_sequence_constraints, {tours} is wrong."

    return ""


def verify_max_dist_two_city(tours, cities, final_cost):
    # Calculate the maximum travel cost between any two consecutive cities in the updated tour
    try:
        updated_max_cost = 0
        for robot, tour in tours.items():
            for i in range(len(tour) - 1):
                cost = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
                updated_max_cost = max(updated_max_cost, cost)

        if not math.isclose(round(updated_max_cost, 2), round(final_cost, 2), rel_tol=1e-2):
            raise ValueError(f"Constraint Violated: Maximum travel cost between any two consecutive cities is incorrect. "
                             f"Expected: {final_cost}, Calculated: {updated_max_cost}")
    except:
        return f"Constraint Violated: Tours are wrong."

    return ""
