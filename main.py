import sys, pygame, numpy
from multiprocessing import Process

pygame.init()

FPS = 165
freq = 440
sampleRate = 44100
fpsClock = pygame.time.Clock()

size = width, height = 720, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

pygame.mixer.init(frequency=44100,size=-16,channels= 2, buffer=512)

arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * freq * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
arr2 = numpy.c_[arr,arr]
sound = pygame.sndarray.make_sound(arr2)

def play_sound():
    print('init')
    sound.play(-1)
    pygame.time.delay(500)
    sound.stop()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        p = Process(target=play_sound)
        p.start()

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        p = Process(target=play_sound)
        p.start()


    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    fpsClock.tick(FPS)

pygame.mixer.stop()