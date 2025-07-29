# Agentic AI Lab

A GitHub Action that demos an AI agent:

1. **Perceive** new issues  
2. **Reason** (classify via LLM)  
3. **Act** (apply a label)  
4. **Feedback** (comment rationale)

## Setup

1. Fork this repo.  
2. In your fork, go to **Settings → Secrets → Actions** and add your `OPENAI_API_KEY`.  
3. Open an issue in your fork to watch the Action run.

## Development

```bash
git clone git@github.com:<you>/agentic-ai-lab.git
cd agentic-ai-lab
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
Edit agent.py to customize labels, prompts, or fallback logic.

Testing
Push any change → watch Actions → Agentic AI Labeler

Open a new GitHub issue → see it auto-labeled + commented.

markdown
Copy
Edit

---

##  Ready to Run

1. **Fork** & **clone**.  
2. **Add** `OPENAI_API_KEY` secret.  
3. **Push** this structure to `main`.  
4. **Open** a test issue—and voilà, your AI agent labels and comments!