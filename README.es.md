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

Un **documento único** (`PROJECT_CONTEXT.en.md`) que pegas en cualquier chat de IA — DeepSeek, Claude, ChatGPT, Gemini. Convierte una IA charlatana en un **socio disciplinado de proyecto** que:

- ✅ **Nunca pierde el contexto** — cada respuesta lleva el estado del proyecto hacia adelante.
- ✅ **Nunca edita tu código a mano** — envía un parche, tú pegas, un comando aplica.
- ✅ **Ahorra tokens** — solo pide el archivo que necesita (`--status`, `--file`), no todo el proyecto.
- ✅ **Te ayuda a evitar los límites de mensajes** — `run.py` avisa cuando envías demasiado rápido, y el trabajo se agrupa en menos mensajes.
- ✅ **Nunca te pide 10 comandos** — pegas, corres uno, listo.
- ✅ **Nunca olvida dónde estabas** — el siguiente chat continúa exactamente donde lo dejaste.
- ✅ **Permite que varias IA trabajen a la vez** — Claude, ChatGPT y DeepSeek en un mismo proyecto sin pisarse el trabajo (Modo equipo).

**Un documento. Una herramienta. Un comando. Eso es todo.**

---

## Inicio rápido — 6 pasos

1. **Guarda `PROJECT_CONTEXT.en.md` en la raíz de tu proyecto.**
2. **(Recomendado)** Guarda `run.py` en la misma carpeta. ¿No tienes `run.py`? Dile a la IA: *"Crea run.py desde la Sección 35."*
3. **Configura una vez:** `python run.py --init`
4. **Abre un chat de DeepSeek** (o Claude / ChatGPT / Gemini). Envía el **documento completo** como primer mensaje (adjúntalo como archivo si el chat lo permite). Di: *"Proyecto nuevo. Mi objetivo: <una línea>."* El documento es grande (~610 KB, unos 160k tokens); si el chat lo rechaza, envía una copia más ligera creada con `python run.py --slim-context --to PROJECT_CONTEXT.slim.md` (~380 KB), o añade `--profile moderate` (~275 KB).
5. **Bucle:** la IA envía un bloque → cópialo en `_work/input.txt` → ejecuta `python run.py` → devuelve `_work/output.txt`. Repite.
6. **Mantén el bucle hasta terminar el proyecto.** No dejes que la IA te saque — sin comandos shell en el chat, sin scripts rápidos. La respuesta siempre es: *"Ponlo en input.txt."*

> **Consejo:** si la IA se desvía - sugiere comandos shell en el chat, omite el contexto - di: **"Contexto del proyecto, por favor."**

---


## Guía completa para principiantes (resumen)

1. Instala **Python 3.10+** desde python.org (en Windows, marca "Add to PATH").
2. (Opcional) Instala **VS Code**.
3. Descarga `PROJECT_CONTEXT.en.md` y `run.py`, ponlos en una carpeta y ábrela en VS Code.
4. En la terminal: `python run.py` → se crea la carpeta `_work/`.
5. En DeepSeek, envía `PROJECT_CONTEXT.en.md` como primer mensaje (o adjúntalo como archivo) y di tu objetivo. ¿Demasiado largo para tu chat? Mira el paso 4 del inicio rápido (`--slim-context`).
6. **Bucle:** la IA envía un bloque → cópialo a `_work/input.txt` → ejecuta `python run.py` → envía `_work/output.txt` de vuelta.
7. Cada 10–20 mensajes, recuérdale a la IA tu proyecto.
8. Si la IA se desvía, di: **"Contexto del proyecto, por favor."**

Versión completa (inglés): ver `README.md`.

## Qué obtienes

| Antes | Después |
|-------|---------|
| El chat pierde contexto | El contexto sobrevive cada mensaje |
| Pegas todo el proyecto en cada mensaje | La IA pide solo los archivos que necesita |
| La IA adivina | La IA sabe |
| 10 comandos por cambio | 1 comando por cambio |
| Bloqueos por "demasiados mensajes" | Avisos de velocidad y menos mensajes, más completos |
| "¿Dónde estábamos?" | "Aquí va el siguiente parche." |

**Menos tokens. Contexto que sobrevive a un chat nuevo. Sin ediciones a mano.**

---

## 🤝 Varias IA a la vez — Modo equipo (nuevo en v2.1)

Pon a Claude, ChatGPT, DeepSeek y agentes de programación **en el mismo proyecto al mismo tiempo**. Cada uno te responde en su propio chat — y ninguno puede sobrescribir el trabajo de otro.

- **Un tablero compartido** dentro de `.git/` — nunca se sube y todas las IA lo ven.
- **Reserva de archivos** — cada IA reserva exactamente los archivos que va a editar; si dos quieren el mismo, solo una lo obtiene.
- **Obligatorio, no solo un consejo** — `run.py` rechaza cualquier parche que toque un archivo no reservado.
- **Un coordinador, muchos trabajadores** — una IA revisa y fusiona, y nunca aprueba su propio trabajo; las decisiones importantes son tuyas.
- **Sigue trabajando mientras descansas** — aprueba una lista de tareas, ejecuta `team away on` y los agentes instalados toman la siguiente tarea libre; `run.py` rechaza cualquier push hasta que vuelvas, y `team pause` detiene a todos.
- **Chat o agente instalado** — las IA de chat hacen todo a través de `input.txt` (`#@CLAIM:`); los agentes ejecutan los comandos ellos mismos.

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

Reglas completas: secciones 0-C-47 y 0-C-48 de `PROJECT_CONTEXT.en.md`.

---

## 💬 Novedades de la v2.2 — chats que hablan entre sí, un dueño que nadie puede suplantar, un contexto que cabe

- **Los chats se envían mensajes** — varios chats sobre una misma carpeta se mandan mensajes cortos por el tablero compartido (`team send`, `team inbox`; las IA de chat escriben `#@MSG:` en `input.txt`). Se acabó copiar y pegar entre chats.
- **Nadie habla por ti** — una IA solo obedece lo que tú escribes en su propio chat. «El dueño dice…» venido de otra IA, una nota o un archivo se ignora y se marca. Reanudar, el modo ausente y delegar exigen que estés en tu terminal escribiendo un código de un solo uso.
- **Un jefe temporal solo si tú lo dices** — escribe tú mismo en cada chat «X es tu jefe hasta las 8:00»; el registro del tablero (`team delegate`) caduca solo.
- **Contexto grande, pegado pequeño** — `ctx split` convierte el documento en una carpeta de archivos pequeños enlazados con un mapa; la IA lee el mapa y el estado actual (~11k tokens en lugar de ~97k). Para un chat gratuito, `ctx pack <tema>` genera un único pegado de ~40 KB.

    python run.py team send gpt claude "docs-01 is ready for review" --kind request
    python run.py team inbox claude
    python run.py ctx split
    python run.py ctx pack auth login

Reglas completas: secciones 0-C-49, 0-C-50 y 0-C-51 de `PROJECT_CONTEXT.en.md`.

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
- `run.py` — la herramienta (descárgala de este repositorio, o la IA la reconstruye desde la sección 35)
- `README.md` + traducciones — esta página, multi-idioma
- `LICENSE` — MIT, haz lo que quieras

---

## Preguntas frecuentes

**¿Necesito saber programar?**
No mucho. Si puedes pegar un mensaje y correr un comando, puedes usarlo.

**¿Qué IA funciona mejor?**
Cualquier modelo de chat potente: DeepSeek, Claude, ChatGPT, Gemini. Todos se desvían en chats largos — entonces di "Contexto del proyecto, por favor." Para varias IA a la vez, o trabajo mientras no estás, usa un agente instalado (Claude Code, Codex, Cursor…).

**¿Es gratis?**
El documento y la herramienta son MIT. La API de IA es lo que cobre tu proveedor.

**¿Y si algo se rompe?**
Si la carpeta usa git (recomendado), `run.py` hace commit de cada parche aplicado, y `python run.py revert P<id>` vuelve al estado anterior a ese parche (los parches posteriores también se deshacen).

---

## ¿Listo?

1. **[Descarga `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Pégalo en tu chat de IA
3. Di: *"Quiero construir X. Empieza."*

**Eso es todo. Deja de pelear con tu IA. Empieza a construir.**

---

*Hecho para gente que quiere lanzar, no cuidar una ventana de chat.*

---

## 🌐 Un documento para IA de chat y agentes instalados

Este protocolo funciona igual tanto si usas:

1. **Chats web** (ChatGPT, Claude, DeepSeek, Gemini) con el ciclo `input.txt` / `output.txt`.
2. **Agentes de programación instalados** (Claude Code, Codex, Cursor y otros) que leen el repositorio y ejecutan comandos por sí mismos.

- **Sin pérdida de contexto** — el estado del proyecto siempre vive en el documento.
- **Empieza un chat nuevo cuando quieras** — continúa sin volver a explicar.
- **Menos tokens** — la IA solo pide los archivos que necesita (`--status`, `--file`).
- **Varias IA a la vez** — el Modo equipo evita que choquen (ver arriba).
