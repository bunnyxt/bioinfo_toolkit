#!/usr/bin/env python3

# Filename: count_fq.py
# Description: count sequences in fastq file
# Usage: python3 count_fq.py filename
# Version: 0.0.1
# Date: 2021-04-27
# Author: bunnyxt
# Link: https://github.com/bunnyxt/bioinfo_toolkit

import sys

if len(sys.argv) < 2:
    print('Please provide fastq filename. Usage: python3 count_fq.py filename')
    exit(1)
filename = sys.argv[1]

count = 0
current_stage = 0
sequence_length = 0
quality_length = 0

with open(filename, 'r') as f:
    for line in f:
        if current_stage == 0:
            if line.startswith('@'):
                current_stage += 1
            else:
                raise RuntimeError('Invalid fastq format detected! First line of one sequence should starts with @!')
        elif current_stage == 1:
            sequence_length = len(line.rstrip('\n'))
            current_stage += 1
        elif current_stage == 2:
            if line.startswith('+'):
                current_stage += 1
            else:
                raise RuntimeError('Invalid fastq format detected! Third line of one sequence should starts with +!')
        elif current_stage == 3:
            quality_length = len(line.rstrip('\n'))
            if quality_length == sequence_length:
                count += 1
                current_stage = 0
            else:
                raise RuntimeError('Invalid fastq format detected! Sequence length and quality length are not equal!')

print('Done! Fastq file %s has %d sequence(s).' % (filename, count))
