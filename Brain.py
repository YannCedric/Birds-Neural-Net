import numpy

class Brain: 
    def __init__(self, inputs):
        self.input_layers_size = inputs + 1
        self.hidden_layers_size = 3 + 1
        self.output_layers_size = 1 

        self.input_weights = numpy.random.randn(self.input_layers_size, self.hidden_layers_size)
        self.hidden_weights = numpy.random.randn(self.hidden_layers_size, self.output_layers_size)

    def sigmoid(self, x):
        return 1/(1 + numpy.exp(-x))

    def feedfoward(self,inputs_array):
        inputs_array.append(1)

        hidden_activations = self.sigmoid(numpy.dot(inputs_array,self.input_weights))

        hidden_activations[len(hidden_activations)-1] = 1

        outputs = self.sigmoid(numpy.dot(hidden_activations, self.hidden_weights))

        return self.sigmoid(outputs)