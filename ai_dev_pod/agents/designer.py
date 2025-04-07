from utils.prompt_templates import design_prompt
from utils.llm import query_ollama

class Designer:
    def create_design(self, user_stories: str):
        prompt = design_prompt.format(user_stories=user_stories)
        return query_ollama(prompt)
