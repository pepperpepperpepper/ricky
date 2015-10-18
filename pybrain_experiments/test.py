from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
n = FeedForwardNetwork()

inLayer = LinearLayer(2)
hiddenLayer = SigmoidLayer(3)
outLayer = LinearLayer(1)

n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)

in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)


n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)


# everything is wired together now
# this makes it usable

n.sortModules()


if __name__ == "__main__":
    #Again, this might look different on your machine -
    #the weights of the connections have already been initialized randomly.
    print n.activate([1, 2])
    #look at the hidden weights
    print in_to_hidden.params
    print hidden_to_out.params
    print n.params #weights here too
