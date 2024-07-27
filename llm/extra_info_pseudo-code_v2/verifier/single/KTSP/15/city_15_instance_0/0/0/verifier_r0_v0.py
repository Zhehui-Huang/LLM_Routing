import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, given_cost):
    cities = [
        (9, 93),  # depot city 0
        (8, 51),  # city 1
        (74, 99), # city 2
        (78, 50), # city 3
        (21, 23), # city 4
        (88, 59), # city 5
        (79, 77), # city 6
        (63, 23), # city 7
        (19, 76), # city 8
        (21, 38), # city 9
        (19, 65), # city 10
        (11, 40), # city 11
        (3, 21),  # city 12
        (60, 55), # city 13
        (4, 39)   # city 14
    ]

    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the tour includes exactly 4 cities
    if len(tour) != 5:  # including repeating the depot city at the end
        return "FAIL"
    
    # Check for 1 robot (implicit by solving once, not explicitly checkable by tour list)

    # Calculate the total cost of the tour
    total_cost = 0
    for i in range(1, len(tour)):
        city_index_previous = tour[i-1]
        city_index_current = tour[i]
        total_cost += calculate_euclidean_distance(
            cities[city_index_previous][0], cities[city_index_previous][1],
            cities[citypl_index_current][0], cities[city_index_current][1]
        )

    # Check if computed travel cost matches the given one
    if not math.isclose(total_cost, given_cost, rel_tol=1e-03):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Provided solution data
sample_tour = [0, 10, 14, 1, 0]
sample_cost = 114.41

# Call the verification function
result = verify_tour(sample_tour, sample_cost)
print(result)