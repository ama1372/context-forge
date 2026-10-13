# 🚀 context-forge

**Tú vs. el chat de IA que lo olvida todo.**

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README.fa.md">فارسی</a> ·
  <a href="README.zh.md">中文</a> ·
  <b>Español</b> ·
  <a href="README.ar.md">العربية</a> ·
  <a href="README.hi.md">हिन्दी</a> ·
  <a href="README.fr.md">Français</a> ·
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

## ¿Te suena familiar?

- 😤 **Llevas 3 horas programando con la IA. El chat llega a su límite. Todo se pierde.**
- 🤯 **La IA olvida lo que decidiste hace dos mensajes.**
- 💸 **Cada mensaje nuevo pegas el proyecto entero — quemando tokens, perdiendo tiempo.**
- 🤖 **La IA edita el código a mano, rompe cosas, y no sabes por qué.**
- 😴 **Pasas más tiempo explicando que construyendo.**
- 🚫 **Recibes "demasiados mensajes, inténtalo más tarde".**

**¿Sí?** Entonces esto es para ti.

---

## ¿Qué es?

Un **documento único** (`PROJECT_CONTEXT.md`) que pegas en cualquier chat de IA — DeepSeek, Claude, ChatGPT, Gemini. Convierte una IA charlatana en un **socio disciplinado de proyecto** que:

- ✅ **Nunca pierde el contexto** — cada respuesta lleva el estado del proyecto hacia adelante.
- ✅ **Nunca edita tu código a mano** — envía un parche, tú pegas, un comando aplica.
- ✅ **Nunca quema tokens** — pide solo el archivo que necesita, no todo el proyecto.
- ✅ **Nunca bloquea tu cuenta** — protocolo anti-límite incluido.
- ✅ **Nunca te pide 10 comandos** — pegas, corres uno, listo.
- ✅ **Nunca olvida dónde estabas** — el siguiente chat continúa exactamente donde lo dejaste.

**Un documento. Una herramienta. Un comando. Eso es todo.**

---

## Inicio rápido — 6 pasos

1. **Guarda `PROJECT_CONTEXT.en.md` en la raíz de tu proyecto.**
2. **(Recomendado)** Guarda `run.py` en la misma carpeta. ¿No tienes `run.py`? Dile a la IA: *"Crea run.py desde la Sección 35."*
3. **Configura una vez:** `python run.py --init`
4. **Abre un chat con DeepSeek** (o Claude / ChatGPT / Gemini). Pega el **documento completo** como primer mensaje. Di: *"Proyecto nuevo. Mi objetivo: <una línea>."*
5. **Bucle:** la IA envía un bloque → cópialo en `_work/input.txt` → ejecuta `python run.py` → devuelve `_work/output.txt`. Repite.
6. **Mantén el bucle hasta terminar el proyecto.** No dejes que la IA te saque — sin comandos shell en el chat, sin scripts rápidos. La respuesta siempre es: *"Ponlo en input.txt."*

> **Consejo:** si la IA se desvía - sugiere comandos shell en el chat, omite el contexto - di: **"Contexto del proyecto, por favor."**

---

## Qué obtienes

| Antes | Después |
|-------|---------|
| El chat pierde contexto | El contexto sobrevive cada mensaje |
| 5000 tokens por respuesta | ~300 tokens por respuesta |
| La IA adivina | La IA sabe |
| 10 comandos por cambio | 1 comando por cambio |
| Cuenta bloqueada | Cuenta segura |
| "¿Dónde estábamos?" | "Aquí va el siguiente parche." |

**40–80% menos tokens. Cero pérdida de contexto. Cero ediciones manuales.**

---

## Funciona con cualquier lenguaje

Rust, Python, Node, Go, C++, lo que sea. Le dices a `run.py` una vez cómo construir y probar tu proyecto — el protocolo es el mismo para todos los lenguajes.

---

## Idioma del documento

El documento de reglas es **solo en inglés** — así cada IA lo analiza idénticamente y hay una única fuente de verdad.

**Pero la conversación con tu IA es en tu idioma.** Solo escribe tu primer mensaje en español, persa, árabe, chino — la IA responde en el mismo idioma. El documento es universal.

---

## Archivos que obtienes

- `PROJECT_CONTEXT.en.md` — el documento de reglas (pega esto en tu IA)
- `run.py` — la herramienta (la IA te la da en el primer uso)
- `README.md` + traducciones — esta página, multi-idioma
- `LICENSE` — MIT, haz lo que quieras

---

## Preguntas frecuentes

**¿Necesito saber programar?**
No mucho. Si puedes pegar un mensaje y correr un comando, puedes usarlo.

**¿Qué IA funciona mejor?**
DeepSeek — sigue el protocolo con mayor precisión. Claude, ChatGPT y Gemini también funcionan.

**¿Es gratis?**
El documento y la herramienta son MIT. La API de IA es lo que cobre tu proveedor.

**¿Y si algo se rompe?**
Todo está versionado con git. Retrocede con un comando. El documento explica cómo.

---

## ¿Listo?

1. **[Descarga `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Pégalo en tu chat de IA
3. Di: *"Quiero construir X. Empieza."*

**Eso es todo. Deja de pelear con tu IA. Empieza a construir.**

---

*Hecho para gente que quiere lanzar, no cuidar una ventana de chat.*