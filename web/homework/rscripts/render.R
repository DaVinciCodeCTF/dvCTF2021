#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
rmarkdown::render(args[1])
