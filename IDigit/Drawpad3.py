import pygame

class DrawPad():
    def __init__(self, size, color):
        self.pad = pygame.display.set_mode(size)
        self.pad.fill((255,255,255))
        pygame.display.update()
	    
	def draw(self, thickness):
	    drawing = False
	    last_post = (0, 0)
	    while 1:
	        event = pygame.event.wait()
	        if (event == pygame.QUIT):
	            pygame.quit()
	        if (event == pygame.MOUSEBUTTONDOWN):
	        	pygame.draw.circle(screen, "black", event.pos, thickness)
	        	drawing = True
	        if (event == pygame.MOUSEBUTTONDOWN):
	        	drawing = False
	        if (event == pygame.MOUSEMOTION):
	        	if (drawing):
	        		pygame.draw.circle(screen, "black", event.pos, thickness)
	        		line(screen, last_pos, event.pos, thickness)
	        	last_post = event.pos

	def line(screen, start, end, thickness):
		dx = start[0] - end[0]
		dy = start[1] - end[1]
		longest = max(abs(dx), abs(dy))
		for i in range (0, longest):
			x = int(start[0] + i / longest * dx)
			y = int(start[1] + i / longest * dy)
			pygame.draw.circle(screen, "black", (x, y), thickness)
