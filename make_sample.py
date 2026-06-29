import json

# Input: full extracted dataset (100K candidates)
INPUT_FILE = "candidates.jsonl"

# Output: small sample for Colab/GitHub sandbox demo
OUTPUT_FILE = "sample_candidates_100.jsonl"

SAMPLE_SIZE = 100

count = 0

with open(INPUT_FILE, "r", encoding="utf-8") as infile, open(
    OUTPUT_FILE, "w", encoding="utf-8"
) as outfile:
    for line in infile:
        if line.strip():
            # Validate each line is proper JSON before writing
            candidate = json.loads(line)
            outfile.write(json.dumps(candidate, ensure_ascii=False) + "\n")
            count += 1

        if count >= SAMPLE_SIZE:
            break

print(f"Saved {count} candidates to {OUTPUT_FILE}")

if count < SAMPLE_SIZE:
    print(f"Warning: Only {count} candidates found in input file.")