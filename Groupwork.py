"""writer = open("project.csv", "w")
writer.write("The following are The cities in America" + "\n" + "\n")
writer.write(input("Enter City: ")+ "\n")
writer.write("The Following are the cities in Kenya" + "\n" + "\n")
writer.write(input("Enter City: "))

writer.close()
"""
import csv

with open('cities.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    populations = []
    cities = []
    for row in readCSV:
        city = row[1]
        population = row[3]

        populations.append(population)
        cities.append(city)

    print("The Following are the available cities")
    print(cities)

    # now, remember our lists?

    whatCity = input('Which city do you wish to know its population?:')
    cidex = cities.index(whatCity)
    thePopulation = populations[cidex]
    print('The Population of',whatCity,'is:',thePopulation)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("OTHER CITIES ALSO INCLUDE:")
    print ("Rank","City","||", "County/State", "||", "Population")
with open('cities.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row[0], row[1], row[2],row[3],)
#to sort the values

"""import operator
sample = open("cities.csv", "r")
csv1 = csv.reader(sample, delimiter=',')
sort  = sorted(csv1, key=operator.itemgetter(3))
for eachline in sort:
    #sort.append(11)
    print(eachline)
"""
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Add a new City below")

def csv_writer(data_list, file_path):
    file_p = open(file_path, "r+")
    reader_pattern = csv.reader(file_p, delimiter=",", quotechar="$")
    write_pattern = csv.writer(file_p, delimiter=",", quotechar="$")

    content = list(reader_pattern)

    file_p.seek(0,0)
    write_pattern.writerow(data_list)
    write_pattern.writerows(content)
    file_p.truncate()
    file_p.close()

data_list = [input("Enter rank: "), input("Enter city: "), input("Enter County/State: "), input("Enter population: ")]

csv_writer(data_list,'cities.csv')