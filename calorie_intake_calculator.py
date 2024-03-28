def get_user_info():
    while True:
        user_input = input(
            "To calculate your daily calorie needs, please enter 'y' to continue or 'q' to quit.: "
        )
        if user_input == "q".lower():
            raise SystemExit("See ya!")
        elif user_input == "y":
            break
        else:
            print("Enter 'y' to continue / 'q' to quit.")

    weight = get_numeric_input("weight", "kg")
    height = get_numeric_input("height", "cm")
    age = get_user_age("age", "years", min_value=15, max_value=80)
    gender = get_gender()

    print("Your personal info as following:")
    print(
        f"Weight: {weight} kg\nHeight: {height} cm\nAge: {age} years old\nGender: {'Male' if gender == 'm' else 'Female'}"
    )

    return weight, height, age, gender


def get_numeric_input(attribute, unit, int_only=False):
    while True:
        try:
            value = float(input(f"Please enter your {attribute} in {unit}: "))
            if int_only and unit != int(value):
                raise ValueError

            return value
        except ValueError as e:
            print(e)


def get_user_age(attribute, unit, int_only=False, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(f"Please enter your {attribute} in {unit} (15 - 80): "))
            if int_only and unit != int(value):
                raise ValueError

            if min_value is not None and value < min_value:
                raise ValueError(
                    f"{attribute.capitalize()} must be at least {min_value}."
                )

            if max_value is not None and value > max_value:
                raise ValueError(f"{attribute.capitalize()} cannot exceed {max_value}")

            return value
        except ValueError as e:
            print(e)


def get_gender():
    while True:
        gender = input("Please enter your gender (m/f): ").lower()
        if gender == "m" or gender == "f":
            return gender
        else:
            print("Invalid gender input, please reenter (m = Male / f = Female).")


def calculate_bmr(weight, height, age, gender):
    if gender == "m":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)


def calculate_daily_calories(bmr):
    activity_multipliers = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.7225, 5: 1.9}

    while True:
        exercise_level = input(
            "1. Sedentary (little or no exercise)\n2. Light exercise (1-3 days per week)\n3. Moderate exercise (3-5 days per week)\n4. Active exercise (6-7 days per week)\n5. Extremely active exercise (twice per day)\nSelect your exercise level (1 - 5): "
        )

        try:
            exercise_level = int(exercise_level)

            if exercise_level in activity_multipliers:
                return bmr * activity_multipliers[exercise_level]
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid input from 1 to 5.")


if __name__ == "__main__":
    weight, height, age, gender = get_user_info()
    bmr = calculate_bmr(weight, height, age, gender)
    print(f"BMR: {bmr:.2f}")
    print(
        "Basal Metabolic Rate (BMR) is the amount of energy your body needs to maintain basic functions while at rest. Most people's BMR is between 1000 - 2000. This means that they need to take in between 1000 - 2000 calories each day to fuel their basic functions\n"
    )
    calories = calculate_daily_calories(bmr)
    print(f"*** Your daily calorie needs: {calories:.2f} cal")
