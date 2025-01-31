#!/bin/bash

# Loop through all files matching chatgpt-*.md
for file in chatgpt-*.md; do
    # Ensure the file exists (to prevent issues if no match occurs)
    if [[ -f "$file" ]]; then
        echo "Processing $file..."
        
        # Define temporary output file
        tmp_file="${file}-tmp"

        # Run Python conversion script
        python3 tools/cvt-file-in.py "$file" "$tmp_file"

        # Check if the conversion was successful
        if [[ -f "$tmp_file" ]]; then
            # Rename tmp file back to original filename
            mv "$tmp_file" "$file"
            echo "Updated: $file"
        else
            echo "Error: Conversion failed for $file"
        fi
    fi
done

echo "Processing complete!"

