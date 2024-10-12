import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
FONT = pygame.font.SysFont(None, 48)
INPUT_FONT = pygame.font.SysFont(None, 36)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main():
    # Game variables
    number_to_guess = random.randint(1, 100)
    attempts = 0
    input_text = ''
    input_box = pygame.Rect(200, 150, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        try:
                            guess = int(input_text)
                            attempts += 1
                            if guess < number_to_guess:
                                result_text = "Too low!"
                            elif guess > number_to_guess:
                                result_text = "Too high!"
                            else:
                                result_text = f"Correct! You guessed the number in {attempts} attempts."
                        except ValueError:
                            result_text = "Invalid input. Enter a number between 1 and 100."
                        input_text = ''
                        number_to_guess = random.randint(1, 100)
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                    color = color_active if active else color_inactive
                else:
                    active = False
                    color = color_inactive

        WIN.fill(WHITE)
        draw_text("Guess the Number (1-100):", FONT, BLACK, WIN, WIDTH // 2, HEIGHT // 4)
        txt_surface = INPUT_FONT.render(input_text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        WIN.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(WIN, color, input_box, 2)
        draw_text(result_text if 'result_text' in locals() else '', FONT, BLACK, WIN, WIDTH // 2, HEIGHT // 2 + 50)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
