# ⚖️ Legal Risk Auditor Pro
An AI-powered legal assistant designed for SMEs to audit vendor agreements and contracts instantly.

## 🚀 Features
- **Deep AI Audit**: Uses Llama 3.1 via Groq for high-speed legal analysis.
- **Visual Risk Gauge**: Real-time risk scoring (0-10) using Plotly.
- **Multi-Format Export**: Download professional PDF reports for business use or JSON logs for technical records.
- **Bilingual Support**: Fully functional in English and Hindi.

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **AI Engine**: Groq (Llama-3.1-8b-instant)
- **PDF Engine**: FPDF
- **Visuals**: Plotly

## 📦 Installation
1. Clone the repo: `git clone <your-repo-link>`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your `GROQ_API_KEY` to a `.env` file.
4. Run: `python -m streamlit run app.py`