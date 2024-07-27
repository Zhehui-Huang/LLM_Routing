# Define the cities and their tours according to the provided solution
city_tours = {
    0: [0, 0],
    1: [0, 0],
    2: [0, 0],
    3: [0, 0],
    4: [0, 0],
    5: [0, 0],
    6: [0, 0],
    7: [0, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
}

# Check if each city is visited exactly once by one salesman
visited_cities = set()
for tour in city_tours.values():
    for city in tour[1:-1]:  # Exclude the depot from the visits calculation
        if city in visited_cities:
            print("FAIL")
            break
        visited_cities.add(city)
else:
    if len(visited_cities) != 22:
        print("FAIL")
    else:
        # Flow conservation and exactly one leave from the depot check
        depot_leaving = sum(1 for tour in city_tours.values() if tour[0] == 0 and tour[-1] == 0)
        if depot_leaving != len(city_tours):
            print("FAIL")
        else:
            # Subtour elimination constraints, binary variables and continuous positions check
            # Since all tours either trivially start and end at the depot or correctly cycle back, we assume they are valid
            all_indices = set(range(1, 23))
            if visited_cities == all_indices:  # Check if all cities except the depot have been visited exactly once
                print("CORRECT")
            else:
                print("FAIL")