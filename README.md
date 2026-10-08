# PCB Defect Inspector

AI-powered PCB defect detection and diagnosis using Computer Vision, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs).

## Project Overview

PCB Defect Inspector is an AI engineering project designed to detect potential defects in printed circuit board images and generate evidence-grounded explanations.

The system combines:

- **Computer Vision:** Detect and localize visible PCB defects.
- **RAG:** Retrieve relevant technical knowledge about PCB defects.
- **LLM:** Generate defect explanations and inspection reports.
- **FastAPI:** Provide backend inference endpoints.
- **Streamlit:** Provide an interactive inspection interface.

## Planned Workflow

1. Upload a PCB image.
2. Detect potential defects using a Computer Vision model.
3. Retrieve relevant technical information using RAG.
4. Generate an inspection report using an LLM.
5. Display detected regions, confidence scores, and explanations.

## Project Structure

- `backend/` — FastAPI, CV, RAG, LLM, and orchestration.
- `frontend/` — Streamlit interface.
- `data/` — Dataset and knowledge resources.
- `models/` — Model checkpoints.
- `experiments/` — Training experiments.
- `evaluation/` — Evaluation scripts.
- `tests/` — Automated tests.
- `docs/` — Technical documentation.

## Getting Started

Create and activate a Python virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run the backend:

```powershell
python -m uvicorn backend.main:app --reload
```

Run the frontend in a separate terminal:

```powershell
python -m streamlit run frontend/app.py
```

## Current Status

**Phase 1 — Project Setup**

The initial FastAPI and Streamlit applications are being established. Computer Vision inference, RAG retrieval, and LLM report generation are not yet implemented.

## Evaluation Plan

The project will evaluate:

- Detection performance: precision, recall, mAP.
- Retrieval quality: relevance and evidence coverage.
- Report quality: factual correctness and grounding.
- System performance: latency and end-to-end reliability.

## Limitations

The system identifies potential visual defects. Its predictions are not equivalent to electrical testing or confirmed manufacturing inspection results.