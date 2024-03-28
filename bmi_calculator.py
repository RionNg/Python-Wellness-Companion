import sys


def get_user_info():
    while True:
        user_input = input(
            "To calculate your BMI, please enter 'y' to continue or 'q' to quit.: "
        )
        if user_input.lower() == "q":
            raise sys.exit("See ya!")
        elif user_input == "y":
            break
        else:
            print("Enter 'y' to continue / 'q' to quit.")

    weight = get_numeric_input("weight", "kg")
    height = get_numeric_input("height", "cm")

    print("Your personal info as following:")
    print(f"Weight: {weight} kg\nHeight: {height} cm")

    return weight, height


def get_numeric_input(attribute, unit, int_only=False):
    while True:
        try:
            value = float(input(f"Please enter your {attribute} in {unit}: "))
            if value <= 0:
                raise ValueError(f"{attribute.capitalize()} must be greater than 0.")
            if int_only and unit != int(value):
                raise ValueError
            return value
        except ValueError as e:
            print(e)


def classify_bmi(bmi):
    bmi_classes = {
        (float("-inf"), 16): "severe thinness",
        (16, 17): "moderate thinness",
        (17, 18.5): "mild thinness",
        (18.5, 25): "normal",
        (25, 30): "overweight",
        (30, 35): "obese class I",
        (35, 40): "obese class II",
        (40, float("inf")): "obese class III",
    }

    for key, value in bmi_classes.items():
        if key[0] <= bmi < key[1]:
            return value

    return "Undefined"


def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) * (height / 100))

    return bmi


def bmi_range():
    weight, height = get_user_info()
    bmi = calculate_bmi(weight, height)
    classification = classify_bmi(bmi)
    print(f"Your bmi is {bmi:.1f}, you are classified as {classification}.")


if __name__ == "__main__":
    bmi_range()
