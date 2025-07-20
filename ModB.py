from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Rotasi
rotX, rotY = 0, 0
lastX, lastY = 0, 0
dragging = False

def initLighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # Ambient Light
    ambient = [0.2, 0.2, 0.2, 1.0]
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)

    # Diffuse Light
    diffuse = [0.7, 0.7, 0.7, 1.0]
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)

    # Specular Light
    specular = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular)

    # Posisi sumber cahaya
    position = [1.0, 1.0, 2.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, position)

    # Properti material untuk refleksi specular
    mat_specular = [1.0, 1.0, 1.0, 1.0]
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)  # semakin besar, semakin tajam highlight

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glShadeModel(GL_SMOOTH)  # Gunakan Gouraud shading

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Kamera
    gluLookAt(3, 3, 6, 0, 0, 0, 0, 1, 0)

    # Transformasi rotasi
    glRotatef(rotX, 1, 0, 0)
    glRotatef(rotY, 0, 1, 0)

    # Warna objek
    glColor3f(0.5, 0.6, 0.9)
    glutSolidCube(2)

    glutSwapBuffers()

def reshape(w, h):
    if h == 0:
        h = 1
    ratio = w / h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, ratio, 1, 100)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global rotX, rotY
    if key == b'w': rotX -= 5
    elif key == b's': rotX += 5
    elif key == b'a': rotY -= 5
    elif key == b'd': rotY += 5
    glutPostRedisplay()

def mouse(button, state, x, y):
    global dragging, lastX, lastY
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            dragging = True
            lastX = x
            lastY = y
        elif state == GLUT_UP:
            dragging = False

def motion(x, y):
    global rotX, rotY, lastX, lastY
    if dragging:
        rotX += (y - lastY)
        rotY += (x - lastX)
        lastX = x
        lastY = y
        glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Phong Lighting - Kubus 3D")

    glEnable(GL_DEPTH_TEST)
    initLighting()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)

    glutMainLoop()

if __name__ == '__main__':
    main()
