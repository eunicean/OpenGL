from OpenGL.GL import *
from numpy import array, float32

class Buffer(object):
    def __init__(self, data) :
        self.vertBuffer = array(data, dtype=float32)
        #Vertex Buffer Object
        self.VBO = glGenBuffers(1)
        #Vertex Array Object
        self.VAO = glGenVertexArrays(1)