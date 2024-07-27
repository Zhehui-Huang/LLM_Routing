def check_tours_robots(tours, costs):
    # Setup
    num_cities = 16
    city_visit = [False] * num1b_cities

    for tour, cost in zip(tours, costs):
        # Check if tour starts and ends at the same depot city
        if tour[0] != tour[-1]:
            print("FAIL")
            return

        # Check if each city in this tour is visited exactly once except depot
        visited_in_tour = set()
        for city in tour[1:-1]:  # exclude first and last as they are the start and end depots
            if city in visited_in_tour or city_visit[city]:
                print("FAIL")
                return
            visited_in_tour.add(city)
            city_visit[city] = True
    
    # Ensuring every city was visited exactly once
    if not all(city_visit):
        print("FAIL")
        return

    print("CORRECT")

# Data from your solution
tours = [
    [0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0],
    [1, 4, 11, 15, 12, 3, 8, 13, 2, 10, 6, 7, 5, 14, 9, 0, 1],
    [2, 10, 6, 7, 5, 14, 9, 0, 1, 4, 11, 15, 12, 3, 8, 13, 2],
    [3, 8, 13, 2, 10, 6, 7, 5, 14, 9, 0, 1, 4, 11, 15, 12, 3],
    [4, 11, 15, 12, 3, 8, 13, 2, 10, 6, 7, 5, 14, 9, 0, 1, 4],
    [5, 14, 9, 0, 1, 4, 11, 15, 12, 3, 8, 13, 2, 10, 6, 7, 5],
    [6, 7, 5, 14, 9, 0, 1, 4, 11, 15, 12, 3, 8, 13, 2, 10, 6],
    [7, 5, 14, 9, 0, 1, 4, 11, 15, 12, 3, 8, 13, 2, 10, 6, 7]
]
costs = [173.01, 186.24, 186.24, 186.24, 186.24, 186.24, 186.24, 186.24]

# Running the test
check_tours_robots(tours, costs)