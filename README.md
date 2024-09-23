## Lexri AI

**Lexri AI** is a project that extracts structured information from conversations between a user and an assistant, specifically in the context of food and nutrition guidance. It leverages OpenAI's language models to understand user requests, provide personalized recommendations, and generate structured output based on user interactions.

**Features:**

- **Dynamic Food Guide Options:** Generates a list of food guide options based on the user's initial request (e.g., weight loss, muscle gain).
- **Personalized Questions:** Asks relevant questions to gather more information about the user's needs and preferences.
- **Structured Output:** Provides a structured output based on the user's selections and answers, including information like caloric breakdown, meal timing, food recommendations, and sample meal plans.
- **Customizable Conditions:** Allows you to add conditions to the AI's responses, such as restricting the use of certain words or phrases.

**How it works:**

1. The user provides an initial request related to food and nutrition.
2. Lexri AI uses OpenAI's language model to generate a list of relevant food guide options.
3. The user selects the options that best fit their needs.
4. Based on the selected options, Lexri AI generates personalized questions to gather more information.
5. The user provides answers to the questions.
6. Lexri AI uses the user's selections and answers to generate a structured output containing personalized recommendations and information.

**Getting Started:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cl0ver012/lexri_ai
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure OpenAI API key:**
   - Create a `.env` file in the project root directory.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=<your-api-key>
     ```
4. **Run the main script:**
   ```bash
   python main.py
   ```

**Customization:**

- You can customize the prompt templates in the `prompt_templates/` directory to modify the AI's behavior.
- You can add conditions to the AI's responses by passing a `condition` string to the relevant functions in `src/utils.py`.
- You can extend the project by adding new food guide options, questions, and output fields.
