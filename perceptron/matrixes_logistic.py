import numpy as np

#tr_inputs = np.array([[0, 0, 0], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
tr_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
tr_outputs = np.array([[0], [1], [1], [0]])
weigths = np.array([[-5], [0], [5]])
analysed = np.array([1, 0, 0])
attenuate = 1

error = 10
trainings = 0
pre_error = error + 1
while error > 1e-3 and trainings < 10000:
#for i in range(trainings):
    outputs = 1 / (1 + np.exp(np.dot(tr_inputs, weigths)))
    errors = outputs - tr_outputs
    #delta = np.dot(errors, tr_inputs, outputs, (1 - outputs))
    delta = np.dot(tr_inputs.T, errors * outputs * (1 - outputs))
    weigths = weigths + attenuate * delta
    error = np.sum(errors * errors)
    result = 1 / (1 + np.exp(np.dot(analysed, weigths)))
    if error == pre_error:
        print("Error has been minimised!")
        break
    trainings += 1
    pre_error = error
    print(error)
    
print(f'{trainings=}, {result=}')
print(weigths)




