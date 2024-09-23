from typing import List
from src.model.food_guide_model import (
    FoodGuideOption,
    FoodGuideQuestion,
    FoodGuideQuestions,
    FoodGuideFinalOutput,
    FoodGuideOptions
)
from openai import OpenAI
from config import get_prompt_template, PromptTemplate, ModelType

client = OpenAI()

def get_food_guide_options(user_input: str, condition: str = None) -> FoodGuideOptions:
    """Generates a list of food guide options using ChatGPT based on the user's input."""
    system_message = "You are a helpful food guide assistant."
    if condition:
        system_message += f"\nHere are some of the conditions that you must keep while generating a response:\n{condition}"

    prompt = get_prompt_template(PromptTemplate.GET_FOOD_GUIDE_OPTIONS).replace(
        "user_input", user_input
    )

    response = client.beta.chat.completions.parse(
        model=ModelType.gpt4o.value,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ],
        response_format=FoodGuideOptions
    )

    return response.choices[0].message.parsed


def get_food_guide_questions(selected_options: List[str], condition: str = None) -> FoodGuideQuestions:
    """Gets the list of questions with descriptions based on selected options using ChatGPT."""
    system_message = "You are a helpful food guide assistant."
    if condition:
        system_message += f"\nHere are some of the conditions that you must keep while generating a response:\n{condition}"

    selected_options_str = ", ".join(selected_options)
    prompt = get_prompt_template(PromptTemplate.GET_FOOD_GUIDE_QUESTIONS).replace(
        "selected_options", selected_options_str
    )
    response = client.beta.chat.completions.parse(
        model=ModelType.gpt4o.value,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ],
        response_format=FoodGuideQuestions,
    )
    return response.choices[0].message.parsed


def get_final_output(selected_options: List[str], user_answers: List[str], condition: str = None) -> FoodGuideFinalOutput:
    """Gets the final output based on selected options and user answers using ChatGPT."""
    system_message = "You are a helpful food guide assistant."
    if condition:
        system_message += f"\nHere are some of the conditions that you must keep while generating a response:\n{condition}"

    # Get the questions within the function's scope
    food_guide_questions = get_food_guide_questions(selected_options, condition)

    user_answers_str = "\n".join(
        [f'{q.question}: "{a}"' for q, a in zip(food_guide_questions.questions, user_answers)]
    )
    prompt_template = get_prompt_template(PromptTemplate.GET_FINAL_OUTPUT)
    prompt = f"{prompt_template}".replace("user_answers", user_answers_str)

    response = client.beta.chat.completions.parse(
        model=ModelType.gpt4o.value,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ],
        response_format=FoodGuideFinalOutput,
    )

    return response.choices[0].message.parsed