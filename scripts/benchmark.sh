#!/bin/bash

# Find all Python files in the current directory
files=$(find . -name "*.py")

# Sort the files
files=$(echo "$files" | sort)

# Run hyperfine on all Python files
hyperfine_commands=()
for file in $files; do
    hyperfine_commands+=("python $file")
done
hyperfine -w 10 -r 20 "${hyperfine_commands[@]}" --export-markdown ./docs/benchmark.md
