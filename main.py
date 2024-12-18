import pyxel
import random

class App:
    def __init__(self):
        
        
        # Initialize the Pyxel window (width, height)
        pyxel.init(160, 120)

        pyxel.load("my_resource.pyxres")
    

        # Set the initial position of the square
        self.x = 75
        self.y = 55
        self.score = 0

        # Set the initial position and velocity of the sprite    

        self.sprite_x = 80
        self.sprite_y = 60
        self.sprite_dx = 2
        self.sprite_dy = 2

        self.coke_x = 60
        self.coke_y = 40
        self.coke_dx = -2
        self.coke_dy = -2
    

        # Start the game loop
        pyxel.run(self.update, self.draw)

    def update(self):
        # Update the square's position based on arrow keys
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2

        # Simple interaction: Increase score when square reaches top-left corner

        # Update the sprite's position
        self.sprite_x += self.sprite_dx
        self.sprite_y += self.sprite_dy

        self.coke_x += self.coke_dx
        self.coke_y += self.coke_dy
        # Bounce the sprite off the edges of the screen
        if self.sprite_x <= 0 or self.sprite_x >= 160:
            self.sprite_dx *= -1
        if self.sprite_y <= 0 or self.sprite_y >= 120:
            self.sprite_dy *= -1

        if self.coke_x <= 0 or self.coke_x >= 160:
            self.coke_dx *= -1
        if self.coke_y <= 0 or self.coke_y >= 120:
            self.coke_dy *= -1

        if abs(self.x - self.sprite_x) <= 20 and abs(self.y - self.sprite_y) <= 20:
            self.score += 1


    def draw(self):
        # Clear the screen with black (color 0)
        pyxel.cls(4)

        # Draw a square (color 9)
        pyxel.load("my_resource.pyxres")
        pyxel.blt(self.x, self.y, 0, 0, 0, 10, 16, 0)

     

        pyxel.blt(self.sprite_x, self.sprite_y, 1, 0, 1, 20, 20, 0)
        


        # Draws a 16x16 sprite from bank 0
        if self.score % 100 == 0:
            self.sprite_x = random.randint(0, 160)
            self.sprite_y = random.randint(0, 120)
        
        if self.score >= 100:
            pyxel.blt(self.coke_x, self.coke_y, 2, 0, 0, 30, 30, 0)
            if abs(self.x - self.coke_x) <= 20 and abs(self.y - self.coke_y) <= 20:
                self.score -= 1
    

        # Draw the moving sprite (color 11)
        
       

        # Display the score
        pyxel.text(5, 5, f"Score: {self.score}", 7)

        # Display a message when score is high
        if self.score >= 100:
            pyxel.text(50, 50, "Bomb Incoming!", 7)

# Run the game
App()
