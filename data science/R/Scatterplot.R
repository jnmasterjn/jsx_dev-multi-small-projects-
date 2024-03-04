#Scatter Plot 
#Visualize the association between two quantitative variables

par(mfrow = c(1,1))

#load data and stuff
library(datasets)
?mtcars
head(mtcars)

#first check the variables seperately
hist(mtcars$wt)
hist(mtcars$mpg)

#basic x y plot for the two variables
plot(mtcars$wt, mtcars$mpg)

#go with some options

plot(mtcars$wt, mtcars$mpg,
     pch = 17, #solid triangle
     cex = 1.5, #size is 50% bigger (1 is defualt)
     col = "pink",
     main = "MPG as a funtion of Weights of Cars",
     xlab = "Weight",
     ylab = "MPG"
     )
