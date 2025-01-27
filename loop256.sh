#!/bin/bash

echo "Show that all possible track-numbers terminate with 1"
for i in {0..15}; do
  echo "Outer loop count: $i" >&2
  for j in {0..15}; do
    echo "  Inner loop count: $j"
    python3 c1-collatz.py $((16*i + j)) 0 0
  done
done

