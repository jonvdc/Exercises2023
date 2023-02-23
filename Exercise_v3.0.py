name = input("What is the drivers name? ")

tripCount = 0
# Set-up to take floats
totalTime = 0.0
totalIncome = 0.0
# Constants rather than literals for these two costs
baseCost = 10.00
minuteCost = 2.00
# Sets loop to true
startNewTrip = "Yes"

while startNewTrip == "Yes":
    # Float allows for half minutes
    tripTime = float(input("How many minutes did the trip take? "))
    tripCount += 1
    totalTime += tripTime
    tripCost = (tripTime * minuteCost) + baseCost
    totalIncome += tripCost
    print(f"This trip costs ${tripCost:.2f}")
    print()
    startNewTrip = input("Do you want to enter a new trip? Yes or No: ")
    # 'No' will break the loop

print("===========================================")
print(f"Driver {name} had {tripCount} trips totalling {round(totalTime)} "
      f"minutes\n"
      # The 'round' function above rounds up or down from .5
      # However, the two below round from 2dp
      f"The average time of all trips was {round(totalTime / tripCount, 2)}"
      f"minutes in \n"
      f"The total income for the day was ${totalIncome:.2f}"
      f"The average cost of all trips was ${totalIncome / tripCount:.2f}")

