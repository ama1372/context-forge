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
  <a href="README.it.md">Italiano</a>
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

Um **documento único** (`PROJECT_CONTEXT.md`) que você cola em qualquer chat de IA — DeepSeek, Claude, ChatGPT, Gemini. Ele transforma uma IA tagarela em um **parceiro disciplinado de projeto** que:

- ✅ **Nunca perde o contexto** — cada resposta leva o estado do projeto adiante.
- ✅ **Nunca edita seu código à mão** — envia um patch, você cola, um comando aplica.
- ✅ **Nunca queima tokens** — pede só o arquivo de que precisa, não o projeto inteiro.
- ✅ **Nunca bloqueia sua conta** — protocolo anti-limite embutido.
- ✅ **Nunca pede 10 comandos** — cola, roda um, pronto.
- ✅ **Nunca esquece onde vocês estavam** — o próximo chat continua exatamente de onde parou.

**Um documento. Uma ferramenta. Um comando. Só isso.**

---

## Como funciona (3 passos)

### 1. Baixe o documento
Baixe [`PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md) deste repositório.

### 2. Cole no seu chat de IA
Abra um novo chat com DeepSeek (ou Claude, ChatGPT, Gemini). Cole o documento inteiro como sua **primeira mensagem**. Escreva uma linha sobre o que você quer construir.

### 3. Siga a IA
A IA dá a você `run.py` (uma pequena ferramenta Python). Salve-a. Daí em diante:

> **Você cola → roda `python run.py` → envia a saída de volta.**

Esse é todo o fluxo de trabalho. Para sempre.

---

## O que você ganha

| Antes | Depois |
|-------|--------|
| O chat perde o contexto | O contexto sobrevive a cada mensagem |
| 5000 tokens por resposta | ~300 tokens por resposta |
| A IA adivinha | A IA sabe |
| 10 comandos por mudança | 1 comando por mudança |
| Conta bloqueada | Conta segura |
| "Onde estávamos?" | "Aqui está o próximo patch." |

**40–80% menos tokens. Zero perda de contexto. Zero edições manuais.**

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
- `run.py` — a ferramenta (a IA te dá no primeiro uso)
- `README.md` + traduções — esta página, multilíngue
- `LICENSE` — MIT, faça o que quiser

---

## FAQ

**Preciso saber programar?**
Não muito. Se você consegue colar uma mensagem e rodar um comando, dá para usar.

**Qual IA funciona melhor?**
DeepSeek — segue o protocolo com mais precisão. Claude, ChatGPT e Gemini também funcionam.

**É grátis?**
O documento e a ferramenta são MIT. A API da IA é o que seu provedor cobrar.

**E se algo quebrar?**
Tudo é versionado com git. Volte com um comando. O documento explica como.

---

## Pronto?

1. **[Baixe `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Cole no seu chat de IA
3. Diga: *"Quero construir X. Comece."*

**Só isso. Pare de brigar com sua IA. Comece a construir.**

---

*Feito para quem quer entregar, não cuidar de uma janela de chat.*