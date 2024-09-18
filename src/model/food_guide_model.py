from typing import List, Dict, Union, Optional
from pydantic import BaseModel, Field

class FoodGuideOption(BaseModel):
    """Represents a user-selectable option for customizing the output of a food guide request."""
    name: str = Field(..., description="The name of the option (e.g., 'Caloric Breakdown', 'Meal Timing and Frequency').")
    description: str = Field(..., description="A description of what the option provides.")


class FoodGuideQuestion(BaseModel):
    """Represents a question with a short description."""
    question: str = Field(..., description="The question to ask the user.")
    description: str = Field(..., description="A short description explaining the purpose of the question.")


class FoodGuideQuestions(BaseModel):
    """Represents a list of questions to ask the user to refine the food guide output."""
    questions: List[FoodGuideQuestion] = Field(..., description="A list of questions with descriptions.")


class FoodGuideFinalOutput(BaseModel):
    """Represents the final structured output of the food guide."""
    caloric_breakdown: Optional[Dict[str, str]] = Field(None, description="Caloric breakdown of meals.")
    meal_timing_and_frequency: Optional[str] = Field(None, description="Guidance on meal timing and frequency.")
    high_protein_foods: Optional[List[str]] = Field(None, description="List of high-protein foods.")
    carbohydrate_rich_foods: Optional[List[str]] = Field(None, description="List of carbohydrate-rich foods.")
    healthy_fats: Optional[List[str]] = Field(None, description="List of healthy fats.")
    sample_meal_plan: Optional[Dict[str, List[str]]] = Field(None, description="Sample meal plan.")
    # Add other fields as needed for different output types

class FoodGuideOptions(BaseModel):
    """Represents a list of food guide options."""
    options: List[FoodGuideOption] = Field(..., description="A list of food guide options.")