from ursina import *
import serial

s = serial.Serial('COM4')
s.baudrate = 9600
# while True:
#     res = s.readline()
#     result_input = str(res).strip()
#     result_input_string = result_input[2] + result_input[3]
#     print(result_input_string)


app = Ursina()
window.color = color.azure

AmbientLight(color=(0.5, 0.5, 0.5, 1))  # общее освещение
DirectionalLight(color=(0.5, 0.5, 0.5, 1), direction=(1, 1, 1))
cub = Entity(model="ImageToStl.com_никто не догадается что в этом файле совсем не хехе.obj", rotation=(0, 0, 0),
             position=(0, 0, 0), scale=(0.5, 0.5, 0.5), color=color.black90)

# Entity(model="cube", parent=cub, scale=(4, 4, 4), color=color.olive, position=(5, 0, 0))
# Entity(model="cube", parent=cub, scale=(4, 4, 4), color=color.olive, position=(0, 5, 0))
# Entity(model="cube", parent=cub, scale=(4, 4, 4), color=color.olive, position=(0, 0, 5))

x_handler = Entity()
y_handler = Entity()
z_handler = Entity()

# def adxl_rotation():
#     res = s.readline()
#     result_input = str(res).strip()
#     result_input_string = result_input[2] + result_input[3]
#     if result_input_string == "+Z":
#         return held_keys['e']
#     elif result_input_string == "-Z":
#         return held_keys['d']
#     elif result_input_string == "+Y":
#         return held_keys['w']
#     elif result_input_string == "-Y":
#         return held_keys['s']
#     elif result_input_string == "+X":
#         return held_keys['q']
#     elif result_input_string == "-X":
#         return held_keys['a']

def switch(entity, parent):
    old_world_rotation = entity.world_rotation
    entity.parent = parent
    entity.world_rotation = old_world_rotation


def update():
    old_parent = cub.parent
    switch(cub, x_handler)
    res = s.readline()
    result_input = str(res).strip()
    result_input_string = result_input[2] + result_input[3]
    if result_input_string == "+X":
        x_handler.rotation_x += 100 * time.dt
    elif result_input_string == "-X":
        x_handler.rotation_x -= 100 * time.dt

    switch(cub, y_handler)
    if result_input_string == "+Y":
        y_handler.rotation_y += 100 * time.dt

    elif result_input_string == "-Y":
        y_handler.rotation_y -= 100 * time.dt

    switch(cub, z_handler)
    if result_input_string == "+Y":
        z_handler.rotation_z += 100 * time.dt
    elif result_input_string == "-Z":
        z_handler.rotation_z -= 100 * time.dt

    switch(cub, old_parent)

app.run()
