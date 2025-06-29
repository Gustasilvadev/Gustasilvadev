import requests
import matplotlib.pyplot as plt
from collections import Counter
import os

GITHUB_USERNAME = "Gustasilvadev"

url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
response = requests.get(url)
repos = response.json()

languages = [repo["language"] for repo in repos if repo["language"]]
count = Counter(languages)

labels = list(count.keys())
sizes = list(count.values())

# Configurações de estilo
plt.style.use('dark_background')  # fundo escuro automático (preto)
fig, ax = plt.subplots(figsize=(8, 6), facecolor='#0d1117')  # fundo do gráfico

# Ajusta as cores das labels e percentuais
def func(pct, allvals):
    return f"{pct:.1f}%"

wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct=lambda pct: func(pct, sizes),
    startangle=140,
    textprops={'color':"white", 'fontsize':14, 'weight':'bold'}
)

# Configura fundo do texto das labels e porcentagens
for txt in texts + autotexts:
    txt.set_color('white')

ax.axis('equal')
plt.title(f"Linguagens mais usadas por @{GITHUB_USERNAME}", color='white', fontsize=16, weight='bold')

os.makedirs("output", exist_ok=True)
plt.savefig("output/linguagens.svg", format="svg", bbox_inches="tight", facecolor=fig.get_facecolor())
plt.savefig("output/linguagens.png", dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())

print("✅ Gráfico gerado com fundo escuro e texto branco em /output/")