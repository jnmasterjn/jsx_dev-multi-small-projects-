#BAR GRAPH 
#The most basic graph 

#load dataset
library(datasets)

#choose a dataset
head(mtcars)
?mtcars

#in order to make a bar chart, we need to make data into a table just like what we do in excel
cylinder <- table(mtcars$cyl)
cylinder
barplot(cylinder) #bar chat
plot(cylinder) #default chart, simple