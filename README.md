\# Ollama Model Comparison — DV066G Assignment 1 (M1)



\*\*Group members:\*\* \[Name Surname], \[Name Surname], \[Name Surname]



\## Overview



A short Python script that sends the same prompt to two local large language

models via \[Ollama](https://ollama.com) and saves the outputs to a CSV file.

No API keys or cloud services are used — everything runs locally.



\## Models used



| Model | Size | Notes |

|---|---|---|

| `gemma4:e2b` | 4.6 GB | Larger model; slower but more detailed |

| `llama3.2:1b` | 1.3 GB | Small model; much faster, less polished |



Both were pulled with:



```bash

ollama pull gemma4:e2b

ollama pull llama3.2:1b

