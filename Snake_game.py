#Modulos
import pygame, random, sys
from pygame import Vector2

#Classes:
class Fruit:
    def __init__(self):
        self.value_x = random.randint(0, cell_num -1)
        self.value_y = random.randint(0, cell_num - 1)
        self.position = Vector2(self.value_x, self.value_y)
    
    def draw_fruit(self):
        rect_fruit = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size)
        window.blit(img_fruta_size, rect_fruit)

    def change_fruit(self):
        self.value_x = random.randint(0, cell_num -1)
        self.value_y = random.randint(0, cell_num - 1)
        self.position = Vector2(self.value_x, self.value_y)


class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    
    def draw_snake(self):
        for block in self.body:
            value_snake_x = int(block.x * cell_size)
            value_snake_y = int(block.y * cell_size)
            rect_snake = pygame.Rect(value_snake_x, value_snake_y, cell_size, cell_size)
            window.blit(img_cobra_size, rect_snake)
    
    def move_snake(self):
        if self.new_block == False:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        else:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
    
    def add_block(self):
        self.new_block = True
        

class Main:
    def __init__(self):
        self.obj_snake = Snake()
        self.obj_fruit = Fruit()
    
    def game_update(self):
        self.obj_snake.move_snake()
        self.check_collision()
        self.check_game()
        
    def game_end(self):
        global running
        running = False
    
    def draw_elements(self):
        self.obj_snake.draw_snake()
        self.obj_fruit.draw_fruit()
        self.draw_scored()

    def draw_scored(self):
        text_scored = str(len(self.obj_snake.body) - 3)
        surface_scored = font_game.render(text_scored, True,(56, 74, 12))
        value_scored_x = int(cell_size * cell_num - 60)
        value_scored_y = int(cell_size * cell_num - 40)
        rect_scored = surface_scored.get_rect(center = (value_scored_x, value_scored_y))
        window.blit(surface_scored, rect_scored)
    

    def check_collision(self):
        if self.obj_fruit.position == self.obj_snake.body[0]:
            self.obj_fruit.change_fruit()
            self.obj_snake.add_block()
            music_scored.play()


    def check_game(self):
      if not 0 <= self.obj_snake.body[0].x < cell_num or not 0 <= self.obj_snake.body[0].y < cell_num:
        self.game_end()

      for body in self.obj_snake.body[1:]:
            if self.obj_snake.body[0] == body:
                self.game_end()


#game start:
pygame.init()


#Variables
running = True
cell_size = 40
cell_num = 20
#Create window
window = pygame.display.set_mode((cell_size * cell_num, cell_size * cell_num))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
font_game = pygame.font.Font(None, 32)
#Img, music 
img_fruta = pygame.image.load('apple_2.png').convert_alpha()
img_fruta_size = pygame.transform.scale(img_fruta,(cell_size, cell_size))
img_fruta = pygame.image.load('block_5.png').convert_alpha()
img_cobra_size = pygame.transform.scale(img_fruta,(cell_size, cell_size))

music_background = pygame.mixer.music.load('music.mp3')
music_scored = pygame.mixer.Sound('ponto.wav')


#Get event:
WINDOW_UPDATE = pygame.USEREVENT
pygame.time.set_timer(WINDOW_UPDATE, 150)

obj_main = Main()
pygame.mixer.music.play(-1)

#game loop:
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == WINDOW_UPDATE:
            obj_main.game_update()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    #Code:
            if event.key == pygame.K_UP:
                if obj_main.obj_snake.direction.y != 1:
                    obj_main.obj_snake.direction = Vector2(0, -1)

            if event.key == pygame.K_RIGHT:
                if obj_main.obj_snake.direction.x != 1:
                    obj_main.obj_snake.direction = Vector2(1, 0)

            if event.key == pygame.K_LEFT:
                if obj_main.obj_snake.direction.x != 1:
                    obj_main.obj_snake.direction = Vector2(-1, 0)

            if event.key == pygame.K_DOWN:
                if obj_main.obj_snake.direction.y != 1:
                    obj_main.obj_snake.direction = Vector2(0, 1)
        


    window.fill((248, 204, 166))
    obj_main.draw_elements()
    pygame.display.update()
    clock.tick(60)



#game end
pygame.quit()
sys.exit()
