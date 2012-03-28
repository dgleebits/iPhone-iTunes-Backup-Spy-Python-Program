############## this starts the job assuming you have your credentials.json set up properly
############## it also assumes the mapper.R/reducer.R/calculatePiFunction.R are all in a bucked called emrexample
############## Output goes to emrout on S3 which must NOT exist before this is run
############## the file numberList.txt is not in this gist because it is 10,000 lines long: each line is simply an integer from 1:10000
############## numberList.txt needs to be created and placed in your S3 emrexample bucket
############## you will also need the Amazon EMR command line tools: http://docs.amazonwebservices.com/ElasticMapReduce/latest/DeveloperGuide/DownloadingtheCLI.html
############## and S3CMD: http://s3tools.org/s3cmd

system("elastic-mapreduce --create  --stream  --input s3n://emrexample/numberList.txt   --mapper s3n://emrexample/mapper.R  --reducer s3n://emrexample/reducer.R --output s3n://emrout/  --name EMRexample  --num-instances 50  --cache s3n://emrexample/calculatePiFunction.R#calculatePiFunction.R")

########### Don't run the rest of this until the job is done ########################
#you have to have s3cmd for this to work
#copies the results back
system("s3cmd get s3://emrexample/out/* .")

require(Hmisc) #for the substring.location() function

#be sure and change this path...
basePath <- "/home/jal/Documents/R/EMR Example/output/"

fileList <- list.files(path=basePath)

fi <- 1
fileResults <- NULL

for (fi in 1:length(fileList)){
	fname <- paste(basePath, fileList[fi], sep = "")
	tst <- readChar(fname, file.info(fname)$size)
	spt <- strsplit(tst, "|", fixed=T) 

	singleFileResults <- NULL

	for (i in 1:(length(spt[[1]])-1)) {
		spt2 <- substr(spt[[1]][i], substring.location(spt[[1]][i], "\tA")$first+1, nchar(spt[[1]][i]))
		results <- unserialize(charToRaw(spt2))
		singleFileResults[[i]] <- results
	}

fileResults[[fi]] <- singleFileResults
}

f <- unlist(fileResults)

cat("estimate of pi is:  ", mean(f), "\n")

