from dotenv import load_dotenv

load_dotenv()
from src.utils import get_food_guide_options, get_food_guide_questions, get_final_output


if __name__ == "__main__":
    user_input = "I want to gain bulk what foods are good."  # User's initial request
    condition = "Please do not use the letter 'r' in any of your output responses."  # Example condition

    # Step 1: Get food guide options (dynamically generated)
    food_guide_options = get_food_guide_options(user_input, condition)
    print("Available Options:")
    for option in food_guide_options.options:
        print(f"- {option.name}: {option.description}")

    # Step 2: User selects options (replace with actual user selection)
    selected_options = [option.name for option in food_guide_options.options]  # Example selection

    # Step 3: Get questions based on selected options
    food_guide_questions = get_food_guide_questions(selected_options, condition)
    print("\nQuestions to Ask:")
    for question_obj in food_guide_questions.questions:
        print(f"- {question_obj.question}")
        print(f"  ({question_obj.description})")

    # Step 4: User provides answers to questions (replace with actual user answers)
    user_answers = [
        "Around 2,500 caloies pe day.",
        "I usually eat 3 main meals and 1 snack.",
        "I don’t have any dietay estrictions, but I pefe to avoid too much ed meat.",
        "I’m aiming fo a 500-caloie suplus.",
        "I wok out in the evenings, aound 6 PM, and I usually wake up aound 7 AM."
    ]

    # Step 5: Get final output
    final_output = get_final_output(selected_options, user_answers, condition)
    print("\nFinal Output:")
    print(final_output.model_dump_json(indent=2))