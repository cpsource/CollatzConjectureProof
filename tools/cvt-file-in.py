import os
import re
import sys

def convert_to_github_latex_format(input_md, output_md):
    with open(input_md, 'r', encoding='utf-8') as f:
        content = f.read()

    # Convert inline math from \( ... \) to $...$ without extra spaces
    content = re.sub(r'\\\(\s*(.+?)\s*\\\)', r'$\1$', content)

    # Convert block math from \[ ... \] to $$...$$ without extra spaces
    content = re.sub(r'\\\[\s*(.+?)\s*\\\]', r'$$\1$$', content)

    # Write the converted content to the output file
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Converted LaTeX to GitHub format in {output_md}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_md> <output_md>")
        sys.exit(1)

    input_md = sys.argv[1]
    output_md = sys.argv[2]

    convert_to_github_latex_format(input_md, output_md)

if __name__ == "__main__":
    main()

