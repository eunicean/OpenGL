import pygame
import glm
from pygame.locals import *
from gl import Renderer
from model import Model
from shaders import *

width = 960
height = 540

pygame.init()

screen = pygame.display.set_mode((width,height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)


rend.setShader(vertex_shader, fragment_shader)


# #           POSITION        #COLOR
# triangleData = [-0.5, -0.5, 0,  1.0, 0.0, 0.0,
#                    0,  0.5, 0,  0.0, 1.0, 0.0,
#                  0.5, -0.5, 0,  0.0, 0.0, 1.0]

# #               POSITIOn        UVs
# triangleData = [-0.5, -0.5, 0,  0.0, 0.0,   0.0,0.0,1.0,
#                 -0.5,  0.5, 0,  0.0, 1.0,   0.0,0.0,1.0,
#                  0.5, -0.5, 0,  1.0, 0.0,   0.0,0.0,1.0,
                 
#                 -0.5,  0.5, 0,  0.0, 1.0,   0.0,0.0,1.0,
#                  0.5,  0.5, 0,  1.0, 1.0,   0.0,0.0,1.0,
#                  0.5, -0.5, 0,  1.0, 0.0,   0.0,0.0,1.0]

# triangleModel = Model(triangleData)
# triangleModel.loadTexture("cea.jpg")
# triangleModel.position.z = -5
# triangleModel.scale = glm.vec3(3,3,3)

# rend.scene.append(triangleModel)

penguin = rend.loadModel(filename="PenguinBaseMesh.obj",texture="PenguinDiffuseColor.bmp")

isRunning = True
while isRunning:
    deltaTime = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()

    for evente in pygame.event.get():
        if evente.type == pygame.QUIT:
            isRunning = False
        elif evente.type == pygame.KEYDOWN:
            if evente.type == pygame.K_ESCAPE:
                isRunning = False


    vel = 5
    if keys[K_d]:
        penguin.rotation.x += vel * deltaTime
    if keys[K_a]:
        penguin.rotation.x -= vel * deltaTime
    if keys[K_w]:
        penguin.rotation.z += vel * deltaTime
    if keys[K_s]:
        penguin.rotation.z -= vel * deltaTime
    if keys[K_q]:
        penguin.rotation.y += vel * deltaTime
    if keys[K_e]:
        penguin.rotation.y -= vel * deltaTime


    rend.render()
    pygame.display.flip()

pygame.quit()
#31:40 min vid 26sep