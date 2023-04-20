"""
make a new dictionary with capital : country from a country : capital dictionary, with dictionaries comprehention
make another dictionary from a list of words, some of which begin with the same letter; because the keys have to be
unique, only the last key which starts with h will be kept
"""
from pprint import pprint as pp

countries_and_capitals = {"France": "Paris", "Bulgaria": "Sofia", "Greece": "Atena", "Italy": "Roma"}
capitals_and_countries = {capital: country for country, capital in countries_and_capitals.items()}


words = {"hi", "how", "are", "you", "horse"}
a_dict = {x[0]: x for x in words}

if __name__ == '__main__':
    pp(capitals_and_countries)
    print(words, a_dict)
