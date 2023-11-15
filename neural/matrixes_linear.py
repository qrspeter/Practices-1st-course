import numpy as np

tr_inputs = np.array([[0, 0, 0], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
#tr_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
tr_outputs = np.array([[1], [1], [1], [0]])
weigths = np.array([[1], [1], [1]])
analysed = np.array([1, 0, 0])
attenuate = 0.1

error = 10
trainings = 0
pre_error = error + 1
while error > 1e-3 and trainings < 10000:
#for i in range(trainings):
    outputs = np.dot(tr_inputs, weigths)
    errors = outputs - tr_outputs
    delta = np.dot(tr_inputs.T, errors)
    weigths = weigths - attenuate * delta
    error = np.sum(errors * errors)
    result = np.dot(analysed, weigths)
    if error == pre_error:
        print("Error has been minimised!")
        break
    trainings += 1
    pre_error = error
    print(error)
    
print(f'trainings={trainings}, result={float(result)}')
print(f'{trainings=}, {result=}')
print(f'{trainings}, {result}')




