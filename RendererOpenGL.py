import pygame
import glm
from pygame.locals import *
from gl import Renderer
from model import Model
from shaders import *
from OpenGL.GL import glClear, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT

width = 960
height = 540

pygame.init()

screen = pygame.display.set_mode((width,height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

pygame.mixer.music.load("aot.mp3")
pygame.mixer.music.play(-1)

print("""--- Comandos ---
    Mouse:
        Scroll up:    Aleja la camara
        Scroll down:  Acerca la camara
    Teclado:
        Movimientos
        A:  Mueve camara hacia la izquierda
        D:  Mueve camara hacia la derecha
        W:  Mueve camara hacia arriba
        S:  Mueve camara hacia abajo
        X:  Rotar modelo hacia la derecha
        Z:  Rotar modelo hacia la izquieda
        Modelos:
        1:  Pinguino
        2:  Oso con silla
        3:  Panito
        4:  Espada
        Shaders
        5:  Normal
        6:  TV noise
        7:  Ballon
        8:  Neon Party""")

rend = Renderer(screen)

rend.setShader(vertex_shader, fragment_shader)

model = [
    rend.loadModel(filename="modelos/PenguinBaseMesh.obj",texture="texturas/PenguinDiffuseColor.bmp"),
    rend.loadModel(filename="modelos/BearSaddle.obj",texture="texturas/MaterialLightBrown.png", rotation=(0,180,0)),
    rend.loadModel(filename="modelos/Bread.obj",texture="texturas/Bread.jpg", position=(0,0,-5), scale=(15,15,15)),
    rend.loadModel(filename="modelos/Viking Sword.obj",texture = "texturas/VikingSword.png", position=(0,0,-5),rotation=(0,90,0), scale=(5,5,5))
]
active_model_index = 0

radius = 5.0
angle = 0.0

rend.scene.append(model[active_model_index])

isRunning = True
zoom_factor = 1.0
while isRunning:
    deltaTime = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()


    for evente in pygame.event.get():
        if evente.type == pygame.QUIT:
            isRunning = False
        elif evente.type == pygame.KEYDOWN:
            if evente.type == pygame.K_ESCAPE:
                isRunning = False
            if evente.key == pygame.K_1:
                active_model_index = 0
            if evente.key == pygame.K_2:
                active_model_index = 1
            if evente.key == pygame.K_3:
                active_model_index = 2
            if evente.key == pygame.K_4:
                active_model_index = 3

        elif evente.type == pygame.MOUSEBUTTONDOWN:
            if evente.button == 4: #rodar hacia arriba
                if rend.camPosition.z < 5.0:
                    rend.camPosition.z += 0.5
            if evente.button == 5: #rodar para abajo
                if rend.camPosition.z > -4.5:
                    rend.camPosition.z -= 0.5

    active_model = model[active_model_index]
    rend.scene = [active_model]
    
    vel = 9
    if keys[K_d]:
        angle += 0.8 * deltaTime
        rend.camPosition.x = active_model.position.x + cam_radius * glm.cos(angle)
    if keys[K_a]:
        angle -= 0.8 * deltaTime
        rend.camPosition.x = active_model.position.x + cam_radius * glm.cos(angle)
    if keys[K_w]:
        angle += 0.8 * deltaTime
        rend.camPosition.y = active_model.position.y + cam_radius * glm.sin(angle)
    if keys[K_s]:
        angle -= 0.8 * deltaTime
        rend.camPosition.y = active_model.position.y + cam_radius * glm.sin(angle)

    cam_radius = radius
    cam_height = 2.0
    
    rend.camTarget = active_model.position
    

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    
    
    if keys[K_z]:
        active_model.rotation.y += 70 * deltaTime
    if keys[K_x]:
        active_model.rotation.y -= 70 * deltaTime
    if keys[K_5]:
        rend.setShader(vertex_shader, fragment_shader)
    if keys[K_6]:
        rend.setShader(vertex_shader, noise_fragment_shader)
    if keys[K_7]:
        rend.setShader(ballon_vertex_shader, ballon_fragment_shader)
    if keys[K_8]:
        rend.setShader(vertex_shader, color_fragment_shader)

    rend.elapsedTime += deltaTime
    rend.render()
    pygame.display.flip()

pygame.quit()