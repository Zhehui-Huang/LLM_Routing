# Function to simulate a test scenario
def check_tour_criteria(tour, total_distance):
    requirement_1 = (tour[0] == 0 and tour[-1] == 0)  # Check start and end at depot city 0
    requirement_2 = (len(set(tour)) == 10 and tour.count(0) >= 2)  # Must visit exactly 10 cities including depot, accounting for start and end at depot
    requirement_3 = total_distance > 0  # Check if tour has a positive distance as a basic validation of a plausible shortest tour
    
    if all([requirement_1, requirement_2, requirement_3]):
        print("CORRECT")
    else:
        print("FAIL")

# Example test case assuming a hypothetical solution
# Tour covers exactly ten cities starting and ending at depot city 0
# The total distance is just a hypothetical positive number for testing
hypothetical_tour = [0, 1, 2, 5, 3, 6, 9, 10, 7, 8, 0]
hypothetical_total_distance = 450  # Example distance value

check_tour_criteria(hypothetical_tour, hypothetical_total_distance)