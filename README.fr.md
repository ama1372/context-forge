# 🚀 context-forge

**Vous vs. le chat IA qui oublie tout.**

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README.fa.md">فارسی</a> ·
  <a href="README.zh.md">中文</a> ·
  <a href="README.es.md">Español</a> ·
  <a href="README.ar.md">العربية</a> ·
  <a href="README.hi.md">हिन्दी</a> ·
  <b>Français</b> ·
  <a href="README.ru.md">Русский</a> ·
  <a href="README.pt.md">Português</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.ko.md">한국어</a> ·
  <a href="README.tr.md">Türkçe</a> ·
  <a href="README.it.md">Italiano</a> ·
  <a href="README.id.md">Bahasa Indonesia</a> ·
  <a href="README.vi.md">Tiếng Việt</a> ·
  <a href="README.th.md">ไทย</a> ·
  <a href="README.he.md">עברית</a> ·
  <a href="README.uk.md">Українська</a> ·
  <a href="README.pl.md">Polski</a> ·
  <a href="README.nl.md">Nederlands</a> ·
  <a href="README.el.md">Ελληνικά</a> ·
  <a href="README.sv.md">Svenska</a> ·
  <a href="README.ro.md">Română</a>
</p>

---

## Ça vous dit quelque chose ?

- 😤 **Vous codez avec l'IA depuis 3 heures. Le chat atteint sa limite. Tout est perdu.**
- 🤯 **L'IA oublie ce que vous avez décidé il y a deux messages.**
- 💸 **Chaque nouveau message vous collez tout le projet — brûlant des tokens, perdant du temps.**
- 🤖 **L'IA modifie le code à la main, casse des choses, et vous ne savez pas pourquoi.**
- 😴 **Vous passez plus de temps à expliquer qu'à construire.**
- 🚫 **Vous recevez sans cesse "trop de messages, réessayez plus tard".**

**Oui ?** Alors c'est pour vous.

---

## Qu'est-ce que c'est ?

Un **document unique** (`PROJECT_CONTEXT.en.md`) que vous collez dans n'importe quel chat IA — DeepSeek, Claude, ChatGPT, Gemini. Il transforme une IA bavarde en **partenaire de projet discipliné** qui :

- ✅ **Ne perd jamais le contexte** — chaque réponse fait avancer l'état du projet.
- ✅ **Ne modifie jamais votre code à la main** — envoie un patch, vous collez, une commande applique.
- ✅ **Économise des tokens** — ne demande que le fichier nécessaire (`--status`, `--file`), pas tout le projet.
- ✅ **Aide à éviter les limites de messages** — `run.py` vous prévient quand vous envoyez trop vite, et le travail est regroupé en moins de messages.
- ✅ **Ne vous demande jamais 10 commandes** — collez, lancez une commande, terminé.
- ✅ **N'oublie jamais où vous étiez** — le prochain chat reprend exactement où vous l'avez laissé.
- ✅ **Fait travailler plusieurs IA en même temps** — Claude, ChatGPT et DeepSeek sur un même projet sans écraser le travail des autres (mode Équipe).

**Un document. Un outil. Une commande. C'est tout.**

---

## Démarrage rapide — 6 étapes

1. **Enregistrez `PROJECT_CONTEXT.en.md` à la racine de votre projet.**
2. **(Recommandé)** Enregistrez `run.py` dans le même dossier. Pas de `run.py` ? Dites à l'IA : *"Génère run.py depuis la Section 35."*
3. **Configuration unique :** `python run.py --init`
4. **Ouvrez un chat DeepSeek** (ou Claude / ChatGPT / Gemini). Envoyez le **document entier** comme premier message (joignez-le en fichier si le chat le permet). Dites : *« Nouveau projet. Mon objectif : <une ligne>. »* Le document est volumineux (~530 Ko, environ 150k tokens) ; si le chat le refuse, envoyez une copie allégée créée avec `python run.py --slim-context --to PROJECT_CONTEXT.slim.md` (~360 Ko), ou ajoutez `--profile moderate` (~260 Ko).
5. **Boucle :** l'IA envoie un bloc → copiez dans `_work/input.txt` → lancez `python run.py` → renvoyez `_work/output.txt`. Répétez.
6. **Gardez la boucle jusqu'à la fin du projet.** Ne laissez pas l'IA vous en sortir — pas de commandes shell dans le chat, pas de scripts rapides. La réponse est toujours : *"Mets-le dans input.txt."*

> **Astuce :** si l'IA dérive - suggère des commandes shell dans le chat, saute le contexte - dites : **« Contexte du projet, s'il te plaît. »**

---


## Guide complet du débutant (résumé)

1. Installez **Python 3.10+** depuis python.org (sur Windows, cochez "Add to PATH").
2. (Optionnel) Installez **VS Code**.
3. Téléchargez `PROJECT_CONTEXT.en.md` et `run.py`, mettez-les dans un dossier, ouvrez-le dans VS Code.
4. Terminal : `python run.py` → le dossier `_work/` est créé.
5. Dans DeepSeek, envoyez `PROJECT_CONTEXT.en.md` comme premier message (ou joignez-le en fichier) et donnez votre objectif. Trop long pour votre chat ? Voir l'étape 4 du démarrage rapide (`--slim-context`).
6. **Boucle :** l'IA envoie un bloc → copiez dans `_work/input.txt` → lancez `python run.py` → renvoyez `_work/output.txt`.
7. Tous les 10–20 messages, rappelez votre projet à l'IA.
8. Si l'IA dérive, dites : **« Contexte du projet, s'il te plaît. »**

Version complète (anglais) : voir `README.md`.

## Ce que vous obtenez

| Avant | Après |
|-------|-------|
| Le chat perd le contexte | Le contexte survit à chaque message |
| Vous collez tout le projet à chaque message | L'IA ne demande que les fichiers utiles |
| L'IA devine | L'IA sait |
| 10 commandes par changement | 1 commande par changement |
| Blocages « trop de messages » | Alertes de vitesse et messages moins nombreux, plus complets |
| "Où en étions-nous ?" | "Voici le prochain patch." |

**Moins de tokens. Un contexte qui survit à un nouveau chat. Aucune modification à la main.**

---

## 🤝 Plusieurs IA en même temps — mode Équipe (nouveau en v2.1)

Faites travailler Claude, ChatGPT, DeepSeek et des agents de code **sur le même projet en même temps**. Chacun vous répond dans son propre chat — et aucun ne peut écraser le travail d'un autre.

- **Un tableau partagé** dans `.git/` — jamais poussé, visible par toutes les IA.
- **Réservation de fichiers** — chaque IA réserve exactement les fichiers qu'elle va modifier ; si deux veulent le même, une seule l'obtient.
- **Imposé, pas seulement conseillé** — `run.py` refuse tout patch qui touche un fichier non réservé.
- **Un coordinateur, plusieurs exécutants** — une IA relit et fusionne, sans jamais valider son propre travail ; les décisions importantes restent les vôtres.
- **Le travail continue pendant votre pause** — validez une liste de tâches, lancez `team away on`, et les agents installés prennent la tâche libre suivante ; `run.py` refuse tout push avant votre retour, et `team pause` arrête tout le monde.
- **Chat ou agent installé** — les IA de chat font tout via `input.txt` (`#@CLAIM:`) ; les agents lancent les commandes eux-mêmes.

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

Règles complètes : sections 0-C-47 et 0-C-48 de `PROJECT_CONTEXT.en.md`.

---

## Fonctionne avec n'importe quel langage

Rust, Python, Node, Go, C++, n'importe quoi. Vous dites à `run.py` une fois comment construire et tester votre projet — le protocole est le même pour tous les langages.

---

## Langue du document

Le document de règles est **en anglais uniquement** — pour que chaque IA l'analyse de manière identique et qu'il n'y ait qu'une seule source de vérité.

**Mais la conversation avec votre IA est dans votre langue.** Écrivez juste votre premier message en français, persan, arabe, chinois — l'IA répond dans la même langue. Le document est universel.

---

## Fichiers fournis

- `PROJECT_CONTEXT.en.md` — le document de règles (collez-le dans votre IA)
- `run.py` — l'outil (téléchargez-le depuis ce dépôt, ou l'IA le reconstruit à partir de la section 35)
- `README.md` + traductions — cette page, multilingue
- `LICENSE` — MIT, faites ce que vous voulez

---

## FAQ

**Dois-je savoir coder ?**
Pas beaucoup. Si vous pouvez coller un message et lancer une commande, vous pouvez l'utiliser.

**Quelle IA fonctionne le mieux ?**
N'importe quel modèle de chat performant : DeepSeek, Claude, ChatGPT, Gemini. Tous dérivent dans les longs chats — dites alors « Contexte du projet, s'il vous plaît. » Pour plusieurs IA en même temps, ou du travail en votre absence, utilisez un agent installé (Claude Code, Codex, Cursor…).

**Est-ce gratuit ?**
Le document et l'outil sont MIT. L'API IA est facturée par votre fournisseur.

**Et si quelque chose casse ?**
Si le dossier utilise git (recommandé), `run.py` fait un commit de chaque patch appliqué, et `python run.py revert P<id>` revient à l'état d'avant ce patch (les patches suivants sont aussi annulés).

---

## Prêt ?

1. **[Téléchargez `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Collez-le dans votre chat IA
3. Dites : *"Je veux construire X. Commence."*

**C'est tout. Arrêtez de vous battre avec votre IA. Commencez à construire.**

---

*Fait pour ceux qui veulent livrer, pas surveiller une fenêtre de chat.*

---

## 🌐 Un seul document pour les IA de chat et les agents installés

Ce protocole fonctionne de la même façon que vous utilisiez :

1. **Des chats web** (ChatGPT, Claude, DeepSeek, Gemini) avec la boucle `input.txt` / `output.txt`.
2. **Des agents de code installés** (Claude Code, Codex, Cursor et d'autres) qui lisent le dépôt et lancent les commandes eux-mêmes.

- **Aucune perte de contexte** — l'état du projet vit toujours dans le document.
- **Ouvrez un nouveau chat quand vous voulez** — continuez sans tout réexpliquer.
- **Moins de tokens** — l'IA ne demande que les fichiers nécessaires (`--status`, `--file`).
- **Plusieurs IA en même temps** — le mode Équipe évite les collisions (voir plus haut).
