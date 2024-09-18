from dotenv import load_dotenv

load_dotenv()
from src.utils import get_food_guide_options, get_food_guide_questions, get_final_output


if __name__ == "__main__":
    user_input = "I want to gain bulk what foods are good."  # User's initial request

    # Step 1: Get food guide options (dynamically generated)
    food_guide_options = get_food_guide_options(user_input)
    print("Available Options:")
    for option in food_guide_options.options:
        print(f"- {option.name}: {option.description}")

    # Step 2: User selects options (replace with actual user selection)
    selected_options = [option.name for option in food_guide_options.options]  # Example selection

    # Step 3: Get questions based on selected options
    food_guide_questions = get_food_guide_questions(selected_options)
    print("\nQuestions to Ask:")
    for question_obj in food_guide_questions.questions:
        print(f"- {question_obj.question}")
        print(f"  ({question_obj.description})")

    # Step 4: User provides answers to questions (replace with actual user answers)
    user_answers = [
        "Around 2,500 calories per day.",
        "I usually eat 3 main meals and 1 snack.",
        "I don’t have any dietary restrictions, but I prefer to avoid too much red meat.",
        "I’m aiming for a 500-calorie surplus.",
        "I work out in the evenings, around 6 PM, and I usually wake up around 7 AM."
    ]

    # Step 5: Get final output
    final_output = get_final_output(selected_options, user_answers)
    print("\nFinal Output:")
    print(final_output.model_dump_json(indent=2))