from pybrain.structure import RecurrentNetwork
n = RecurrentNetwork()

n.addInputModule(LinearLayer(2, name='in'))
n.addModule(SigmoidLayer(3, name='hidden'))
n.addOutputModule(LinearLayer(1, name='out'))
n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))
n.addRecurrentConnection(FullConnection(n['hidden'], n['hidden'], name='c3'))


n.sortModules()
n.activate((2, 2))
array([-0.1959887])
n.activate((2, 2))
array([-0.19623716])
n.activate((2, 2))
array([-0.19675801])
n.reset() #clears history
