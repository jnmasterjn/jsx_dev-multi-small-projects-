#PLOT

#get the data
library(datasets)

#head() is use to view the first few rows of a datasets
head(iris)

#? is to get help 
?plot 

#graph examples

#the dollar sigh is telling the computer where to find the data from, it's like / in vs code
plot(iris$Species) #catetorgorical variable
plot(iris$Petal.Length) #quantitative data
plot(iris$Species, iris$Petal.Length)
plot(iris$Petal.Length, iris$Sepal.Length)
plot(iris) #this give you all the plots that can be drawn with the data given

#graph with options / customization

plot(iris$Petal.Length, iris$Petal.Width,
     pch = 19, # plot character for the graph 
     main = "Iris: The relation between Petal's Length and Width", #the main title of the graph
     xlab = "Petal's width", #title for x axis 
     ylab = "Petal's length") #title for y axis 


#graph given formulas using plot()

plot(cos,0,2*pi)
plot(sin,0,10*pi)
plot(exp,0,9)
plot(dnorm,-3,+3)
plot(pnorm,-3,+3)

#can also decorate it with options
plot(dnorm,-3,+3,
     main = "Math score",
     ylab = "Unit of test",
     xlab = "Score")

# control + l to clean console





