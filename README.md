# AI Chatbot using LangChain and Groq API

A lightweight, high-performance, console-based AI chatbot built with **Python**, **LangChain**, and the **Groq API** utilizing the advanced **Llama-3.3-70b-versatile** model for near-instantaneous intelligent responses.

---

## 🚀 Features

- **Blazing Fast Responses:** Leverages Groq's LPU™ (Language Processing Unit) architecture for ultra-low latency text generation.
- **State-of-the-Art LLM:** Powered by the advanced `llama-3.3-70b-versatile` model via LangChain.
- **Secure Configuration:** Environment variable isolation using `python-dotenv` to ensure sensitive credentials (API keys) are kept safe.
- **Robust Loop:** Interactive, continuous terminal-based session with a clear termination command (`exit`).

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Framework:** [LangChain](https://github.com/langchain-ai/langchain) (modular LLM wrapper)
- **Inference Engine:** [Groq Cloud API](https://console.groq.com/)
- **Model:** `llama-3.3-70b-versatile`
- **Environment Management:** `python-dotenv`

---

## 📦 Installation & Setup

Follow these steps to run the chatbot locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-chatbot-groq.git
cd ai-chatbot-groq
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
1. Create a file named `.env` in the root directory.
2. Add your Groq API key (get one from the [Groq Console](https://console.groq.com/)):
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

> [!WARNING]
> Never commit your `.env` file containing the `GROQ_API_KEY` to public repositories. The `.gitignore` in this project is pre-configured to prevent this.

---

## 🏃 Run the Application

Start the interactive session:
```bash
python app.py
```

### Example Usage:
```text
AI Chatbot Started! Type 'exit' to stop.

You: Explain quantum computing in one sentence.
AI: Quantum computing uses qubits to process information in ways classical computers can't, allowing them to solve certain complex problems much faster.

You: exit
Goodbye!
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
