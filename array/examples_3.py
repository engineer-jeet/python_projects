temprature = input("How many days temperature?  ")
temprature = int(temprature)

all_temperatures = []

for i in range(1, temprature+1):
    data = input("Day " + str(i) + "'" + "s high temp: ")
    data = int(data)
    all_temperatures.append(data)
   
print(all_temperatures)
avg = sum(all_temperatures)/len(all_temperatures)
    
print(avg)
