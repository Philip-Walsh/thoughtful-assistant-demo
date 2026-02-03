---
title: Thoughtful Assist Demo
emoji: 💡
colorFrom: indigo
colorTo: green
sdk: gradio
sdk_version: 5.34.2
app_file: app.py
pinned: false
short_description: A simple customer support AI agent for Thoughtful AI
---

# Thoughtful Assist Demo

Thoughtful Assist demo was designed to for the [Thoughtful AI Technical Screening](https://thoughtfulautomation.notion.site/AI-Technical-Screen-d4d381a8c38d40fc9287cdb6c4f9992a) it's a minimal customer support agent that answers common questions about Thoughtful AI using semantic retrieval, with an LLM fallback for unmatched queries (Fallback uses DistilGPT2, a generic text generator, so when no Q&A match is found it may produce off-topic or nonsensical responses).

View it on Hugging Face
**(DEMO)[todo]**

---

## Steps to run locally

```sh
# Clone the repository
git clone https://github.com/Philip-Walsh/thoughtful-assistant-demo
cd thoughtful-assist

# Create and activate the env
python -m venv venv
source venv/bin/activate

# Install dependencies:
pip install -r requirements.txt


# Run it
python app.py

```
