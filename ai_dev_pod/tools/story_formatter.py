def format_user_stories(raw_stories: str) -> str:
    lines = raw_stories.split('\n')
    formatted = []
    for line in lines:
        if line.strip():
            formatted.append(f"- {line.strip()}")
    return '\n'.join(formatted)
