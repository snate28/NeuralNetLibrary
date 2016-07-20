#activation functions
import numpy as np
def sigmoid(input):
    return 1/(1+np.e**-input)
        
def ReLu(input,threshold = 0):
    return input*(input>threshold)
        
def Tanh( input):
    return (np.e**input-np.e**-input)/(np.e**input+np.e**-input)
        # can be just np.tanh(input)
def LeakyReLu(input,constant = 0.01):
    return 1*(input<0)*(constant*input)+1*(input>=0)*input
        

