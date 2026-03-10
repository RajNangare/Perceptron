import math



class Activation_Function:

    def sigmoid(self, input):
        return 1 / (1 + math.exp(-input))
    
    def linear(self, input):
        return input
    
    def tanh(self, input):
        return (math.exp(input) - math.exp(-input)) / (math.exp(input) + math.exp(-input))
    
