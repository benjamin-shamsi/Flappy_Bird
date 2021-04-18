#Benjamin Shamsi




#Basic settings
TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 710

#Distance between two pipes
gap = 140

#Gravity of the game
gravity = 0.3

#Speed of the whole Game
scroll_speed = -1

#Making Actors
bird = Actor('bird1')
top_pipe = Actor('top')
bottom_pipe = Actor('bottom')

#Background
BGImage = 'background'

def draw():
    #Drawing Background
    screen.blit(BGImage, (0, 0))

    #Drawing the Objects
    bird.draw()
    top_pipe.draw()
    bottom_pipe.draw()


def update():
    bird.speed += gravity

    #Moving The Bird Down
    bird.y += bird.speed

    #Reset the bird
    if bird.y > HEIGHT:
        reset()

    #Moving the pipes to the left
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed

    #Bring the pipes back to the screen
    if top_pipe.right < 0:
        top_pipe.left = WIDTH
        bottom_pipe.left = WIDTH

    #Bird hitting the pipes
    if bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe):
        hit_pipe()


#Move the Bird to the top
def on_mouse_down():
    if bird.alive == True:
        print('MOUSE IS CLICKED')

    #bird.y -= 50
    if bird.alive == True:
        bird.speed = -6.5



#Resets everything in the Game to the first
def reset():
    print('resetting the bird')

    #reset the speed of the bird
    bird.speed = 1

    #reset position of the bird
    bird.center = (75, 350)

    #reset position of the pipes
    top_pipe.center = (300, 0)
    bottom_pipe.center = (300, top_pipe.height + gap)

    #Bird is alive
    bird.alive = True
    bird.image = 'bird1'


#Changing the Bird style
def hit_pipe():
    print('bird is dead')

    #Changing the bird image tothe dead one
    bird.image = 'birddead'

    #Bird is dead
    bird.alive = False

#print(top_pipe.width, top_pipe.height)

#First positioning of the Actor and Speed
reset()