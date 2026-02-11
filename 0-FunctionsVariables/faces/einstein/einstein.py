userinput = input("Enter a mass in kilograms and ill tell you its equivelant energy: ")

speedoflightsquared = int(300000000 * 300000000)
mass = int(userinput)
energy = mass * speedoflightsquared
print("Total energy of given mass: " + str(energy))
