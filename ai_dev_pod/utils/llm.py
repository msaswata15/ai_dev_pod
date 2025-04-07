import requests
import json

def query_ollama(prompt: str, model: str = "llama3", stream=False) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": stream},
        stream=True  # Always stream=True to get line-by-line JSON
    )
    
    output = ""
    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    output += data["response"]
            except json.JSONDecodeError:
                continue  # Skip bad lines
    
    return output.strip()
