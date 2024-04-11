print ("Calculate the redshift of a star or galaxy.")


# Function to find redshift
def calculateRedshift():
    # Observed wavelength entered by user and converted to an integer
    observedWavelength = float(input("Enter the observed wavelength in Angstroms: "))
    
    # Wavelength of element entered by user and converted to an integer
    emmitedWavelength = float(input("Enter the element's emitted wavelength in Angstroms: "))

    # Calculate the change or shift in the wavelength
    redshift = ((observedWavelength/emmitedWavelength) -1)
    return redshift
    
redShiftCalculated = calculateRedshift()
print("------")
velocityKms = (redShiftCalculated*(300000))
velocityMs = (velocityKms/1000)

growthFactor = (redShiftCalculated*100)
distanceMpc = (velocityKms/68)
distanceKm = (distanceMpc*30860000000000000000)
print ("The redshift of the target celestial body is: ",redShiftCalculated, "with no units.")
print("------")
print ("The dynamic interpertion of this value is as follows:")
print ("The velocity of the target celetsial body is: ",velocityKms, "km/s")
print("The distance from earth to the target celetsial body is: ",distanceMpc, "Mpc, or: ",distanceKm, "Km")
print("------")
print("The cosmological interpretation of this value is as follows:")
print("The universal expansion factor since the light being measured left this celestial body is: ", growthFactor, "%")
