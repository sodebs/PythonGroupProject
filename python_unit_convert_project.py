# 1
def len_convert(num, start_unit, end_unit):
    len_units = {"m": 1, "km": 0.001, "cm": 100, "ft": 3.28084, "in": 39.3701, "yds": 1.09361, "mi": 0.000621371}
    return num * (len_units[end_unit] / len_units[start_unit])


# 2
def temp_convert(num, start_unit, end_unit):
    if start_unit == end_unit:
        print(f"No conversion needed: {num} {start_unit} is already {num} {end_unit}")
        return num

    if start_unit == "c" and end_unit == "f":
        return (num * (9 / 5) + 32)
    elif start_unit == "f" and end_unit == "c":
        return (num - 32) * (5 / 9)
    else:
        print("Invalid temperature units. Try again.")
        return None

# 3
def weight_convert(num, start_unit, end_unit):
    weight_units = {"kg": 1, "g": 1000, "lbs": 2.20462, "oz": 35.274}
    return num * (weight_units[end_unit] / weight_units[start_unit])

# 4
def convert():
    print("UNIT CONVERSION CALCULATOR")
    print()
    print("1. Are you converting length: kilometers, meters, centimeters, feet, inches, yards, miles? ")
    print("2. Are you converting temperature: Celsius, Fahrenheit? ")
    print("3. Are you converting weight: kilograms, grams, pounds, ounces? ")


    #5
    choice = input("Please enter the category of conversion you would like to use (1, 2, or 3): ")
    if choice == "1":
        start_unit = input("What unit are you converting from? km, m, cm, ft, in, yds, mi: ").lower()
        end_unit = input("What unit are you converting to? km, m, cm, ft, in, yds, mi: ").lower()

        if start_unit not in ["km", "m", "cm", "ft", "in", "yds", "mi"] or end_unit not in \
            ["km", "m", "cm", "ft", "in","yds", "mi"]:
            print("Invalid unit. Please enter a valid unit.")
            return None
        try:
            num = float(input("Enter the number you would like to convert: "))
        except ValueError:
            print("Invalid number. Please enter a valid number.")
            return

        answer = len_convert(num, start_unit, end_unit)

    # 6
    elif choice == "2":
        start_unit = input("What unit are you converting from? F or C: ").lower()
        end_unit = input("What unit are you converting to? F or C: ").lower()
        if start_unit not in ["f", "c"] or end_unit not in ["f", "c"]:
            print("Invalid unit. Please enter a valid unit.")
            return
        try:
            num = float(input("Enter the number you would like to convert: "))
        except ValueError:
            print("Invalid number. Please enter a valid number.")
            return

        answer = temp_convert(num, start_unit, end_unit)


    # 7
    elif choice == "3":
        start_unit = input("What unit are you converting from? kg, g, lbs, oz: ").lower()
        end_unit = input("What unit are you converting to? kg, g, lbs, oz: ").lower()
        if start_unit not in ["kg", "g", "lbs", "oz"] or end_unit not in ["kg", "g", "lbs", "oz"]:
            print("Invalid unit. Please enter a valid unit.")
            return

        try:
            num = float(input("Enter the number you would like to convert: "))
        except ValueError:
            print("Invalid number. Please enter a valid number.")
            return

        answer = weight_convert(num, start_unit, end_unit)
    else:
        print(" Try again. You might have a typo.")
        return


    print(f"{num} {start_unit} is equivalent to {answer} {end_unit}")


if __name__ == "__main__":
    convert()

