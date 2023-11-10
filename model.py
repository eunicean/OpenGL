import glm
from OpenGL.GL import *
from numpy import array, float32
import pygame

class Model(object):
    def __init__(self, data) :
        self.vertBuffer = array(data, dtype=float32)
        #Vertex Buffer Object
        self.VBO = glGenBuffers(1)
        #Vertex Array Object
        self.VAO = glGenVertexArrays(1)

        self.position = glm.vec3(0,0,0)
        self.rotation = glm.vec3(0,0,0)
        self.scale = glm.vec3(1,1,1)

    def loadTexture(self, textureName):
        self.textureSurface     = pygame.image.load(textureName)
        self.textureData        = pygame.image.tostring(self.textureSurface, "RGB", True)
        self.textureBuffer      = glGenTextures(1)

    def getModelMatrix(self):
        identity = glm.mat4(1)

        translateMat = glm.translate(identity, self.position)

        # Rotation x - Pitch
        pitch = glm.rotate(identity, glm.radians(self.rotation.x), glm.vec3(1,0,0))
        # Rotation y - Yaw
        yaw   = glm.rotate(identity, glm.radians(self.rotation.y), glm.vec3(0,1,0))
        # Rotation z - Roll
        roll  = glm.rotate(identity, glm.radians(self.rotation.z), glm.vec3(0,0,1))

        rotationMat = pitch * yaw * roll

        scaleMat = glm.scale(identity, self.scale)

        return translateMat * rotationMat * scaleMat
    
    def render(self): 
        # Ata los buffer del objeto a la GPU
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBindVertexArray(self.VAO)

        #Especificar la informacion de vertices
        glBufferData(GL_ARRAY_BUFFER,               #BufferID
                    self.vertBuffer.nbytes,      #Buffer Size in Bytes
                    self.vertBuffer,             #Buffer Data
                    GL_STATIC_DRAW)                #Usage
        
        #Atributos de posiciones
        glVertexAttribPointer(0,                    #Atribute number
                              3,                    #Size
                              GL_FLOAT,             #Type
                              GL_FALSE,             #Is it normalize
                              4 * 8,                #Stride
                              ctypes.c_void_p(0))   #offset
        glEnableVertexAttribArray(0)

        #Atributo de coordenadas de textura
        glVertexAttribPointer(1,                    #Atribute number
                              2,                    #Size
                              GL_FLOAT,             #Type
                              GL_FALSE,             #Is it normalize
                              4 * 8,                #Stride
                              ctypes.c_void_p(4*3)) #offset
        glEnableVertexAttribArray(1)

        #Atributo de coordenadas de textura
        glVertexAttribPointer(2,                    #Atribute number
                              3,                    #Size
                              GL_FLOAT,             #Type
                              GL_FALSE,             #Is it normalize
                              4 * 8,                #Stride
                              ctypes.c_void_p(4*5)) #offset
        glEnableVertexAttribArray(2)

        #Activar las texturas
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.textureBuffer)
        glTexImage2D(GL_TEXTURE_2D,
                    0,
                    GL_RGB,
                    self.textureSurface.get_width(),
                    self.textureSurface.get_height(),
                    0,
                    GL_RGB,
                    GL_UNSIGNED_BYTE,
                    self.textureData)
        glGenerateTextureMipmap(self.textureBuffer)
        
        glDrawArrays(GL_TRIANGLES, 0, int(len(self.vertBuffer) / 8))