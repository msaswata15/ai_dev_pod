from utils.prompt_templates import code_prompt
from utils.llm import query_ollama

class Developer:
    def write_code(self, user_stories: str, design: str):
        prompt = code_prompt.format(user_stories=user_stories, design=design)
        return query_ollama(prompt)
