class Loss_Function:

    def hinge(self, expected, predicted):
        output = []
        for i in range(len(expected)):
            output.append(max(0, -expected[i] * predicted[i]))
        
        return output
    


