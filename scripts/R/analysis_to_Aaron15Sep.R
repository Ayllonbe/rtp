#Loading data
datas <- read.csv("preprocessed_nnDataInput.csv")
summary(datas)

#Backup data to get a cleanear data set
datas_clean <- datas

#Select data
datas_sele <- datas_clean[,c(3,5:17)]

set.seed(453)

#Create training and test data sets
dt = sort(sample(nrow(datas_sele), nrow(datas_sele)*.8))
train<-datas_sele[dt,]
test<-datas_sele[-dt,]



##### SVM
library(kernlab)
system.time(
svm <- ksvm(Link~., data=train, kernel="rbfdot")
)
pred <- predict(svm, test[,-1])
table(observed=test[,1],predicted=pred)

##### RF
library(randomForest)

system.time(
  rf <- randomForest(Link~., data=train, ntree=1000,mtry=4)
)

# Validation set assessment #1: looking at confusion matrix
prediction_for_table <- predict(rf,test[,-1])
table(observed=test[,1],predicted=prediction_for_table)

##### NN
library(neuralnet)
system.time(
nnet <- neuralnet(Link~. ,data=train, hidden=c(5,5), stepmax=1e7 )
)
pred <- predict(nnet, test[,-1])
table(observed=test[,1],predicted=pred)


