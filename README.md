# 🚀 Auto-PPT Agent

An AI-powered agent that generates PowerPoint presentations from a single prompt.

---

## 📌 Features

* Generates slides automatically using LLM
* Adds titles, bullet points, and images
* Uses MCP architecture (agent + tools)
* Simple UI with Streamlit
* Exports `.pptx` file

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
GROK_API_KEY=your_api_key_here
```

---

## ▶️ Run

Start server:

```bash
uvicorn mcp_server.server:app --reload
```

Run app:

```bash
streamlit run app.py
```

---

## 🧠 Usage

Enter a topic → Click Generate → Download PPT

---

## 📦 Output

* Presentation saved in `outputs/`
* Includes slides with content + images

---

## 👨‍💻 Note

Built using Python, Streamlit, and AI APIs for automated presentation generation.
