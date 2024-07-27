import math

# City coordinates with index as city numbers
cities_coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def calculate_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_tour_start_end(tour):
    # Check if tour starts and ends at the depot (city 0)
    return tour[0] == 0 and tour[-1] == 0

def check_visited_once(tour):
    # Check if each city is visited exactly once, except depot which should be visited twice
    from collections import Counter
    counts = Counter(tour)
    # Check count of each city (1 for all, 2 for depot)
    return all(count == 1 for city, count in counts.items() if city != 0) and counts[0] == 2

def calculate_total_travel_cost(tour):
    # Get total travel cost of the tour
    total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_cost

def main():
    proposed_tour = [0, 1, 4, 12, 3, 7, 11, 2, 8, 6, 10, 13, 9, 5, 14, 0]
    proposed_cost = 330.41
    
    # Checking all requirements
    if (check_tour_start_end(proposed_tour) and 
        check_visited_once(proposed_tour) and
        abs(calculate_total_travel_cost(proposed_tour) - proposed_cost) < 1e-2):
        print("CORRECT")
    else:
        print("FAIL")

main()