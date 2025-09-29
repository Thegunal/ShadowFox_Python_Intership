# Program 1: BMI Category
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print(f"BMI = {bmi:.2f} → Obesity")
elif bmi >= 25:
    print(f"BMI = {bmi:.2f} → Overweight")
elif bmi >= 18.5:
    print(f"BMI = {bmi:.2f} → Normal")
else:
    print(f"BMI = {bmi:.2f} → Underweight")


# Program 2: City and Country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("\nEnter a city name: ")

if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print(f"Sorry, I don't know which country {city} belongs to.")


# Program 3: Check if two cities belong to the same country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Check which country each city belongs to
def get_country(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    else:
        return None

country1 = get_country(city1)
country2 = get_country(city2)

if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the list")
