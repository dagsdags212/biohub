#!/usr/bin/env bash

set -eu

# Specify the filenames of the forward and reverse reads
R1=$1
R2=$2
PREFIX=$3

# Path to reference assembly
REF=data/assembly/scaffolds.fasta

# Generate genome index
bwa index ${REF}

# Map "anc" reads to reference
bwa mem ${REF} ${R1} ${R2} >output/bwa/${PREFIX}.aln.sam

# Fix mates and compress
mkdir -p output/samtools
samtools sort -n -O sam output/bwa/${PREFIX}.aln.sam |
  samtools fixmate -m -O bam - output/samtools/${PREFIX}.fixmate.bam

# Sort by genome coordinate
samtools sort -O bam -o output/samtools/${PREFIX}.sorted.bam output/samtools/${PREFIX}.fixmate.bam

# Remove duplicates
samtools markdup -r -S output/samtools/${PREFIX}.sorted.bam output/samtools/${PREFIX}.sorted.dedup.bam

# Generate mapping statistics
mkdir -p output/qualimap
qualimap bamqc -outdir output/qualimap -outformat PDF -bam output/samtools/${PREFIX}.sorted.dedup.bam
