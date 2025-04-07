story_prompt = """
You are a business analyst. Given the following high-level requirements:

"{requirements}"

Generate detailed user stories.
"""

design_prompt = """
As a designer, create software design components for the following user stories:

"{user_stories}"
"""

code_prompt = """
As a developer, write Python code based on the following user stories and design:

User Stories:
"{user_stories}"

Design:
"{design}"
"""

test_prompt = """
As a QA engineer, write test cases for the following code:

"{code}"
"""
