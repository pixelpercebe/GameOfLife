# Example file showing a basic pygame "game loop"
import pygame
import functions


# Función para mostrar texto en pantalla
def show_text(text, x, y, color):
	# Render text
	rendered_text = font.render(text, True, color)  # Antialiasing activado, color blanco
	# Dibujar el texto en la posición (x, y)
	screen.blit(rendered_text, (x, y))


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
	screen.fill("blue")
	init_population = []
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			draw_pix_x = row * x_size
			draw_pix_y = col * y_size
			if matrix[row][col] == 1:
				init_population.append((row, col))
				pygame.draw.rect(screen, "green", (draw_pix_y, draw_pix_x, x_size, y_size))
	return init_population


def analyse(population):
	count_matrix = functions.analyse_neighbours(matrix, population)
	new_matrix = functions.verify_terrain(count_matrix)
	return new_matrix


def clean_screen(current_matrix):
	functions.clean_matrix(current_matrix)
	draw_population()


# pygame setup
pygame.init()

start = 0
dimensions = (1280, 720)  # 1280,720
x_size = 5
y_size = 5

screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()
running = True

font = pygame.font.Font(None, 36)  # Usa la fuente predeterminada, tamaño 36
screen.fill("blue")
matrix = functions.create_grid(dimensions, x_size, y_size)
rand_pop = functions.generate_random_terrain(matrix)
functions.load_init_matrix(matrix, rand_pop)

while running:
	# poll for events
	# pygame.QUIT event means the user clicked X to close your window
	pop = draw_population()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			if matrix[mouse_pos[1] // x_size][mouse_pos[0] // y_size] == 0:
				matrix[mouse_pos[1] // x_size][mouse_pos[0] // y_size] = 1
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
	else:
		show_text("Pause", 1, 30, 'red')
	show_text("Space = start", 1, 1, 'white')


	# RENDER YOUR GAME HERE
	# flip() the display to put your work on screen
	pygame.display.flip()
	clock.tick(60)  # limits FPS to 60
pygame.quit()
