## Imports
import pygame

"""
    This is a simple Ball class for respresenting a ball 
    in the video
"""
class Ball(object):
    """! Class with all the implementation for the ball
    on the visualizer.

    This class contains all the ball properties and the
    methods to update the ball's visual
    """

    def __init__ (self, screen, radius, color, x, y, gravity):
        """! The ball base class initializer

        @param screen   The parent screen base class for the ball.
        @param radius   The radius of the ball.
        @param color    The desired color for the ball: A touple (R, G, B)
                        values from 0 to 255
        @param x        The initial position at X axis.
        @param y        The initial position at Y axis.
        @paream gravity The gravity that will be applied to the ball
                        

        @return         An instance of a ball class initialized
        """

        ## The parent screen base class where it will be drawn
        self._screen = screen 

        ## The radius of the ball
        self._radius = radius

        ## Actual X position
        self._xLoc = x

        ## Actual Y position
        self._yLoc = y

        ## Actual speed at X axis
        self._xVel = 0

        ## Actual speed at Y axis
        self._yVel = 0

        ## Gravity applied to the ball
        self.gravity = gravity

        ## Actual color of the ball
        self._color = color


    def draw(self, camera_offset):
        """! Function responsible to draw the ball at the screen.

        @param camera_offset    A touple containing the actual position of the camera. 
            
        @return none
        """
        pygame.draw.circle(self._screen, self._color , (self._xLoc - camera_offset[0],self._yLoc - camera_offset[1]), self._radius)


    def update(self, xCollision, yCollision, dT):
        """! Function responsible to update the ball dinamics.

        @param xCollision   Boolean flag with the collision status of the ball at X axis.
        @param yCollision   Boolean flag with the collision status of the ball at Y axis.
        @param dT           Time variable used to calculate the ball update in miliseconds.            
        
        @return none
        """
        dT /= 1000

        self._xLoc += self._xVel * dT

        self._yLoc = self._yLoc + self._yVel * dT + (self.gravity * dT * dT)/2

        self._yVel += self.gravity * dT 

        ## Bouncing interation. The ball looses 10% of the energy
        if  xCollision:
            self._xVel *= -0.9
        if  yCollision:
            self._yVel *= -0.9


    def setPosition(self, x=None, y=None):
        """! Function used to set the desired position for the ball.

        @param x    X axis position. Default: No upadte
        @param y    Y axis position. Default: No upadte

        @return none
        """

        if x != None: self._xLoc = x

        if y != None: self._yLoc = y

    def getPosition(self):
        """! Funtion used to get the actual postion of the ball
        
        @return x, y    Actual Position of the ball
        """

        return self._xLoc, self._yLoc
    
    
    def setSpeed(self, xVel=None, yVel=None):
        """! Function used to set the desired speed for the ball.

        @param x    X axis speed. Default: No upadte
        @param y    Y axis speed. Default: No upadte

        @return none
        """

        if xVel != None: self._xVel = xVel

        if yVel != None: self._yVel = yVel


    def getSpeed(self):
        """! Funtion used to get the actual speed of the ball
        
        @return xVel, yVel    Actual Speed of the ball
        """

        return self._xVel, self._yVel
    


"""
    Script for quick behavioral and visual testing of the platform.
    Draws a ball in the center that falls over the screen.
"""
if __name__ == "__main__":    
    # Initializing Pygame
    pygame.init()

    # Initializing surface
    screen = pygame.display.set_mode((1000,1000))

    # Initializing platform (in the center of the screen)
    x = pygame.display.Info().current_w//2
    y = pygame.display.Info().current_h//2
    ball = Ball(screen, 15, (0, 0, 0), x, y, 1000)

    # Initializing camera
    cam = (0,0) 

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    last_tick = pygame.time.get_ticks()

    # Loop until the user clicks the close button.
    done = False

    # Main program loop
    while not done:

        # Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Updating the object dynamics
        ball.update(False, False, pygame.time.get_ticks() - last_tick)
        last_tick = pygame.time.get_ticks()

        # Filling the screen
        screen.fill((255, 255, 255))  

        # Draw the ball on the screen
        ball.draw(cam)

        # Updating the screen
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

# Close the window and quit.
pygame.quit()