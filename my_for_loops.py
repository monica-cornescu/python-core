# Find the positive and 0 values for the statistics

myStats = {"Received": 1200, "Invalid": 0, "Filtered_out": 150, "Passed": 1000}


#for letter in myString:
#    print(letter, letter*2, letter*3)


#myStatValues = myStats.values()
#myStatKeys = myStats.keys()
positiveStats = []
positiveValues = []
zeroStats = []

# for statValue in myStatValues:
#     print(statValue, type(statValue))
#     if statValue > 0:
#         positiveStats.append(statValue)
#     else:
#         print("These stats are 0: ", statValue)
# print("positiveStats = ", positiveStats)

# for key, value in enumerate(myStats):
#    print(key, value)
#     if value > 0:
#         positiveStats.append(value)
#     else:
#         print(key, "= 0")
# print("positiveStats = ", positiveStats)

myStatsItems = myStats.items()
for stat in myStatsItems:
    statName = stat[0]
    statValue = stat[1]
    if statValue > 0:
        positiveStats.append(statName)
        positiveValues.append(statValue)
    else:
        zeroStats.append(statName)
print("positiveStats are ", positiveStats, "and their corresponding values are ", positiveValues)
print("zeroStats = ", zeroStats)


