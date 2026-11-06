# Ollama Model Comparison — DV066G Assignment 1 (M1)

**Group members:** Homayon Azizi, Gargaar Ahmed Abdulle, Basel Tatari

## Overview

A short Python script that sends the same prompt to two local large language
models via [Ollama](https://ollama.com) and saves the outputs to a CSV file.
No API keys or cloud services are used — everything runs locally.

## Models used

| Model | Size | Notes |
|---|---|---|
| `gemma4:e2b` | 4.6 GB | Larger model; slower but more detailed |
| `llama3.2:1b` | 1.3 GB | Small model; much faster, less polished |

Both were pulled with:

```bash
ollama pull gemma4:e2b
ollama pull llama3.2:1b
```

## How to run

### Prerequisites
1. Install [Ollama](https://ollama.com/download) and make sure it is running.
2. Pull both models (see commands above).
3. Python 3.10+ installed.

### Setup (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install ollama
```

*Note: inside a virtual environment, always use `python -m pip` so packages install into the venv.*

### Run

```powershell
python compare_models.py
```

The script writes `outputs.csv` with one row per model.

## What the script does

For each model, it sends the prompt via `ollama.chat(...)`, measures response time, and writes the result to `outputs.csv`.

## Observations (using course terminology)

Prompt used: *"Explain in 3 sentences what a large language model is."*

| Model | Time | Quality & Terminology |
|---|---|---|
| `gemma4:e2b` | **27.78 s** | Accurate, well-structured, exactly 3 sentences. |
| `llama3.2:1b` | **8.15 s** | About 3.4× faster, but produced **4 sentences** instead of 3. |

### Was it slow?
- Yes, relative to commercial cloud models. `gemma4:e2b` took ~28 s; `llama3.2:1b` took ~8 s on this machine.
- Running on a machine with more VRAM (or a dedicated GPU) would make `gemma4:e2b` significantly faster.

### Was it correct? (Non-determinism and Hallucinations)
- Both models gave factually accurate definitions. Neither exhibited **hallucinations** (fabricating facts).
- However, **non-determinism** was observed: the outputs are not strictly fixed. The smaller `llama3.2:1b` model drifted from the instruction (producing 4 sentences instead of 3), showing that smaller models may struggle with precise instruction-following.

### Is it worse than commercial models?
- Yes, in instruction-following and polish. Commercial models (e.g., GPT-4, Claude) reliably obey "exactly 3 sentences" and produce tighter prose.
- However, for a 1.3 GB model running locally on a laptop, the output is remarkably good. The trade-off is: commercial models are smarter, but local models guarantee **privacy** (no data sent to the cloud) and **zero cost**.

## Files

| File | Purpose |
|---|---|
| `compare_models.py` | Main script |
| `outputs.csv` | Generated results |
| `README.md` | This file |
| `.gitignore` | Excludes `.venv/` and Python cache |
