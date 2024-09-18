from enum import Enum
from os.path import join, dirname, abspath

PROJECT_ROOT = ""
PROMPTS = join(PROJECT_ROOT, 'prompt_templates')


class ModelType(str, Enum):
    gpt4o = 'gpt-4o-2024-08-06'  # Assuming you are using this specific model
    gpt4o_mini = 'gpt-4o-mini'
    embedding = "text-embedding-3-large"


class PromptTemplate(Enum):
    GET_FOOD_GUIDE_OPTIONS = 'get_food_guide_options.txt'
    GET_FOOD_GUIDE_QUESTIONS = 'get_food_guide_questions.txt'
    GET_FINAL_OUTPUT = 'get_final_output.txt'


def get_prompt_template(prompt_template: PromptTemplate):
    with open(join(PROMPTS, prompt_template.value), "rt") as f:
        return f.read()
