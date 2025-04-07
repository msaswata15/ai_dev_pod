import subprocess
import requests

def query_ollama(prompt: str, model: str = "llama3", stream=False) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": stream}
    )
    output = ""
    for line in response.iter_lines():
        if line:
            output += line.decode("utf-8")
    return output
