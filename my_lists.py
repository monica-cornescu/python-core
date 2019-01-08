list1 = ["Inspected pkt", "Transmitted to Resource pkt", "Dropped by Resource pkt", "Passes pkt"]
list2 = ["Inspected bytes", "Transmitted to Resource bytes", "Dropped by Resource bytes", "Passes bytes"]

list3 = list1.extend(list2)
list4 = list2.extend(list1)

print(list3)
print(list4)

print(list1.insert(1, "Invalid pkt"))
