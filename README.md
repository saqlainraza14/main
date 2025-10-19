# 🧠 AI Policy Helper

AI Policy Helper is an **AI-powered policy document assistant** that allows you to upload, embed, and intelligently search through policy or text documents using natural language queries.  
It is built using **FastAPI**, **Next.js**, and **Qdrant**, with support for LLMs like **OpenAI** or **Ollama** for retrieval-augmented generation (RAG).

---

## 🌟 Features

✅ Upload and ingest policy documents  
✅ Automatic chunking and vector embedding storage in Qdrant  
✅ Natural language querying over stored documents  
✅ Switchable LLM providers (`stub`, `OpenAI`, or `Ollama`)  
✅ Dockerized for instant local setup  
✅ Includes automated tests (pytest) and CI/CD (GitHub Actions)

---

## 🧩 Project Structure

```
ai-policy-helper-starter-pack/
├── backend/              # FastAPI backend (document ingestion + LLM logic)
│   ├── app/
│   │   ├── main.py       # API entry point
│   │   ├── rag.py        # RAG engine implementation
│   │   ├── routes/       # API endpoints
│   │   └── tests/        # pytest-based automated tests
│   └── Dockerfile
│
├── frontend/             # Next.js frontend (UI)
│   ├── pages/
│   ├── components/
│   └── Dockerfile
│
├── docker-compose.yml    # One-command multi-container setup
├── .env.example          # Environment variable template
└── README.md             # Documentation
```

---

## ⚙️ Environment Variables

Make sure to create a `.env` file (or update `.env.example`) with the following:

| Variable | Description | Default |
|-----------|-------------|----------|
| `EMBEDDING_MODEL` | Embedding model name | `local-384` |
| `LLM_PROVIDER` | `stub` \| `openai` \| `ollama` | `stub` |
| `OPENAI_API_KEY` | Your OpenAI API key (required if using OpenAI) | — |
| `OLLAMA_HOST` | Ollama host endpoint | `http://ollama:11434` |
| `VECTOR_STORE` | Vector storage backend | `qdrant` |
| `COLLECTION_NAME` | Collection name in Qdrant | `policy_helper` |
| `CHUNK_SIZE` | Chunk size for text splitting | `700` |
| `CHUNK_OVERLAP` | Overlap between text chunks | `80` |
| `NEXT_PUBLIC_API_BASE` | Backend API base URL | `http://localhost:8000` |

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/saqlainraza14/main.git
cd main
```

### 2️⃣ Create an `.env` file

```bash
cp .env.example .env
```

Add your OpenAI API key if using OpenAI:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 3️⃣ Run with Docker Compose

```bash
docker compose up --build
```

Wait until you see:
```
Backend:  http://localhost:8000
Frontend: http://localhost:3000
```

---

## 🧠 Usage

### Upload Documents
You can upload PDFs, text files, or documents through the frontend UI or via the backend `/api/ingest` endpoint.

### Query the Assistant
Use the frontend interface or call the `/api/query` endpoint to ask natural language questions.  
The app uses semantic vector search + LLM to generate contextual answers.

---

## 🧪 Automated Tests

Run backend tests using **pytest** inside Docker:

```bash
docker compose run --rm backend pytest -q
```

Test files are located in:  
```
backend/app/tests/
```

---

## 🔄 CI/CD Automation

This project includes a **GitHub Actions workflow** (`.github/workflows/ci.yml`) that automatically:

- Builds and tests Docker containers  
- Runs automated acceptance tests  
- Optionally pushes Docker images to a registry  

You can view the workflow under the **Actions** tab in your GitHub repository.

---

## 🧰 Technology Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Next.js (React, TypeScript) |
| **Backend** | FastAPI (Python) |
| **Database / Vector Store** | Qdrant |
| **AI Integration** | OpenAI / Ollama / Stub LLM |
| **Testing** | Pytest |
| **Containerization** | Docker & Docker Compose |
| **CI/CD** | GitHub Actions |

---

## 🧱 Docker Setup Summary

| Service | Port | Description |
|----------|------|-------------|
| Frontend | `3000` | Next.js app |
| Backend | `8000` | FastAPI app |
| Qdrant | `6333` | Vector database |

To bring the entire stack up:
```bash
docker compose up --build
```

To stop:
```bash
docker compose down
```

---

## 📚 Example API Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| `POST` | `/api/ingest` | Upload and embed new documents |
| `POST` | `/api/query` | Query vector store using LLM |
| `GET` | `/healthz` | Check backend health |

---

## 🧩 Troubleshooting

**Common issues:**
- ❌ `qdrant` unhealthy → restart Docker containers  
- ❌ `OPENAI_API_KEY` error → make sure `.env` has valid key  
- ❌ Tests failing → ensure backend service is running before pytest  

---

## 🧑‍💻 Author

**Saqlain Raza**  
🚀 GitHub: [saqlainraza14](https://github.com/saqlainraza14)

