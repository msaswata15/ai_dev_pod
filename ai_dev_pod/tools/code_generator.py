def wrap_code_in_template(code: str, language: str = "python") -> str:
    return f"```{language}\n{code.strip()}\n```"
