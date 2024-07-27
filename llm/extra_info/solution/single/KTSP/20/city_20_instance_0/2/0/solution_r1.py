import itertools

def find_shortest_tour(cities, depot=0):
    # Assumption: 'cities' is a list of tuples representing (x, y) coordinates.
    # Assumption: `depot` is the start and end point index in the cities list.
    
    number_of_cities = len(cities)
    shortest_distance = float('inf')
    best_tour = None
    
    # We include the depot `0` and choose any 3 of the remaining cities
    for tour in itertools.combinations(range(1, number_of_cities), 3):
        current_tour = [depot] + list(tour) + [depot]
        # Calculate the travel cost of the tour
        travel_cost = sum(distances[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))
        
        if travel.local_cost < shortest_distance:
            shortest_distance = travel_cost
            best_tour = current_tour
    
    return best_tour, shortest_distance

# Generating the shortest tour and its cost
tour, total_cost = find_shortest_tour(cities)

# Formatting and outputting the results
print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost}')