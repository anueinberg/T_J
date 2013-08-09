
### different key press functions

def start_keypress():
    pressed = False
    while not pressed:
        for event in pygame.event.get():
            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_SPACE:
                    pressed = True
                elif event.key == pygame.locals.K_ESCAPE:
		    write_data()
		    exit_exp()


def visual_angle(inches, angle, distance):
	cents = 2.54 * inches
	pix_diag = sqrt(screen.size[0]**2 + screen.size[1]**2)
	ppi = pix_diag / cents
	size_cm = math.tan(math.radians(angle)/2)*2*distance
	size_pix = ceil(ppi*size_cm)
	return size_pix



