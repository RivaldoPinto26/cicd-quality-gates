# save_metrics script - to be implemented
import json
import os
from datetime import datetime

# ─── Ler variáveis do GitHub Actions ───────────────────────
pr_number = int(os.environ.get("PR_NUMBER", 0))
branch = os.environ.get("BRANCH_NAME", "unknown")
author = os.environ.get("AUTHOR", "unknown")
tests_passed = os.environ.get("TESTS_PASSED", "false").lower() == "true"
coverage = float(os.environ.get("COVERAGE", 0.0))
ai_decision = os.environ.get("AI_DECISION", "unknown")

# ─── Criar registo novo ─────────────────────────────────────
new_record = {
    "pr": pr_number,
    "branch": branch,
    "date": datetime.now().strftime("%Y-%m-%d"),
    "author": author,
    "tests_passed": tests_passed,
    "coverage": coverage,
    "ai_decision": ai_decision,
    "manual_decision": None,
    "override": None,
    "override_reason": None,
    "bugs_after_merge": None
}

# ─── Ler ficheiro existente ─────────────────────────────────
metrics_path = "data/metrics.json"

try:
    with open(metrics_path, "r") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

# ─── Adicionar registo e guardar ────────────────────────────
data.append(new_record)

with open(metrics_path, "w") as f:
    json.dump(data, f, indent=2)

print(f" Metrics saved for PR #{pr_number} - AI: {ai_decision} - Coverage: {coverage}%")
