import csv
import time
import ollama

PROMPT = "Explain in 3 sentences what a large language model is."
MODELS = ["gemma4:e2b", "llama3.2:1b"]

rows = []
for model in MODELS:
    print(f"\nRunning: {model} ...")
    start = time.time()
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
    )
    elapsed = round(time.time() - start, 2)
    output = response["message"]["content"]
    print(f"Done in {elapsed}s")
    rows.append({
        "model": model,
        "prompt": PROMPT,
        "output": output,
        "seconds": elapsed,
    })

with open("outputs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["model", "prompt", "output", "seconds"])
    writer.writeheader()
    writer.writerows(rows)

print("\nDone — wrote outputs.csv")