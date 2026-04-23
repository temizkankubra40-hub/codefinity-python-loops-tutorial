# Travel expenses for multiple trips
travel_costs = [[500, 150, 100, 50], [200, 300, 120, 80], [180, 220, 130, 170], [600, 250, 200, 90], [300, 180, 150, 70], [400, 320, 110, 100], [550, 270, 180, 60], [250, 190, 140, 120], [700, 350, 210, 110], [450, 230, 160, 95], [320, 280, 190, 85], [580, 260, 175, 75], [630, 300, 220, 130], [280, 210, 125, 140], [490, 330, 145, 105], [520, 340, 190, 125], [750, 400, 250, 150], [340, 270, 160, 115], [620, 310, 225, 135], [410, 290, 135, 90]]

# List to store the first significant expense of each trip
significant_expenses = []

i = 0
while i < len(travel_costs):
    j = 0 
    while j < len(travel_costs[i]):
        if travel_costs[i][j] < 100:
            continue
            j += 1
        elif travel_costs[i][j] <= 200:
            j += 1
        else:
            significant_expenses.append(travel_costs[i][j]) 
            break
    i += 1
    print('')


# Testing
print('First Significant Expenses:', significant_expenses)