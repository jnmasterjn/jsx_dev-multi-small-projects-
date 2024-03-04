#Histogram 
#For data that r quantitative, in this case use to compare between different species

#load data first
library(datasets)

#choose the data set
?iris
head(iris)

#basic histogram
hist(iris$Sepal.Length)
hist(iris$Sepal.Width)

#plot by groups#

#check all the species
plot(iris$Species)

#put graph in 3 rows and 1 column
par (mfrow = c(3,1) )

#histogram by speices with option
hist(iris$Petal.Width [iris$Species == "setosa"],
     xlim = c(0,2.5),
     breaks = 9,
     main = "Petal Width for Setosa",
     x_lab = "",
     col = "green")

hist(iris$Petal.Width [iris$Species == "versicolor"],
     xlim = c(0,2.5),
     breaks = 9,
     main = "Petal Width for Versicolor",
     x_lab = "",
     col = "pink")
     
hist(iris$Petal.Width [iris$Species == "virginica"],
     xlim = c(0,2.5),
     breaks = 10,
     main = "Petal Width for Virginica",
     x_lab = "",
     col = "blue")

#change back to normal graph
par (mfrow = c(1,1))
