def confusion_matrix(predicted, expected):
    confusion = []
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0


    for i in range(len(predicted)):
        if predicted[i] == expected[i]:
            if predicted[i] == 1:
                true_positive += 1
            else:
                true_negative += 1
        else:
            if predicted[i] == 1:
                false_positive += 1
            else:
                false_negative += 1
    


    confusion.append([true_positive, false_negative])
    confusion.append([false_positive, true_negative])


    
    # Accuracy, Precision and etc calcalation to be done here
