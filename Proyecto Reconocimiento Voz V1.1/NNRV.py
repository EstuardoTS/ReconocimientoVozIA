from pybrain.tools.shortcuts import buildNetwork
#from pybrain.structure import TanhLayer
from pybrain.structure.modules import SigmoidLayer, LSTMLayer,LinearLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

# Create a neural network with two inputs, three hidden, and one output
#TanhLayer
net = buildNetwork(6, 10, 4, bias=True, hiddenclass=SigmoidLayer)

# Create a dataset that matches NN input/output sizes:
RecVoice = SupervisedDataSet(6, 4)

# Add input and target values to dataset
# Values correspond to XOR truth table
RecVoice.addSample((5.03765443, -4.91747495, 1.16557777, 2.54495674, -5.87675429, 2.55821221), (1, 0, 0, 0))
RecVoice.addSample((0.80438469,	-1.70752047, -0.11393426, 1.31285914, -1.86314206, 0.02671551), (0, 1, 0, 0))
RecVoice.addSample((4.69720506, -1.77711417, -1.20990075, 0.71086019, -0.64044225, 4.48441995), (0, 0, 1, 0))
RecVoice.addSample((2.04424812, -4.69246883, 3.29483815, 3.26663668, -2.38758877, 1.87432863), (0, 0, 0, 1))
RecVoice.addSample((4.97519228,	-9.84669948, -6.34554744, -9.62489343, 8.9544877, -7.41328398), (0, 0, 0, 0))
RecVoice.addSample((4.164547, -6.18263321, -2.85650935, -3.10354024, -1.23278981, 11.04671741), (0, 0, 0, 0))
RecVoice.addSample((0.62421269, 23.52099536, -3.53143154, 12.346209, 12.07340704, 7.86004438), (0, 0, 0, 0))

trainer = BackpropTrainer(net, RecVoice)
#trainer.trainUntilConvergence()
for epoch in range(1000):
    trainer.train()

testdata = RecVoice
trainer.testOnData(testdata, verbose = True)  # Works if you are lucky!
