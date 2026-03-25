import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    fps_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
             if asteroid.collides_with(player):
                  log_event("player_hit")
                  print("Game over!")
                  sys.exit()
        for asteroid in asteroids:
             for shot in shots:
                  if shot.collides_with(asteroid):
                       log_event("asteroid_shot")
                       shot.kill()
                       asteroid.split()                                   
        screen.fill("black")
        for items in drawable:
                items.draw(screen)    
        pygame.display.flip()
        dt = fps_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
        
            

