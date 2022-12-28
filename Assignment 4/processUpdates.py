# Andrei Merkulov 251145994, Dec 6 2021
from catalogue import CountryCatalogue
CONTINENTS = ["Africa", "Antarctica", "Arctic", "Asia", "Europe", "North_America", "South_America"]
def processUpdates(cntryFileName, updateFileName, badUpdateFile):
    while True:     # opening data file error check
        try:
            catalog = CountryCatalogue(cntryFileName)
            break
        except FileNotFoundError:
            exit = input("Country file not found. \nWould you like to quit? Y (yes) or N (no): ")
            if exit == "N":
                cntryFileName = input("Please enter a new country file name: ")
            else:
                outputF = open("output.txt", "w")
                outputF.write("Update Unsuccessful\n")
                outputF.close()
                return False, None
    while True:
        try:
            u_file = open(updateFileName, "r")
            break
        except FileNotFoundError:
            exit = input("Updates file not found. Would you like to quit? Y (yes) or N (no): ")
            if exit == "N":
                updateFileName = input("Please enter a new update file name: ")
            else:
                outputF = open("output.txt", "w")
                outputF.write("Update Unsuccessful\n")
                outputF.close()
                return False, None
