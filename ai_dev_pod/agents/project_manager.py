class ProjectManager:
    def __init__(self):
        pass

    def summarize_status(self, stories: str, design: str, code: str, tests: str) -> str:
        return f"""
# 📊 Project Status Summary

---

## 📚 User Stories
{stories}

---

## 🧩 Design Document
{design}

---

## 💻 Generated Code
```python
{code}
```

{tests}


"""
