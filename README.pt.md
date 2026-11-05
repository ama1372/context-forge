# 🚀 context-forge

**Você vs. o chat de IA que esquece tudo.**

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README.fa.md">فارسی</a> ·
  <a href="README.zh.md">中文</a> ·
  <a href="README.es.md">Español</a> ·
  <a href="README.ar.md">العربية</a> ·
  <a href="README.hi.md">हिन्दी</a> ·
  <a href="README.fr.md">Français</a> ·
  <a href="README.ru.md">Русский</a> ·
  <b>Português</b> ·
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

## Parece familiar?

- 😤 **Você programou com IA por 3 horas. O chat atinge seu limite. Tudo se perde.**
- 🤯 **A IA esquece o que você decidiu duas mensagens atrás.**
- 💸 **Cada nova mensagem você cola o projeto inteiro — queimando tokens, perdendo tempo.**
- 🤖 **A IA edita o código à mão, quebra coisas, e você não sabe por quê.**
- 😴 **Você gasta mais tempo explicando do que construindo.**
- 🚫 **Você recebe sempre "mensagens demais, tente depois".**

**Sim?** Então isto é para você.

---

## O que é?

Um **documento único** (`PROJECT_CONTEXT.en.md`) que você cola em qualquer chat de IA — DeepSeek, Claude, ChatGPT, Gemini. Ele transforma uma IA tagarela em um **parceiro disciplinado de projeto** que:

- ✅ **Nunca perde o contexto** — cada resposta leva o estado do projeto adiante.
- ✅ **Nunca edita seu código à mão** — envia um patch, você cola, um comando aplica.
- ✅ **Economiza tokens** — pede só o arquivo de que precisa (`--status`, `--file`), não o projeto inteiro.
- ✅ **Ajuda a evitar limites de mensagens** — o `run.py` avisa quando você envia rápido demais, e o trabalho é agrupado em menos mensagens.
- ✅ **Nunca pede 10 comandos** — cola, roda um, pronto.
- ✅ **Nunca esquece onde vocês estavam** — o próximo chat continua exatamente de onde parou.
- ✅ **Permite que várias IAs trabalhem ao mesmo tempo** — Claude, ChatGPT e DeepSeek no mesmo projeto sem sobrescrever o trabalho umas das outras (Modo equipe).

**Um documento. Uma ferramenta. Um comando. Só isso.**

---

## Início rápido — 6 passos

1. **Salve `PROJECT_CONTEXT.en.md` na raiz do projeto.**
2. **(Recomendado)** Salve `run.py` na mesma pasta. Sem `run.py`? Diga à IA: *"Gere run.py da Seção 35."*
3. **Configure uma vez:** `python run.py --init`
4. **Abra um chat do DeepSeek** (ou Claude / ChatGPT / Gemini). Envie o **documento inteiro** como primeira mensagem (anexe como arquivo se o chat permitir). Diga: *"Projeto novo. Meu objetivo: <uma linha>."* O documento é grande (~530 KB, cerca de 150 mil tokens); se o chat recusar, envie uma cópia mais leve criada com `python run.py --slim-context --to PROJECT_CONTEXT.slim.md` (~360 KB), ou adicione `--profile moderate` (~260 KB).
5. **Loop:** a IA envia um bloco → copie para `_work/input.txt` → execute `python run.py` → devolva `_work/output.txt`. Repita.
6. **Mantenha o loop até terminar o projeto.** Não deixe a IA te tirar — sem comandos shell no chat, sem scripts rápidos. A resposta é sempre: *"Coloque em input.txt."*

> **Dica:** se a IA desviar - sugere comandos shell no chat, pula o contexto - diga: **"Contexto do projeto, por favor."**

---


## Guia completo para iniciantes (resumo)

1. Instale **Python 3.10+** do python.org (no Windows, marque "Add to PATH").
2. (Opcional) Instale **VS Code**.
3. Baixe `PROJECT_CONTEXT.en.md` e `run.py`, coloque numa pasta, abra no VS Code.
4. No terminal: `python run.py` → a pasta `_work/` é criada.
5. No DeepSeek, envie `PROJECT_CONTEXT.en.md` como primeira mensagem (ou anexe como arquivo) e diga seu objetivo. Longo demais para o seu chat? Veja o passo 4 do início rápido (`--slim-context`).
6. **Loop:** a IA envia um bloco → copie para `_work/input.txt` → rode `python run.py` → envie `_work/output.txt` de volta.
7. A cada 10–20 mensagens, lembre a IA do seu projeto.
8. Se a IA desviar, diga: **"Contexto do projeto, por favor."**

Versão completa (inglês): veja `README.md`.

## O que você ganha

| Antes | Depois |
|-------|--------|
| O chat perde o contexto | O contexto sobrevive a cada mensagem |
| Você cola o projeto inteiro a cada mensagem | A IA pede só os arquivos necessários |
| A IA adivinha | A IA sabe |
| 10 comandos por mudança | 1 comando por mudança |
| Bloqueios por "mensagens demais" | Avisos de velocidade e menos mensagens, mais completas |
| "Onde estávamos?" | "Aqui está o próximo patch." |

**Menos tokens. Contexto que sobrevive a um chat novo. Sem edição à mão.**

---

## 🤝 Várias IAs ao mesmo tempo — Modo equipe (novo na v2.1)

Coloque Claude, ChatGPT, DeepSeek e agentes de programação **no mesmo projeto ao mesmo tempo**. Cada um responde no seu próprio chat — e nenhum consegue sobrescrever o trabalho de outro.

- **Um quadro compartilhado** dentro de `.git/` — nunca é enviado ao remoto e todas as IAs o veem.
- **Reserva de arquivos** — cada IA reserva exatamente os arquivos que vai editar; se duas quiserem o mesmo, só uma consegue.
- **Obrigatório, não só um conselho** — o `run.py` recusa qualquer patch que toque um arquivo não reservado.
- **Um coordenador, vários trabalhadores** — uma IA revisa e integra, e nunca aprova o próprio trabalho; as decisões importantes são suas.
- **O trabalho continua enquanto você descansa** — aprove uma lista de tarefas, rode `team away on` e os agentes instalados pegam a próxima tarefa livre; o `run.py` recusa qualquer push até você voltar, e `team pause` para todos.
- **Chat ou agente instalado** — IAs de chat fazem tudo pelo `input.txt` (`#@CLAIM:`); agentes rodam os comandos sozinhos.

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

Regras completas: seções 0-C-47 e 0-C-48 do `PROJECT_CONTEXT.en.md`.

---

## Funciona com qualquer linguagem

Rust, Python, Node, Go, C++, o que for. Você diz ao `run.py` uma vez como construir e testar seu projeto — o protocolo é o mesmo para todas as linguagens.

---

## Idioma do documento

O documento de regras é **apenas em inglês** — para que toda IA o analise de forma idêntica e haja uma única fonte de verdade.

**Mas a conversa com sua IA é no seu idioma.** Basta escrever sua primeira mensagem em português, persa, árabe, chinês — a IA responde no mesmo idioma. O documento é universal.

---

## Arquivos que você recebe

- `PROJECT_CONTEXT.en.md` — o documento de regras (cole isto na sua IA)
- `run.py` — a ferramenta (baixe deste repositório, ou a IA a reconstrói a partir da seção 35)
- `README.md` + traduções — esta página, multilíngue
- `LICENSE` — MIT, faça o que quiser

---

## FAQ

**Preciso saber programar?**
Não muito. Se você consegue colar uma mensagem e rodar um comando, dá para usar.

**Qual IA funciona melhor?**
Qualquer modelo de chat forte: DeepSeek, Claude, ChatGPT, Gemini. Todos se desviam em chats longos — então diga "Contexto do projeto, por favor." Para várias IAs ao mesmo tempo, ou trabalho enquanto você está fora, use um agente instalado (Claude Code, Codex, Cursor…).

**É grátis?**
O documento e a ferramenta são MIT. A API da IA é o que seu provedor cobrar.

**E se algo quebrar?**
Se a pasta usa git (recomendado), o `run.py` faz commit de cada patch aplicado, e `python run.py revert P<id>` volta ao estado anterior a esse patch (os patches posteriores também são desfeitos).

---

## Pronto?

1. **[Baixe `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Cole no seu chat de IA
3. Diga: *"Quero construir X. Comece."*

**Só isso. Pare de brigar com sua IA. Comece a construir.**

---

*Feito para quem quer entregar, não cuidar de uma janela de chat.*

---

## 🌐 Um documento para IAs de chat e agentes instalados

Este protocolo funciona do mesmo jeito, seja qual for o uso:

1. **Chats na web** (ChatGPT, Claude, DeepSeek, Gemini) com o ciclo `input.txt` / `output.txt`.
2. **Agentes de programação instalados** (Claude Code, Codex, Cursor e outros) que leem o repositório e rodam comandos sozinhos.

- **Sem perda de contexto** — o estado do projeto vive sempre no documento.
- **Comece um chat novo quando quiser** — continue sem explicar tudo de novo.
- **Menos tokens** — a IA pede só os arquivos de que precisa (`--status`, `--file`).
- **Várias IAs ao mesmo tempo** — o Modo equipe evita colisões (veja acima).
