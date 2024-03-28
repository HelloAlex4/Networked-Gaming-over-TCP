import socket
import threading
import pygame
import time
import random

def handle_client(conn, addr):
    global change_to

    while True:
        data = conn.recv(1024)
        if not data or data.decode().strip() == 'quit':
            break
        print(data.decode())
        change_to = data.decode()
    conn.close()

def start_server(host='0.0.0.0', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        while True:
            conn, addr = s.accept()
            # Start a new thread for each client
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()



def snakeGame():
    global red
    global direction
    global change_to
    global food_pos
    global food_spawn
    global snake_pos
    global snake_body
    global score

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # Making sure the snake cannot move in the opposite direction instantaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        
        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10
        
        # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 10
            food_spawn = False
        else:
            snake_body.pop()
            
        if not food_spawn:
            food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        food_spawn = True
        
        # GFX
        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        
        # Game Over conditions
        if snake_pos[0] < 0 or snake_pos[0] > width-10:
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > height-10:
            game_over()
        
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()
        
        pygame.display.update()
        fps_controller.tick(25)

pygame.init()

# Window size
width, height = 600, 400
game_window = pygame.display.set_mode((width, height))

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# FPS controller
fps_controller = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

# Game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()




if __name__ == '__main__':
    # Start the server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    
    snakeGame()
