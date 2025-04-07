from agents.business_analyst import BusinessAnalyst
from agents.designer import Designer
from agents.developer import Developer
from agents.tester import Tester
from agents.project_manager import ProjectManager


class DevPod:
    def __init__(self):
        # Initialize all agents
        self.analyst = BusinessAnalyst()
        self.designer = Designer()
        self.developer = Developer()
        self.tester = Tester()
        self.manager = ProjectManager()

    def run(self, requirements: str) -> str:
        print("📋 Generating user stories...")
        user_stories = self.analyst.generate_user_stories(requirements)
        print("✅ User stories done.")

        print("🧠 Creating design...")
        design = self.designer.create_design(user_stories)
        print("✅ Design done.")

        print("💻 Writing code...")
        code = self.developer.write_code(user_stories, design)
        print("✅ Code generation done.")

        print("🧪 Running tests...")
        tests = self.tester.generate_and_run_tests(code)
        print("✅ Tests done.")

        print("📊 Summarizing project...")
        status = self.manager.summarize_status(user_stories, design, code, tests)
        print("✅ Summarization done.")
        return status
