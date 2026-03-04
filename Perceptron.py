import random as rm
class Perceptron: 

    # Constructor to initialize     
    def __init__(self, n, lr = 0.1):
        self.lr = lr
        self.weight = [rm.uniform(-1, 1) for i in range(n)]
        self.weight_lenght = n
        self.bias = rm.uniform(-1, 1)


    # activation function of step activation function
    def activation(self, input):
        if (input >= 0):
            return 1
        return 0
    


    #forward pass

    def predict(self, input):
        
        sum = 0

        for i in range(self.weight_lenght):
            sum += input[i] * self.weight
        
        sum += self.bias

        active = self.activation(sum)

        return active
    

    # Backward pass (Back Propagation)
    # also called as training


    def train(self, inputs, target, epochs = 100):
        # input is 2D matrix where mutliple input input and there features are give in one list
        # target is 1D with expected output
        for epoch in range(epochs):

            for iter in range(len(inputs)):

                pred = self.predict(inputs[iter])

                error = target[iter] - pred

                for i in range(self.weight_lenght):
                    # letting error decide to minus or plus 
                    self.weight[i] += error * self.lr * inputs[iter][i]

                self.bias += error * self.lr

# Testing
P = Perceptron(100, 0.01)
print(P.lr)
print(P.weight)


    

