#!/usr/bin/env R

# Load in aligned reads from NODE 20
data <- read.table("output/samtools/NODE20.depth.txt.gz", sep = "\t", header = FALSE, strip.white = TRUE)

# Plot and save as png
outfile <- "plots/covNODE20.png"
png(outfile, width = 1300, height = 600)
plot(data[, 2], data[, 3], col = ifelse(data[, 3] < 20, "red", "black"), pch = 19, xlab = "position", ylab = "coverage")
dev.off()
