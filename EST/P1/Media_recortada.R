media_recortada <- function(x, trim = 0.2 ) {
  n = length(x)
  k = round(trim*n)
  if ( k < 0 | k >= n/2 ) stop("Valor de 'trim' incorrecto")
  
  
  x = sort(x)
  
  min = x[k +1 ]
  max = x[n - k]
  
  x[1:k] = min
  x[(n- k) :n] = max
  
  return(mean(x))
}