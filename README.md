# 🚀 StartupX – AI-Powered Startup Idea Evaluator

**StartupX** is an intelligent co-pilot for aspiring founders. It helps users rapidly **validate startup ideas**, **assess market fit**, **identify competitors**, and even **generate an investor-style pitch deck** — all powered by cutting-edge AI.

---

## 📌 Table of Contents

- [🎥 Demo](#-demo)
- [💡 Motivation](#-motivation)
- [✨ Features](#-features)
- [🧰 Tech Stack](#-tech-stack)
- [🧠 How It Works](#-how-it-works)
- [🛠️ Getting Started](#-getting-started)
- [📁 Folder Structure](#-folder-structure)

---

## 🎥 Demo

https://github.com/user-attachments/assets/dd443743-8cca-475f-bc1c-63c1efc466a0


---

## 💡 Motivation

In a time when launching a product is easier than ever but validating an idea remains a mystery, **StartupX** was built to answer one question:

> “Is this idea even worth pursuing?”

As a first-generation tech student with a passion for both **AI** and **entrepreneurship**, I wanted to explore what it really takes to bring an AI product to life — not just from a model’s perspective, but from a **full-stack engineer’s mindset**. This project was my attempt to:

- Understand how **LLMs**, **prompt engineering**, and **data pipelines** can come together to create meaningful user experiences.
- Learn and apply full-stack tools like **Next.js**, **Tailwind CSS**, **FastAPI**, and **OpenAI GPT-4** outside the classroom.
- Build a real-world MVP that could support founders without access to elite networks or accelerators.

---

## ✨ Features

With **StartupX**, users can:

- ✅ **Validate startup ideas** in real-time using GPT-4
- 🧠 Generate **SWOT analysis**
- 📢 Create an **Elevator pitch**
- 🎯 Map **Target personas**
- 📊 Calculate **Market Scope** (TAM, SAM, SOM)
- 🕵️‍♀️ Discover **Competitors** using semantic search
- 🎞️ Generate a **Pitch deck** with GPT-powered slides
- 🧵 Leverage **prompt chaining** and structured response pipelines

---

## 🧰 Tech Stack

### 🖥️ Frontend
- **Next.js (v15)** – App Router, Server Actions
- **Tailwind CSS** – Utility-first styling
- **Framer Motion** – UI animations
- **Axios** – For API communication

### ⚙️ Backend
- **FastAPI** – Python-based backend framework
- **OpenAI GPT-4** – For all core AI generation
- **Prompt Engineering** – Modular structured prompts
- **LangChain** (optional) – Agent-like reasoning

### 📦 Dev & Deployment
- **Python 3.11+**
- **Node.js 20+**
- **Vercel** for frontend
- **Render / Railway** for backend

---

## 🧠 How It Works

1. User submits a startup idea via the frontend
2. Backend routes request to agents:
   - Extracts keywords
   - Generates SWOT, Personas, Pitch, Market Scope, etc.
3. Runs **competitor matching** using semantic search
4. Estimates **TAM/SAM/SOM** with keyword approximations
5. Optionally creates a **Pitch Deck**
6. Outputs clean, readable insights via the UI

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.11+
- Node.js 20+
- OpenAI API key

### Clone the Repository

```bash
git clone https://github.com/ApoorvThite/startupx.git
cd startupx

cd startupx-backend
pip install -r requirements.txt
cp .env.example .env  # Add your OpenAI API key
uvicorn main:app --reload

cd startupx-ui
npm install
npm run dev
```

📁 Folder Structure
```
startupx/
├── startupx-backend/
│   ├── main.py
│   ├── agents/
│   ├── utils/
│   └── requirements.txt
├── startupx-ui/
│   ├── app/
│   │   └── page.tsx
│   ├── public/
│   └── tailwind.config.js
```
