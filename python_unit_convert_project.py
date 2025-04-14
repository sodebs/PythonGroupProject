# Converts length in terms of meters. The result is referred to later in block #5
# 1
def len_convert(num, start_unit, end_unit):
    len_units = {"m": 1, "km": 0.001, "cm": 100, "ft": 3.28084, "in": 39.3701, "yds": 1.09361, "mi": 0.000621371}
    return num * (len_units[end_unit] / len_units[start_unit])


# Converts temperature using a formula. The result is referred to later in block #6.
# 2
def temp_convert(num, start_unit, end_unit):
    if start_unit == "C" and end_unit == "F":
        return (num * (9 / 5) + 32)
    elif start_unit == "F" and end_unit == "C":
        return (num - 32) * (5 / 9)
    else:
        return num


# Converts weight in terms of kilograms. The result is referred to later in block #7.
# 3
def weight_convert(num, start_unit, end_unit):
    weight_units = {"kg": 1, "g": 1000, "lbs": 2.20462, "oz": 35.274}
    return num * (weight_units[end_unit] / weight_units[start_unit])


# Asks for user input regarding type of conversion
# 4
def convert():
    print("UNIT CONVERSION CALCULATOR")
    print()
    print("1. Are you converting length: kilometers, meters, centimeters, feet, inches, yards, miles? ")
    print("2. Are you converting temperature: Celsius, Fahrenheit? ")
    print("3. Are you converting weight: kilograms, grams, pounds, ounces? ")

    # For length conversions, gathers data and stores into the len_convert function.
    # The result of the computation is stored in the "answer" variable.
    #5
    choice = input("Please enter the category of conversion you would like to use (1, 2, or 3): ")
    if choice == "1":
        start_unit = input("What unit are you converting from? km, m, cm, ft, in, yds, mi: ")
        end_unit = input("What unit are you converting to? km, m, cm, ft, in, yds, mi: ")
        num = float(input("Enter the number you would like to convert: "))
        answer = len_convert(num, start_unit, end_unit)

    # For temperature conversions, gathers data and stores into the temp_convert function.
    # The result of the computation is stored in the "answer" variable.
    # 6
    elif choice == "2":
        start_unit = input("What unit are you converting from? F or C: ")
        end_unit = input("What unit are you converting to? F or C: ")
        num = float(input("Enter the number you would like to convert: "))
        answer = temp_convert(num, start_unit, end_unit)

    # For weight conversions, gathers data and stores into the weight_convert function.
    # The result of the computation is stored in the "answer" variable.
    # 7
    elif choice == "3":
        start_unit = input("What unit are you converting from? kg, g, lbs, oz: ")
        end_unit = input("What unit are you converting to? kg, g, lbs, oz: ")
        num = float(input("Enter the number you would like to convert: "))
        answer = weight_convert(num, start_unit, end_unit)

    else:
        print(" Try again. You might have a typo.")

    # Displays final answer with start and end units.
    print(f"{num} {start_unit} is equivalent to {answer} {end_unit}")


if __name__ == "__main__":
    convert()
