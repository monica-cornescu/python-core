user_input = input('Why did you start learning python? ')

print (user_input)

# string formatting

s1 = "Applicant information: %s, %.2f m hight, %d years old" % ("John Smith", 1.85, 40) 
s2 = "Applicant information: {}, {} m hight, {} years old".format("Johana Stewart", 1.75, 37)
s3 = "Statistics snapshot: Inspected: {0}, Invalid packets: {1}, Transmitted to resource: {2}, Dropped by Resource: {1}, Passed: {2}".format(1344, 0, 672, 1300)
s4 = "I run SNMP tests on the VM with the IP: 10.38.185.148, and sometimes on another one: 10.38.185.149"

s5 = s4.find("10")
first_ip = s4[s5:53]
second_ip = s4[-13:]

print (s1)
print (s2)
print (s3)
print (s4)
print (s5)
print (first_ip)
print (second_ip)