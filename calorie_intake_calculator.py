def get_user_info():
    while True:
        user_input = input(
            "To calculate your daily calorie needs, please enter the following information. (Please enter 'y' to continue / 'q' to quit.): "
        )
        if user_input == "q":
            raise SystemExit("See ya!")
        elif user_input == "y":
            break
        else:
            print("Please decide. 'y' to continue / 'q' to quit")

    while True:
        try:
            weight = float(input("Please enter your weight in kg: "))
            break
        except ValueError:
            print("Input of weight is not numeric, please try again!")

    while True:
        try:
            height = float(input("Please enter your height in cm: "))
            break
        except ValueError:
            print("Input of height is not numeric, please try again!")

    while True:
        age = input("Please enter your age: ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Input of age is not numeric, please try again!")

    while True:
        gender = input("Please enter your gender (m/f): ")
        if gender == "m" or gender == "f":
            print("Your personal info as following:")
            print(
                f"Weight: {weight} kg\nHeight: {height} cm\nAge: {age} years old\nGender: {'Male' if gender == 'm' else 'Female'}"
            )
            break
        else:
            print("Invalid gender input, please reenter (m = male / f = female).")

    return weight, height, age, gender


def calculate_bmr():
    weight, height, age, gender = get_user_info()

    if gender == "m":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr


bmr = calculate_bmr()
print(f"BMR: {bmr:.2f}")
print()
print(
    "Basal Metabolic Rate (BMR) is the amount of energy your body needs to maintain basic functions while at rest. Most people's BMR is between 1000 - 2000. This means that they need to take in between 1000 - 2000 calories each day to fuel their basic functions"
)
print()


def calculate_daily_calories(bmr):
    while True:
        calories = 0

        exercise_level = input(
            "1. Sedentary\n2. Lightly active\n3. Moderately active\n4. Very active\n5. Extremely active\nSelect your exercise level as above(1 - 5): "
        )

        if exercise_level.isdigit():
            exercise_level = int(exercise_level)

        if exercise_level == 1:
            calories = bmr * 1.2
        elif exercise_level == 2:
            calories = bmr * 1.375
        elif exercise_level == 3:
            calories = bmr * 1.55
        elif exercise_level == 4:
            calories = bmr * 1.7225
        elif exercise_level == 5:
            calories = bmr * 1.9
        else:
            print("Please enter valid input from 1 to 5.")
            continue

        return calories


calories = calculate_daily_calories(bmr)
print(f"Your daily calorie needs: {calories:.2f} cal")
