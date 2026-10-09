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
  <a href="README.it.md">Italiano</a>
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

Un **document unique** (`PROJECT_CONTEXT.md`) que vous collez dans n'importe quel chat IA — DeepSeek, Claude, ChatGPT, Gemini. Il transforme une IA bavarde en **partenaire de projet discipliné** qui :

- ✅ **Ne perd jamais le contexte** — chaque réponse fait avancer l'état du projet.
- ✅ **Ne modifie jamais votre code à la main** — envoie un patch, vous collez, une commande applique.
- ✅ **Ne brûle jamais de tokens** — demande seulement le fichier dont il a besoin, pas tout le projet.
- ✅ **Ne bloque jamais votre compte** — protocole anti-limite intégré.
- ✅ **Ne vous demande jamais 10 commandes** — collez, lancez une commande, terminé.
- ✅ **N'oublie jamais où vous étiez** — le prochain chat reprend exactement où vous l'avez laissé.

**Un document. Un outil. Une commande. C'est tout.**

---

## Comment ça marche (3 étapes)

### 1. Récupérez le document
Téléchargez [`PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md) depuis ce dépôt.

### 2. Collez-le dans votre chat IA
Ouvrez un nouveau chat avec DeepSeek (ou Claude, ChatGPT, Gemini). Collez le document entier comme **premier message**. Écrivez une ligne sur ce que vous voulez construire.

### 3. Suivez l'IA
L'IA vous donne `run.py` (un petit outil Python). Enregistrez-le. À partir de là :

> **Vous collez → lancez `python run.py` → renvoyez la sortie.**

C'est tout le workflow. Pour toujours.

---

## Ce que vous obtenez

| Avant | Après |
|-------|-------|
| Le chat perd le contexte | Le contexte survit à chaque message |
| 5000 tokens par réponse | ~300 tokens par réponse |
| L'IA devine | L'IA sait |
| 10 commandes par changement | 1 commande par changement |
| Compte bloqué | Compte sûr |
| "Où en étions-nous ?" | "Voici le prochain patch." |

**40–80% de tokens en moins. Zéro perte de contexte. Zéro édition manuelle.**

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
- `run.py` — l'outil (l'IA vous le donne à la première utilisation)
- `README.md` + traductions — cette page, multilingue
- `LICENSE` — MIT, faites ce que vous voulez

---

## FAQ

**Dois-je savoir coder ?**
Pas beaucoup. Si vous pouvez coller un message et lancer une commande, vous pouvez l'utiliser.

**Quelle IA fonctionne le mieux ?**
DeepSeek — suit le protocole le plus précisément. Claude, ChatGPT et Gemini fonctionnent aussi.

**Est-ce gratuit ?**
Le document et l'outil sont MIT. L'API IA est facturée par votre fournisseur.

**Et si quelque chose casse ?**
Tout est versionné avec git. Revenez en arrière avec une commande. Le document explique comment.

---

## Prêt ?

1. **[Téléchargez `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Collez-le dans votre chat IA
3. Dites : *"Je veux construire X. Commence."*

**C'est tout. Arrêtez de vous battre avec votre IA. Commencez à construire.**

---

*Fait pour ceux qui veulent livrer, pas surveiller une fenêtre de chat.*