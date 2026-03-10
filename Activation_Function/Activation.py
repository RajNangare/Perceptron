import math



class Activation_Function:

    def sigmoid(self, input):
        return 1 / (1 + math.exp(-input))