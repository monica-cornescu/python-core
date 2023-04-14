# check each element of a list of stats (a dictionary) and when it gets to a certain stat exit and do something with it

#myStats = {"P1-rx": 1200, "P2-rx": 100, "P3-rx": 150, "P4-rx": 1000, "P5-rx": 0, "P6-rx": 500}
myStats = {"Received": 1200, "Dropped": 50, "Invalid": 1, "Filtered_out": 150, "Passed": 1000}

sumStatsTillInvalid = 0
sumStatsNoInvalid = 0

myStatsItems = myStats.items()
for stat in myStatsItems:
    statName = stat[0]
    statValue = stat[1]
    if statName == 'Invalid':
        break
    sumStatsTillInvalid = sumStatsTillInvalid + statValue
print(sumStatsTillInvalid)

for stat in myStatsItems:
    statName = stat[0]
    statValue = stat[1]
    if statName == 'Invalid':
        continue
    sumStatsNoInvalid = sumStatsNoInvalid + statValue
print(sumStatsNoInvalid)




# check each element of a list of stats (a dictionary), and when it gets to a certain stat value
#it skips it and continues with the test

