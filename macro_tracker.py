def get_user_info():
    while True:
        user_input = input(
            "To track your daily macros, please enter 'y' to continue or 'q' to quit.: "
        ).lower()
        if user_input == "q":
            raise SystemExit("See ya!")
        elif user_input == "y":
            break
        else:
            print("Enter 'y' to continue / 'q' to quit.")

    protein_goal = macro_goal("Protein", "grams")
    carb_goal = macro_goal("Carbohydrates", "grams")
    fat_goal = macro_goal("Fats", "grams")

    protein_consumed = macro_consumed("Protein", "grams")
    carb_consumed = macro_consumed("Carbohydrates", "grams")
    fat_consumed = macro_consumed("Fats", "grams")

    food_energy_target = (protein_goal * 4) + (carb_goal * 4) + (fat_goal * 9)
    food_energy = (protein_consumed * 4) + (carb_consumed * 4) + (fat_consumed * 9)
    food_energy_result = food_energy_target - food_energy

    return (
        protein_goal,
        carb_goal,
        fat_goal,
        protein_consumed,
        carb_consumed,
        fat_consumed,
        food_energy_target,
        food_energy,
        food_energy_result,
    )


def macro_goal(macro, unit, int_only=False):
    while True:
        try:
            goal_value = int(input(f"{macro} goal in {unit}: "))
            if int_only and unit != int(goal_value):
                raise ValueError("Please enter an integer value.")
            if goal_value <= 0:
                raise ValueError(f"{macro} must be greater than 0.")

            return goal_value

        except ValueError as e:
            print(e)


def macro_consumed(macro, unit, int_only=False):
    while True:
        try:
            value_consumed = int(input(f"{macro} consumed in {unit}: "))
            if int_only and unit != int(value_consumed):
                raise ValueError("Please enter an integer value.")
            if value_consumed <= 0:
                raise ValueError(f"{macro} must be greater than 0.")

            return value_consumed

        except ValueError as e:
            print(e)


def macro_result(
    protein_goal, carb_goal, fat_goal, protein_consumed, carb_consumed, fat_consumed
):
    remaining_protein = protein_goal - protein_consumed
    remaining_carb = carb_goal - carb_consumed
    remaining_fat = fat_goal - fat_consumed

    return remaining_protein, remaining_carb, remaining_fat


if __name__ == "__main__":
    (
        protein_goal,
        carb_goal,
        fat_goal,
        protein_consumed,
        carb_consumed,
        fat_consumed,
        food_energy_target,
        food_energy,
        food_energy_result,
    ) = get_user_info()

    if (
        protein_consumed is not None
        and carb_consumed is not None
        and fat_consumed is not None
    ):
        remaining_protein, remaining_carb, remaining_fat = macro_result(
            protein_goal,
            carb_goal,
            fat_goal,
            protein_consumed,
            carb_consumed,
            fat_consumed,
        )

    print("\n--- Daily Macros Tracking ---")
    print("Goal:")
    print(f"Protein: {protein_goal}g | Carbohydrates: {carb_goal}g | Fats: {fat_goal}g")
    print("\nConsumed:")
    print(
        f"Protein: {protein_consumed}g | Carbohydrates: {carb_consumed}g | Fats: {fat_consumed}g"
    )
    print("\nMacro Result:")
    print(
        f"Protein: {remaining_protein}g | Carbohydrates: {remaining_carb}g | Fats: {remaining_fat}g"
    )
    print("\nFood Energy Result:")
    print(
        f"Target: {food_energy_target} Calories | Consumed: {food_energy} Calories |  {"Exdeeded:" if food_energy_result < 0 else "Remaining:"} {abs(food_energy_result)} Calories"
    )
