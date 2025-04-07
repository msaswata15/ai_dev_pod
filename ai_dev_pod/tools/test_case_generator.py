def format_test_cases(test_cases: str) -> str:
    lines = test_cases.split('\n')
    return "\n".join([f"- {line.strip()}" for line in lines if line.strip()])
