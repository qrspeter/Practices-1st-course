import numpy as np
import matplotlib.pyplot as plt

tr_inputs = np.array(
[[0, 0.3, 0.5, 1, 0.5, 0], 
[0, 1, 0.6, 0.3, 0.2, 0.1], 
[0, 0.8, 0.9, 0.6, 0.3, 0], 
[0, 0.2, 0.3, 0.4, 0.5, 0.1]])
tr_outputs = np.array([[0], [1], [1], [0]])
weigths = np.array([[0], [0], [0], [0], [0], [0]])
analysed = np.array([0.3, 0.6, 0.7, 0.8, 0.3, 0])
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
if result >= 0.5:
    print('Образец А')
else:
    print('Образец B')
print(f'{trainings=}, {result=}')
print(weigths)

for n,i in enumerate(tr_inputs):
    plt.plot(i,color = (lambda x:'red' if x==1 else 'blue')(tr_outputs[n,0]), label = (lambda x:'A' if x==1 else 'B')(tr_outputs[n,0]))
plt.plot(analysed, color='green', label = 'predicted '+(lambda x:'A' if x==1 else 'B')(round(float(result))))
plt.text(1, 0.1, f'result={float(result):.2f}')
plt.legend()
plt.show()
