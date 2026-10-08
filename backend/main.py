from fastapi import FastAPI

app = FastAPI(
    title="PCB Defect Inspector API",
    description="AI-powered PCB defect inspection system",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "PCB Defect Inspector API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}