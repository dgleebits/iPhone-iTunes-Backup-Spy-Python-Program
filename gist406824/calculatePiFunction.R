estimatePi <- function(numDraws){
	r <- .5 #radius... in case the unit circle is too boring
	x <- runif(numDraws, min=-r, max=r) 
	y <- runif(numDraws, min=-r, max=r)
	inCircle <- ifelse( (x^2 + y^2)^.5 < r , 1, 0)
	return(sum(inCircle) / length(inCircle) * 4)
}