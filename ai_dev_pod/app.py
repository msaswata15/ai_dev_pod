import streamlit as st
from main import DevPod
import time

# Streamlit page setup
st.set_page_config(page_title="AI Dev Pod", layout="wide")
st.title("🤖 AI-Powered Virtual Development Pod")
st.markdown("""
Simulate a full-stack software development project using AI agents.
Powered by **OpenLLaMA** via **Ollama**, this pod includes:
- 🧠 Business Analyst (User Stories)
- 🎨 Designer (Design Artifacts)
- 👨‍💻 Developer (Code)
- 🧪 Tester (Test Cases & Execution)
""")

# Input area
requirements = st.text_area("📝 Enter high-level business requirements here:")

if st.button("🚀 Run AI DevPod"):
    if not requirements.strip():
        st.warning("⚠️ Please enter some requirements before running the pod.")
    else:
        with st.spinner("🔄 Running the AI DevPod..."):
            pod = DevPod()
            time.sleep(1)  # Simulate delay for realistic UX
            output = pod.run(requirements)

            st.success("✅ Development complete!")
            st.markdown("### 🧾 Generated Artifacts:")
            st.markdown(output)
