## Imports
import pygame
import sys

"""
    This is a simple platform class for respresenting a platform 
    in the video
"""
class Platform(object):
    """! Class with all the implementation for the platform
    on the visualizer.

    This class contains all the platform properties and the
    methods to update the platform's visual
    """

    def __init__ (self, screen, length, width, color, x, y):
        """! The platform base class initializer

        @param screen   The parent screen base class for the platform.
        @param length   The length of the platform.
        @param color    The desired color for the platform: A touple (R, G, B)
                        values from 0 to 255
        @param x        The center position at X axis.
        @param y        The center position at Y axis.                        

        @return         An instance of a platform class initialized
        """

        ## The parent screen base class that it will be drawn
        self._screen = screen 

        ## The length of the platform
        self._length = length

        ## Platform width
        self._width = width

        ## X center position
        self._x = x

        ## Y center position
        self._y = y

        ## Actual color of the platform
        self._color = color

    def draw(self, camera_offset):
        # calculating top left (p) corner and platform side dimensions (l) 
        p = (self._x-self._length/2 - camera_offset[0], self._y-self._width/2 - camera_offset[1])
        l = (self._length, self._width)
        pygame.draw.rect(self._screen, self._color , pygame.Rect(p, l), border_radius = int(self._width/2))



"""
    script for quick behavioral and visual testing of the platform.
    draws a platform in the center, with the mouse pointer representing the camera movement.
"""
if __name__ == "__main__":    
    # Initializing Pygame
    pygame.init()
    
    # Initializing surface
    screen = pygame.display.set_mode((1000,1000))

    # Initializing platform (in the center of the screen)
    x = pygame.display.Info().current_w//2
    y = pygame.display.Info().current_w//2
    plat = Platform(screen, 100, 20, (0, 0, 0), x, y)

    # Initializing camera
    cam = (0,0) 

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255, 255, 255))  
        
        # Update camera value 
        cam = pygame.mouse.get_pos()[0]-x, pygame.mouse.get_pos()[1]-y
        print(cam)
        plat.draw(cam)
        
        pygame.display.flip()