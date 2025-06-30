# BMI Calculator
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")

# City-Country Checker
city = input("Enter city name: ")
country = ""
if city in ["Sydney", "Melbourne", "Brisbane", "Perth"]:
    country = "Australia"
elif city in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]:
    country = "UAE"
elif city in ["Mumbai", "Bangalore", "Chennai", "Delhi"]:
    country = "India"

if country:
    print(f"{city} is in {country}")
else:
    print("City not found in database")

# Two City Checker
city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

def find_country(c):
    if c in ["Sydney", "Melbourne", "Brisbane", "Perth"]:
        return "Australia"
    elif c in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]:
        return "UAE"
    elif c in ["Mumbai", "Bangalore", "Chennai", "Delhi"]:
        return "India"
    return None

country1 = find_country(city1)
country2 = find_country(city2)

if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities not recognized")
