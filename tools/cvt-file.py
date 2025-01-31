import os
import re
import glob
import filecmp

def convert_to_github_latex_format(input_md, output_md):
    with open(input_md, 'r', encoding='utf-8') as f:
        content = f.read()

    # Convert inline math from \( ... \) to $...$ without extra spaces
    content = re.sub(r'\\\(\s*(.+?)\s*\\\)', r'$\1$', content)

    # Convert block math from \[ ... \] to $$...$$ without extra spaces
    content = re.sub(r'\\\[\s*(.+?)\s*\\\]', r'$$\1$$', content)

    # Add the specified lines to the top of the output
    #header = "[Home](https://t2m.io/VwvDcuw)\n---\n\n"
    #content = header + content

    # Write the converted content to the output file
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Converted LaTeX to GitHub format in {output_md}")

def main():
    convert_to_github_latex_format("collatz-deepseek-flow.md","collatz-deepseek-flow.md.tmp")

if __name__ == "__main__":
    main()
