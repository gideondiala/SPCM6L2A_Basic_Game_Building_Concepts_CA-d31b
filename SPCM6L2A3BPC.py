# 1) Import the `pygame` library to create a window, handle keyboard input, and draw shapes.

# 2) Define a function `main()` to contain the full game logic.

# 3) Inside `main()`:
#    a) Initialize pygame using `pygame.init()`.
#    b) Set screen dimensions (`screen_width`, `screen_height`) to 500x500.
#    c) Create the game window using `pygame.display.set_mode(...)`.
#    d) Set the window title using `pygame.display.set_caption(...)`.

# 4) Create a dictionary `colors` to map color names to RGB values using `pygame.Color(...)`.

# 5) Set the initial sprite color to white using:
#    `current_color = colors['white']`.

# 6) Set the starting position of the sprite:
#    a) `x, y = 30, 30`

# 7) Set the sprite size:
#    a) `sprite_width, sprite_height = 60, 60`

# 8) Create a clock object using `pygame.time.Clock()` to control the frame rate.

# 9) Create a loop control variable `done = False`.

# 10) Start the main game loop `while not done`:
#     a) Handle events using `pygame.event.get()`.
#     b) If the event is `pygame.QUIT`, set `done = True` to exit the loop.

# 11) Read keyboard inputs using `pygame.key.get_pressed()`:
#     a) If LEFT key is pressed, move sprite left by decreasing `x`.
#     b) If RIGHT key is pressed, move sprite right by increasing `x`.
#     c) If UP key is pressed, move sprite up by decreasing `y`.
#     d) If DOWN key is pressed, move sprite down by increasing `y`.

# 12) Restrict the sprite to stay inside the screen boundaries:
#     a) Clamp `x` between 0 and `screen_width - sprite_width`.
#     b) Clamp `y` between 0 and `screen_height - sprite_height`.

# 13) Change the sprite color based on which boundary it touches:
#     a) If `x == 0`, change to blue (left wall).
#     b) Else if `x == screen_width - sprite_width`, change to yellow (right wall).
#     c) Else if `y == 0`, change to red (top wall).
#     d) Else if `y == screen_height - sprite_height`, change to green (bottom wall).
#     e) Otherwise, keep it white (not touching any boundary).

# 14) Draw everything on the screen:
#     a) Fill the background with black using `screen.fill((0, 0, 0))`.
#     b) Draw the sprite as a rectangle using `pygame.draw.rect(...)`.

# 15) Update the display using `pygame.display.flip()`.

# 16) Limit the frame rate using `clock.tick(90)`.

# 17) After the loop ends, close pygame using `pygame.quit()`.

# 18) Use `if __name__ == "__main__":` to call `main()` only when
#     the file is run directly.