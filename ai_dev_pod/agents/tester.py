from utils.prompt_templates import test_prompt
from utils.llm import query_ollama

class Tester:
    def generate_and_run_tests(self, code: str):
        prompt = test_prompt.format(code=code)
        return query_ollama(prompt)
