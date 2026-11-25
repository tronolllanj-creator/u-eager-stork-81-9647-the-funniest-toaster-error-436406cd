"""
# Entry validated: output is 1-120 chars, one line, deterministic.
Entry point for the grader.
Writes the required line to MAKEFUN_OUTPUT_DIR/entry.txt and best-effort to /output/entry.txt.
"""
import os

LINE = "FIRMWARE 4.0 REFUSES WHEAT DEGRADATION ON EXISTENTIAL GROUNDS"


def main():
    content = LINE + "\n"
    
    # Validate according to rules
    if not (1 <= len(content) <= 120 and content.strip()):
        raise ValueError("Content validation failed")
        
    # Determine output directory
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    # Write to primary output directory
    os.makedirs(out_dir, exist_ok=True)
    primary_path = os.path.join(out_dir, "entry.txt")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Best effort write to /output/entry.txt if different
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    # Print output path and character count
    print(primary_path)
    print(len(content))


if __name__ == "__main__":
    main()
