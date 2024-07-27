# Corrected print statement for the execution results
for idx, tour in enumerate(final_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")

print(f"Overall Total Travel Cost: {overall_cost}")