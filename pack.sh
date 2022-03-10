#!/usr/bin/env bash

shell_dir=$(dirname "$0")

cd "$shell_dir"

rm -f ai-lab-2_zz2960.zip

zip -r ai-lab-2_zz2960.zip solving solver requirements.txt README.md
