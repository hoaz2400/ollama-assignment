# Ollama Model Comparison — DV066G Assignment 1 (M1)

**Group members:** Homayon Azizi, Gargaar Ahmed Abdulle, Basel Tatari

## Overview

This project uses a short Python script to send the same prompt to two local large language models through [Ollama](https://ollama.com). It measures their response times and saves their outputs to a CSV file.

No API keys or cloud services are required. The models run locally on the computer.

## Models used

| Model | Size | Description |
|---|---:|---|
| `gemma4:e2b` | 4.6 GB | Larger model; produced a more detailed response. |
| `llama3.2:1b` | 1.3 GB | Smaller model; generated a response faster. |

Both models were downloaded using:

```bash
ollama pull gemma4:e2b
ollama pull llama3.2:1b
```

## How to run

### Prerequisites

1. Install [Ollama](https://ollama.com/download).
2. Make sure Ollama is running.
3. Download both models using the commands above.
4. Install Python 3.10 or later.

### Setup (Windows PowerShell)

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the Ollama Python library:

```powershell
python -m pip install ollama
```

### Run the program

Run:

```powershell
python compare_models.py
```

The script sends the same prompt to both models, measures their response times and saves the results in `outputs.csv`.

## Observations

**Prompt used:**

"Explain in 3 sentences what a large language model is."

### Response time

| Model | Response time |
|---|---:|
| `gemma4:e2b` | 27.78 seconds |
| `llama3.2:1b` | 8.15 seconds |

In this experiment, Llama 3.2 (1B) was approximately 3.4 times faster than Gemma 4 (E2B). These measurements apply to the computer used for this experiment and may differ on other hardware.

### Was it correct?

Both models produced relevant explanations of large language models. However, the responses differed in detail and presentation. The smaller model was faster, while the larger model provided a more detailed response.

### Was it slow?

The response times were relatively long compared with some commercial cloud-based AI services. However, both models ran locally without requiring an external AI service.

### Is it worse than commercial models?

This experiment did not directly compare the local models with commercial models, so we cannot draw a definite conclusion. Commercial models may offer stronger performance in some tasks, but local models have advantages such as greater control over data and no per-request cloud API fees.

Local execution can improve privacy because prompts do not need to be sent to an external AI service. However, privacy also depends on how the application and its logs handle data.

## Files

| File | Purpose |
|---|---|
| `compare_models.py` | Python script that runs both models. |
| `outputs.csv` | Contains the prompt, model responses and response times. |
| `README.md` | Project description and instructions. |
| `.gitignore` | Excludes virtual environments and Python cache files. |
