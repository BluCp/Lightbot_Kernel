from Bot import Bot
from Terrain import Terrain

class Lightbot():
    """Main class for the Lightbot game"""
    def __init__(self):
        # Creates a terrain class object, sets a new size, builds a terrain, creats a height map
        self.terrain = Terrain()
        self.terrain.set_size()
        self.terrain_map = self.terrain.build_terrain()
        self.height_map = self.terrain.build_height()
        # Creates a bot class object 
        self.bot = Bot(self.terrain_map, self.height_map)

    def run_game(self):
        """Main function of the game"""
        # Takes inputs for the lightbot game 
        self.cmd = input("Commands for lightbot: ")
        # Evaluates each command and runs it
        for i in self.cmd:
            if i == "^":
                self.bot.go()
            elif i == "<":
                self.bot.turn_left()
            elif i == ">":
                self.bot.turn_right()
            elif i == "*":
                self.bot.jump()
            else:
                self.bot.light()
        # Prints out the terrain map 
        for row in self.bot.output():
            print(row)

if __name__ == "__main__":
    game = Lightbot()
    game.run_game()
