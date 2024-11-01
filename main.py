# Example file showing a basic pygame "game loop"
import pygame
import functions


def draw_grid():
    aux_x_size = x_size
    aux_y_size = y_size
    for row in range(len(matrix)):
        pygame.draw.line(screen, "white", (0, aux_x_size), (dimensions[0], aux_x_size), 1)
        aux_x_size = aux_x_size + x_size
        for col in range(len(matrix[0])):
            pygame.draw.line(screen, "white", (aux_y_size, 0), (aux_y_size, dimensions[1]), 1)
            aux_y_size = aux_y_size + x_size


def draw_population():
    init_population = []
    screen.fill("black")
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            draw_pix_x = row * x_size
            draw_pix_y = col * y_size
            if matrix[row][col] == 1:
                init_population.append((row, col))
                pygame.draw.rect(screen, "white", (draw_pix_y, draw_pix_x, x_size, y_size))
    return init_population


def analyse(population):
    count_matrix = functions.analyse_neighbours(matrix, population)
    new_matrix = functions.verify_alive(matrix, count_matrix)
    return new_matrix


def clean_screen(current_matrix):
    functions.clean_matrix(current_matrix)
    draw_population()


# pygame setup
pygame.init()
start = 0
dimensions = (1280, 720)  # 1280,720
x_size = 10
y_size = 10

screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()
running = True

screen.fill("black")

matrix = functions.create_grid(dimensions, x_size, y_size)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    pop = draw_population()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if matrix[mouse_pos[1]//x_size][mouse_pos[0]//y_size] == 0:
                matrix[mouse_pos[1]//x_size][mouse_pos[0]//y_size] = 1
            else:
                matrix[mouse_pos[1] // x_size][mouse_pos[0] // y_size] = 0
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_SPACE:
                    start = 1 if start == 0 else 0
                    print(start)
                case pygame.K_w:
                    start = 0
                    matrix = analyse(pop)
                    print("next iteration")
                case pygame.K_ESCAPE:
                    start = 0
                    clean_screen(matrix)
    if start:
        matrix = analyse(pop)

    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(10)  # limits FPS to 60
pygame.quit()
