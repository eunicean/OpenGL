from OpenGL.GL import *
from numpy import array, float32

class Buffer(object):
    def __init__(self, data) :
        self.vertBuffer = array(data, dtype=float32)
        #Vertex Buffer Object
        self.VBO = glGenBuffers(1)
        #Vertex Array Object
        self.VAO = glGenVertexArrays(1)
    
    def render(self): 
        # Ata los buffer del objeto a la GPU
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBindVertexArray(self.VAO)

        #Especificar la informacion de vertices
        glBufferData(GL_ARRAY_BUFFER,               #BufferID
                     self.vertBuffer.nbytes,      #Buffer Size in Bytes
                     self.vertBuffer,             #Buffer Data
                     GL_STATIC_DRAW)                #Usage
        
        #Atributos
        #Especificar que representa el contenido del vertice
        glVertexAttribPointer(0,                    #Atribute number
                              3,                    #Size
                              GL_FLOAT,             #Type
                              GL_FALSE,             #Is it normalize
                              4 * 3,                  #Stride
                              ctypes.c_void_p(0))   #offset
        glEnableVertexAttribArray(0)


        glDrawArrays(GL_TRIANGLES, 0, int(len(self.vertBuffer) / 3))