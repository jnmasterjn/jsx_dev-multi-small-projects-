#overlaying graphs tells more information than a graph with just one kind of presented mode.  
library(datasets)
 ?lynx
 head(lynx)
 
 #histogram- only one variable don't need to specify
 hist(lynx)
 
par(mfrow=c(1,1)) 
 #histogram with options
 hist(lynx,
      breaks= 10,
      freq = FALSE,
      col= "pink",
      main = "Histogram of Lynx Trapping, 1821-1934",
      xlab= "Numbers of Lynx trapped")
 
 #add a normal distribution on the graph
 #normal distribution is aka bell shaped curve, it is determined by standard deviation and mean 
 
 curve(dnorm(x, mean = mean(lynx), sd = sd(lynx)),
       col = "black", 
       lwd = 3, #line width
       add = TRUE) #stick it on the previous graph
 
 #adding rug plot, 可以看分佈 , shows indivual data and give a better understanding of why does the graph looks like this
 
 rug (lynx, lwd = 2, col = "gray")
 