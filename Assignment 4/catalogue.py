# Andrei Merkulov 251145994, Dec 6 2021
from country import Country


class CountryCatalogue:
    def __init__(self, countryFile):
        self.country_cat = []
        c_file = open(countryFile, 'r', encoding='utf-8', errors='ignore')  # this opens file
        next(c_file)  # this skips first line
        for line in c_file:
            if line == "\n":    # if there is nothing in the line it skips the line
                continue
            temp = line.strip("\n").split("|")
            country_new = Country(temp[0], temp[2], temp[3], temp[1])
            self.country_cat.append(country_new)
        c_file.close()
    def getCountryList(self):
        return self.country_cat     # this prints the country catalogue in its default formatting
    def findCountryIndex(self, country_name):
        for i in range(len(self.country_cat)):
            if country_name == self.country_cat[i].getName():   # if repeated inputted country name, then it is returned
                return i    # returns nothing if there is no country
    def setPopulationOfCountry(self, newPopulation, country):
        index = self.findCountryIndex(country)
        if index != None:
            self.country_cat[index].setPopulation(newPopulation)
    def setAreaOfCountry(self, newArea, country):
        index = self.findCountryIndex(country)  # setting the area of a specific country
        if index != None:
            self.country_cat[index].setArea(newArea)
    def setContinentOfCountry(self, newCont, country):
        index = self.findCountryIndex(country)  # setting the continent
        if index != None:
            self.country_cat[index].setContinent(newCont)
    def findCountry(self, country):
        found = False
        for i in range(len(self.country_cat)):  # finding if country is in catalogue
            if str(self.country_cat[i]) == str(country):
                found = True
        if found:
            return country
        else:
            return None
    def addCountry(self, countryName, pop, area, cont):
        success = False
        if self.findCountry(countryName) is None:
            country_new = Country(countryName, pop, area, cont)
            self.country_cat.append(country_new)
            success = True
        return success
    def printCountryCatalogue(self):
        for i in range(len(self.country_cat)):  # prints a list of the countries
            print(self.country_cat[i])
    def saveCountryCatalogue(self, fname):
        counter = 0
        try:
            out_file = open(fname, 'w', encoding='utf-8', errors='ignore')
        except IOError:
            print("Error: output file not accepted")
        out_file.write("Country|Continent|Population|Area\n")
        self.country_cat = sorted(self.country_cat)
        for count_index in range(len(self.country_cat)):
            new_line = self.country_cat[count_index].getName() + "|" + self.country_cat[count_index].getContinent() + "|" + self.country_cat[count_index].getPopulation() + "|" + self.country_cat[count_index].getArea()
            out_file.write(new_line + "\n")
            counter += 1
        if counter != 0:
            return counter
        else:
            return -1
        out_file.close()
