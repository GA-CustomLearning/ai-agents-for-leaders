import os, json
import openai
from github import Github

# — Perception: read the issue event
event_path = os.getenv("GITHUB_EVENT_PATH")
with open(event_path) as f:
    event = json.load(f)
issue = event["issue"]
text = issue["body"]
number = issue["number"]

# — Reasoning: call the LLM
openai.api_key = os.getenv("OPENAI_API_KEY")
resp = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role":"user", "content":
        f"Classify this GitHub issue as one of [Bug, Feature, Chore].\n\nIssue:\n{text}"
    }]
)
label = resp.choices[0].message.content.strip()

# — Action & Feedback: apply label + comment
gh = Github(os.getenv("GITHUB_TOKEN"))
repo = gh.get_repo(os.getenv("GITHUB_REPOSITORY"))
gh_issue = repo.get_issue(number)
try:
    gh_issue.add_to_labels(label)
    gh_issue.create_comment(f"⚙️ I labeled this issue as **{label}** because the LLM classified it accordingly.")
except Exception:
    gh_issue.create_comment("❗️ I couldn’t classify this issue automatically—please review manually.")