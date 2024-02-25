import math
import re


def extract_solution_with_separation(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content by double newlines to find separated chunks
    # chunks = content.split('\n\n')

    chunks = re.split(r'\n\s*\n', content)
    # Assuming the solution chunk is well defined and separated as indicated
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
            tour = eval(parts[1].strip())
            tours[robot] = tour

        if line.startswith('Robot') and 'Cost' in line:
            parts = line.split(':')
            robot = parts[0].strip()
            if parts[1].strip() == 'inf':
                cost = float(1e9)
            else:
                cost = eval(parts[1].strip())
            costs[robot] = cost

        if line.startswith('Final cost'):
            parts = line.split(':')
            final_cost = eval(parts[1].strip())

        if file_path.split('/')[5] == 'E-TPP':
            if line.startswith('Robot') and 'Product' in line:
                parts = line.split(':')
                robot = parts[0].split('-')[0].strip()
                city_amount = eval(parts[1].strip())
                purchases[robot] = city_amount

    return tours, costs, final_cost, purchases


def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def calculate_tour_cost(tour, cities):
    cost = 0.0
    for i in range(len(tour) - 1):
        cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost


def verify_start_end_depot(tours, depot=3):
    # Check 1: Each robot starts and ends at the depot
    for robot, tour in tours.items():
        if len(tour) == 0:
            return f"Constraint Violated: Each robot must have a tour, but {robot} does not."
        if tour[0] != depot or tour[-1] != depot:
            return f"Constraint Violated: Each robot starts and ends at the depot, but {robot} does not."

    return ""


def verify_visit_city_once(tours, cities):
    # Check 2: Each city must be visited exactly once
    all_visited_cities = [city for tour in tours.values() for city in tour[1:-1]]  # Excluding depot at start/end
    if len(all_visited_cities) != len(set(all_visited_cities)) or len(all_visited_cities) != len(cities) - 1:
        for city in range(1, len(cities) + 1):
            if city != 3 and all_visited_cities.count(city) != 1:
                return (f"Constraint Violated: Each city must be visited exactly once by one of the robots, "
                        f"and city {city} is not visited correctly.")

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
        provided_cost = robot_costs[robot_cost_key]

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
    total_units_purchased = sum(units for _, units in product.values())
    if total_units_purchased < 60:
        return (f"Constraint Violated: Total units purchased is {total_units_purchased}, "
                "but the minimum required is 60.")
    return ""


def verify_robot_capacity(robot_capacities, product):
    capacity_check = all(units <= robot_capacities[robot] for robot, (_, units) in product.items())
    if not capacity_check:
        return "Constraint Violated: At least one robot's capacity is exceeded by the purchased units."

    return ""


def verify_full_purchase_requirements(city_products, product):
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
        calculated_cost = calculate_total_cost(robot, robot_tour, purchases, city_products, cities)
        provided_cost = robot_costs[robot_name + ' - Cost']

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
    # Check 2: Each city must be visited exactly once
    all_visited_cities = [city for tour in tours.values() for city in tour[1:-1]]  # Excluding depot at start/end
    if len(all_visited_cities) != len(set(all_visited_cities)) or len(all_visited_cities) != len(cities) - 1:
        for city in range(1, len(cities) + 1):
            if city != 3 and all_visited_cities.count(city) != 1:
                return (f"Constraint Violated: Each city must be visited exactly once by one of the robots, "
                        f"and city {city} is not visited correctly.")

    return ""

def verify_sequence_constraints(tours, sequence_order):
    # Define the sequence order
    # sequence_order = [2, 4, 5, 6, 7]

    for robot, tour in tours.items():
        # Filter the tour to only include cities that are part of the sequence constraint
        filtered_tour = [city for city in tour if city in sequence_order]

        # Check if the filtered tour is in the same order as the sequence order
        for i in range(len(filtered_tour) - 1):
            if sequence_order.index(filtered_tour[i]) > sequence_order.index(filtered_tour[i + 1]):
                return (f"Constraint Violated: Sequence constraint violated in {robot}'s tour. {filtered_tour[i]} "
                        f"appears before {filtered_tour[i + 1]}")

    return ""
