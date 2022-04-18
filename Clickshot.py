import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
screen.fill((255, 255, 255))
running = True


class Targets(pygame.sprite.Sprite):
    def __init__(self, width, height, colour, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)


Target_group = pygame.sprite.Group()
mouse_x = 0
mouse_y = 0

Target = Targets(50, 50, (0, 0, 255), random.randint(1, 1920), random.randint(1, 1080))
Target_group.add(Target)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            for target in Target_group:
                if target.rect.collidepoint(mouse_x, mouse_y):
                    target.kill()
                    screen.fill("white")
                    Target = Targets(50, 50, (0, 0, 255), random.randint(1, 1920), random.randint(1, 1080))
                    Target_group.add(Target)
                    Target_group.draw(screen)

    pygame.display.flip()
    Target_group.draw(screen)
