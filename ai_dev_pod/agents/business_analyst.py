from utils.prompt_templates import story_prompt
from utils.llm import query_ollama

class BusinessAnalyst:
    def generate_user_stories(self, requirements: str):
        prompt = story_prompt.format(requirements=requirements)
        return query_ollama(prompt)
