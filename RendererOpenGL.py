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


rend.setShader(vertex_shader, noise_fragment_shader)


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
rend.scene.append(penguin)

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


    vel = 9
    if keys[K_d]:
        rend.camPosition.x += vel * deltaTime
    if keys[K_a]:
        rend.camPosition.x -= vel * deltaTime
    if keys[K_w]:
        rend.camPosition.z += vel * deltaTime
    if keys[K_s]:
        rend.camPosition.z -= vel * deltaTime
    if keys[K_q]:
         rend.camPosition.y += vel * deltaTime
    if keys[K_e]:
         rend.camPosition.y -= vel * deltaTime
    if keys[K_z]:
        penguin.rotation.y += 70 * deltaTime
    if keys[K_x]:
        penguin.rotation.y -= 70 * deltaTime
    if keys[K_1]:
        rend.setShader(vertex_shader, fragment_shader)
    if keys[K_2]:
        rend.setShader(vertex_shader, noise_fragment_shader)
    if keys[K_3]:
        rend.setShader(ballon_vertex_shader, ballon_fragment_shader)
    if keys[K_4]:
        rend.setShader(vertex_shader, color_fragment_shader)

    # penguin.rotation.y += 45 * deltaTime

    rend.elapsedTime += deltaTime       

    rend.render()
    pygame.display.flip()

pygame.quit()
#31:40 min vid 26sep