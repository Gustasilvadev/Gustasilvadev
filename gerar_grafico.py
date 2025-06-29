import requests
import matplotlib.pyplot as plt
from collections import Counter

# --- CONFIG ---
GITHUB_USERNAME = "Gustasilvadev"

# --- API ---
url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
response = requests.get(url)
repos = response.json()

# --- Contar linguagens ---
languages = [repo["language"] for repo in repos if repo["language"]]
count = Counter(languages)

# --- Gráfico ---
labels = list(count.keys())
sizes = list(count.values())

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
plt.axis("equal")
plt.title(f"Linguagens mais usadas por @{GITHUB_USERNAME}")

# --- Salvar imagem na pasta output/ ---
import os
os.makedirs("output", exist_ok=True)

plt.savefig("output/linguagens.png", dpi=300, bbox_inches="tight")
plt.savefig("output/linguagens.svg", format="svg", bbox_inches="tight")

print("✅ Gráfico gerado com sucesso em /output/")