import csv

#inputs to store csv
X = []
y = []

#basic operaiton to open and extract data from the file
with open("Dataset/Iris.csv", 'r') as file:
    reader = csv.reader(file)
    next(reader)
    read = list(reader)
    # print(read)


    
    for i in range(len(read)):
        l = []
        for j in range(len(read[i]) - 1):
            l.append(float(read[i][j]))
        X.append(l)
        if read[i][-1] == "Iris-setosa":
            y.append(0)
        else:
            y.append(1)


#Testing 

# print(X)
# print(y)

from Train_Test import split
from Perceptron import Perceptron
n = len(X[0])

lr = 0.01 #standard

p = Perceptron(n, lr)
st = split(0.7, 0.3)

N = len(X)


X_train, X_test, y_train, y_test = st.random_split(X, y, N)


# print(X_test, y_test)
# print(len(y_test))
# print(X, y)









