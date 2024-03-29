import calorie_intake_calculator


def your_goal(calories):
    macros_ratio = {
        1: [3.0, 5.5, 1.5],
        2: [3.5, 5.0, 1.5],
        3: [4.5, 4.0, 1.5],
        4: [2.5, 5.5, 2.0],
        5: [2.0, 6.0, 2.0],
    }

    while True:
        goal = input(
            "1. Maintain weight\n2. Weight loss of 0.5kg per week\n3. Extreme weight loss of 1kg per week\n4. Weight gain of 0.5kg per week\n5. Extreme weight gain of 1kg per week\nSelect your goal (1 - 5): "
        )

        # Calculate macros based on recommended ratios (example ratios)
        try:
            goal = int(goal)

            if goal in macros_ratio:
                # Protein (1 gram of protein = 4 calories)
                protein = int((calories * (macros_ratio[goal][0] / 10)) / 4)
                # Carbohydrates (1 gram of carbohydrate = 4 calories)
                carbs = int((calories * (macros_ratio[goal][1] / 10)) / 4)
                # Fat (1 gram of fat = 9 calories)
                fats = int((calories * (macros_ratio[goal][2] / 10)) / 9)

                return protein, carbs, fats
        except ValueError:
            print("Please enter a valid input from 1 to 5.")


if __name__ == "__main__":
    weight, height, age, gender = calorie_intake_calculator.get_user_info()
    bmr = calorie_intake_calculator.calculate_bmr(weight, height, age, gender)
    print()
    calories = int(calorie_intake_calculator.calculate_daily_calories(bmr))
    print()
    protein, carbs, fats = your_goal(calories)
    print()
    print(f"Food energy: {calories} Calories/day")
    print(f"Protein needs: {protein} grams/day")
    print(f"Carbohydrate needs: {carbs} grams/day")
    print(f"Fat needs: {fats} grams/day")
