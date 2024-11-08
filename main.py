import pygame
import player as p
import asteroid as ast
import asteroidfield as astfield
import shot
import constants as C


def main():
    print("Starting asteroids!")
    print(f"Screen width: {C.SCREEN_WIDTH}")
    print(f"Screen height: {C.SCREEN_HEIGHT}")

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    p.Player.containers = (updatable, drawable)
    ast.Asteroid.containers = (asteroids, updatable, drawable)
    astfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))
    player = p.Player(C.SCREEN_WIDTH / 2, C.SCREEN_HEIGHT / 2)
    asteroid_field = astfield.AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                return
            for bullet in shots:
                if asteroid.check_collision(bullet):
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
