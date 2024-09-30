
import random
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, millis=1)
nyan_surface = pygame.image.load('images/Anime.gif').convert_alpha()





class ParticlePrinciple:
    def __init__(self):
        self.particles = []
        self.size = 8


    def emit(self):
        if self.particles:
            self.delete_particles()
        # for particle in self.particles:
        #     particle[0][1] += particle[2][0]
        #     particle[0][0] += particle[2][1]
        #     particle[1] -= 0.2
        #     pygame.draw.circle(screen, pygame.Color('White'), particle[0], int(particle[1]))
        for particle in self.particles:
            particle[0].x -= 2
            pygame.draw.rect(screen, particle[1], particle[0])
            pygame.draw.rect(screen, particle[1], particle[0])
        self.draw_nyancat()





    def add_particles(self,offset, color):
        # pos_x = pygame.mouse.get_pos()[0]
        # pos_y = pygame.mouse.get_pos()[1]
        # radius = 10
        # direction_x = random.randint(-3, 3)
        # direction_y = random.randint(-3, 3)
        # particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        # self.particles.append(particle_circle)
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1] + offset
        particle_rect = pygame.Rect(pos_x - self.size / 2, pos_y - self.size / 2,self.size, self.size)
        self.particles.append((particle_rect, color))




    def delete_particles(self):
        # particles_copy = [particle for particle in self.particles if particle[1] > 0]
        # self.particles = particles_copy
        particles_copy = [particle for particle in self.particles if particle[0].x > 0]
        self.particles = particles_copy
    def draw_nyancat(self):
        nyan_rect = nyan_surface.get_rect(center=pygame.mouse.get_pos())
        screen.blit(nyan_surface, nyan_rect)





particle2 = ParticlePrinciple()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLE_EVENT:
            particle2.add_particles(-30, pygame.Color('Red'))
            particle2.add_particles(-12, pygame.Color('Orange'))
            particle2.add_particles(-6, pygame.Color('Yellow'))
            particle2.add_particles(6, pygame.Color('Green'))
            particle2.add_particles(10, pygame.Color('Blue'))
            particle2.add_particles(30, pygame.Color('Purple'))





    screen.fill((30, 30, 30))
    particle2.emit()
    pygame.display.update()
    clock.tick(120)
