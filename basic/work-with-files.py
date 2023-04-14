import re

# create a file with open and x option

#csvFile = open("C:\_D\@MONICA\learning\python3-for-windows\statsfile.txt", 'x')

# read a file and search for the IP addresses inside it

ipFile = open("C:\_D\@MONICA\learning\python3-for-windows\ipfile.txt", "r")

ipList = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ipFile.read())

print(ipList, len(ipList))
