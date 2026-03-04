import random as re

class split:
    def __init__(self, train_split, test_split):
        self.train_n = train_split
        self.test_n = test_split
    

    def random_split(self, input, output, n):
        #order for the input to be choosed
        order = []

        #to keep unique
        s = set()

        for i in range(int(self.test_n * n)):
            val = int(re.uniform(0, n - 1))
            if val not in s:
                order.append(val)
                s.add(val)




        X_train = []
        X_test = []
        y_train = []
        y_test = []

        for i in order:
            X_test.append(input[i])
            y_test.append(output[i])
        

        for i in range(n):
            if i not in s:
                X_train.append(input[i])
                y_train.append(output[i])


        return X_train, X_test, y_train, y_test

        

