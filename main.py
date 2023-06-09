from random import randint
import pygame
import button

# initialize pygame
pygame.init()

# All the variables
player_score = 0
computer_score = 0
r = True
p = True
s = True
eee = True
rbg1 = randint(0, 255)
rbg2 = randint(0, 255)
rbg3 = randint(0, 255)

# Define game screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

# FPS settings
clock = pygame.time.Clock()
FPS = 60

# Load background/others
bg = pygame.transform.scale(pygame.image.load("Photos/white_bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
reset_img = pygame.image.load("Photos/reset_btn.png")


# Load player images
player_rock_img = pygame.image.load("Photos/player_rock.png")
player_paper_img = pygame.image.load("Photos/player_paper.png")
player_scissors_img = pygame.image.load("Photos/player_scissors.png")

# Load computer images
computer_rock_img = pygame.image.load("Photos/computer_rock.png")
computer_paper_img = pygame.image.load("Photos/computer_paper.png")
computer_scissors_img = pygame.image.load("Photos/computer_scissors.png")

# Define fonts
font = pygame.font.SysFont("Futura", 60)
font_HUD = pygame.font.SysFont("Futura", 30)

# Define a function to render text on screen
def draw_text(text, font, text_color, x, y):
    label = font.render(text, True, text_color)
    screen.blit(label, (x, y))

def show_GameInfo():
    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(0, 0, 800, 60))
    draw_text("You: " + str(player_score), font_HUD, (0, 100, 0), 160, 10)
    draw_text("Computer: " + str(computer_score), font_HUD, (100, 0, 0), 480, 10)
    draw_text("---First to 5 WINS!---", font, (rbg1, rbg2, rbg3), 130, 550)

# Define rock Class
class ROCK(pygame.sprite.Sprite):
    # Define constructor
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.update_time = pygame.time.get_ticks()

    # Object methods
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

# Define paper Class
class PAPER(pygame.sprite.Sprite):
    # Define constructor
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # Object methods
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

# Define scissors Class
class SCISSORS(pygame.sprite.Sprite):
    # Define constructor
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # Object methods
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

# Create a button object
rock_button = button.Button(SCREEN_WIDTH - 720, 465, player_rock_img, 0.125)
paper_button = button.Button(SCREEN_WIDTH - 600, 465, player_paper_img, 0.1)
scissors_button = button.Button(SCREEN_WIDTH - 485, 465, player_scissors_img, 0.45)
reset_button = button.Button(SCREEN_WIDTH - 200, 465, reset_img, 0.08)

# Make the items displayed on the screen
player_rock = ROCK(45, 90, player_rock_img, 0.4)
player_paper = PAPER(60, 90, player_paper_img, 0.3)
player_scissors = SCISSORS(50, 120, player_scissors_img, 1.2)
computer_rock = ROCK(400, 90, computer_rock_img, 0.4)
computer_paper = PAPER(415, 90, computer_paper_img, 0.3)
computer_scissors = SCISSORS(405, 120, computer_scissors_img, 1.2)

# create list of playable options
options = ["Rock", "Paper", "Scissors"]
player_options = 0

# Displaying computers options
def comp_play():
    if computer_options == "Rock":
        computer_rock.draw(screen)
    elif computer_options == "Paper":
        computer_paper.draw(screen)
    else:
        computer_scissors.draw(screen)

# Define reset
def reset():
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(30, 60, 360, 360))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(390, 60, 360, 360))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(315, 420, 180, 35))


############### GAME LOOP ##################


run = True

screen.blit(bg, (0, 0))

while run:
    clock.tick(60)

    show_GameInfo()

    # Set up layout
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(30, 60, 360, 360), 1)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(390, 60, 360, 360), 1)

    # giving computer random option
    computer_options = options[randint(0, 2)]

    # Displaying players choice of play
    if rock_button.draw(screen) and r == True:
        p = False
        s = False
        player_rock.draw(screen)
        player_options = options[0]
        rbg1 = randint(0, 255)
        rbg2 = randint(0, 255)
        rbg3 = randint(0, 255)
        comp_play()
        if computer_options == "Rock":
            draw_text("DRAW", font_HUD, (0, 0, 150), 350, 420)
        elif computer_options == "Paper":
            draw_text("YOU LOSE!", font_HUD, (255, 0, 0), 315, 420)
            computer_score += 1
        else:
            draw_text("YOU WIN!", font_HUD, (0, 255, 0), 316, 420)
            player_score += 1
        r = False

    if paper_button.draw(screen) and p == True:
        r = False
        s = False
        player_paper.draw(screen)
        player_options = options[1]
        rbg1 = randint(0, 255)
        rbg2 = randint(0, 255)
        rbg3 = randint(0, 255)
        comp_play()
        if computer_options == "Paper":
            draw_text("DRAW", font_HUD, (0, 0, 150), 350, 420)
        elif computer_options == "Scissors":
            draw_text("YOU LOSE!", font_HUD, (255, 0, 0), 315, 420)
            computer_score += 1
        else:
            draw_text("YOU WIN!", font_HUD, (0, 255, 0), 316, 420)
            player_score += 1
        p = False

    if scissors_button.draw(screen) and s == True:
        p = False
        r = False
        player_scissors.draw(screen)
        player_options = options[2]
        rbg1 = randint(0, 255)
        rbg2 = randint(0, 255)
        rbg3 = randint(0, 255)
        comp_play()
        if computer_options == "Scissors":
            draw_text("DRAW", font_HUD, (0, 0, 150), 350, 420)
        elif computer_options == "Rock":
            draw_text("YOU LOSE!", font_HUD, (255, 0, 0), 315, 420)
            computer_score += 1
        else:
            draw_text("YOU WIN!", font_HUD, (0, 255, 0), 316, 420)
            player_score += 1
        s = False

    if reset_button.draw(screen) and eee == True:
        reset()
        rbg1 = randint(0, 255)
        rbg2 = randint(0, 255)
        rbg3 = randint(0, 255)
        if r == False:
            r = True
        if p == False:
            p = True
        if s == False:
            s = True

    computer_options = options[randint(0, 2)]

    # Making the game finish
    if player_score == 5:
        eee = False
        r = False
        p = False
        s = False
        pygame.draw.rect(screen, (0, 50, 0), pygame.Rect(0, 210, 800, 90))
        draw_text("You Defeated the Computer!", font, (0, 255, 0), 10, 210)

    if computer_score == 5:
        eee = False
        r = False
        p = False
        s = False
        pygame.draw.rect(screen, (50, 0, 0), pygame.Rect(0, 210, 800, 90))
        draw_text("The Computer Defeated You!", font, (255, 0, 0), 10, 210)

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update display window on every frame
    pygame.display.update()

pygame.quit()
