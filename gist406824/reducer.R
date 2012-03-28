#! /usr/bin/env Rscript

options(warn=-1)
trimWhiteSpace <- function(line) gsub("(^ +)|( +$)", "", line)

con <- file("stdin", open = "r")
source("./calculatePiFunction.R")
while (length(line <- readLines(con, n = 1, warn = FALSE)) > 0) {
	x <- as.numeric(trimWhiteSpace(line))
	set.seed(x)	
	myOutput <- estimatePi(1e5)				
	cat(line, rawToChar(serialize(myOutput, NULL, ascii=T)),  "|\n", sep = "")
}

close(con)

