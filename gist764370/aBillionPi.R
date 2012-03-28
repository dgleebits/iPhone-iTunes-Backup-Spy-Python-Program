estimatePi <- function(seed){
  set.seed(seed)
  numDraws <- 1e6
  r <- .5 #radius... in case the unit circle is too boring
  x <- runif(numDraws, min=-r, max=r)
  y <- runif(numDraws, min=-r, max=r)
  inCircle <- ifelse( (x^2 + y^2)^.5 < r , 1, 0)
  return(sum(inCircle) / length(inCircle) * 4)
}

seedList <- as.list(1:1e3)

require(segue)
myCluster <- createCluster(20)
myEstimates <- emrlapply( myCluster, seedList, estimatePi )
stopCluster(myCluster)

myPi <- Reduce(sum, myEstimates) / length(myEstimates)

format(myPi, digits=10)


