# test command : uv run main.py
import pygame
from player import Player
from constants import *
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # delta time for fps
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    running = True
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 60 fps
        dt = clock.tick(60) / 1000
        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
if __name__ == "__main__":
    main()
