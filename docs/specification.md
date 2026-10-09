# PCB Defect Inspector — Project Specification v1.0

## 1. Problem Statement
PCB Defect Inspector is an AI-assisted prototype that detects visible PCB surface defects and generates evidence-grounded troubleshooting reports.

## 2. Project Goals
- Detect and localize six PCB defect categories.
- Retrieve relevant technical knowledge.
- Generate grounded inspection explanations with citations.
- Provide an API and interactive web demo.
- Evaluate CV, retrieval, report generation, and end-to-end behavior.

## 3. Scope
In scope: static PCB images, object detection, technical retrieval, LLM explanations, and report visualization.
Out of scope: electrical measurements, industrial certification, real-time production inspection, and automatic repairs.

## 4. Target Defect Classes
- open circuit
- short
- mouse bite
- spur
- missing hole
- spurious copper

Final class IDs and names must match the audited dataset.

## 5. Input and Output
Input: one supported PCB image in JPG, JPEG, or PNG format.
Output: detected defect classes, bounding boxes, confidence scores, technical explanations, references, and limitations.

No detection does not imply a defect-free PCB.

## 6. Proposed Technology Stack
- CV: pretrained YOLO11n, fine-tuned on PCB data
- Dataset candidate: DeepPCB
- Retrieval: sentence-transformers and ChromaDB
- LLM: configurable API provider
- Backend: FastAPI and Pydantic
- Frontend: Streamlit
- Deployment: Docker

## 7. Processing Pipeline
Image upload -> validation -> CV inference -> defect-based retrieval -> grounded LLM report -> API response -> UI.

## 8. Evaluation
- CV: precision, recall, mAP50, mAP50-95, per-class results
- Retrieval: Recall@5, MRR
- LLM: grounding, citation correctness, abstention
- System: end-to-end task success and latency

Targets are provisional and will be refined after baseline evaluation.

## 9. Known Limitations
- Performance on phone images is not established.
- Visual predictions cannot confirm electrical faults.
- False negatives and false positives are possible.
- LLM explanations require relevant supporting evidence.

## 10. Acceptance Criteria
- Reproducible dataset preparation and CV baseline
- Working retrieval and report generation
- Working FastAPI and Streamlit demo
- Documented evaluation results and limitations
- Reproducible setup and deployment instructions
