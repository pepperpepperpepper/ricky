from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import SoftmaxLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer


class BinaryClassifier(object):
    def __init__(self):
        self._default_hidden_layers = 3
        pass

    def _train(self, dataset):
        """
        pybrain.tools.shortcuts.buildNetwork(*layers, **options)
        Build arbitrarily deep networks.

        layers should be a list or tuple of integers, that
        indicate how many neurons the layers should have.
        bias and outputbias are flags to indicate whether
        the network should have the corresponding biases;
        both default to True.
        """
        net = buildNetwork(
            dataset.params_length,
            self._default_hidden_layers,
            1  # a binary classifier only requires one output layer
        )
        ds = SupervisedDataSet(dataset)
        trainer = BackpropTrainer(net, ds)
        trainer.trainUntilConvergence()
        net.activate(params.as_serialized)

    def classify(self, dataset):
        return False
