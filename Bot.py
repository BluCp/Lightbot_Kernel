class Bot():
    """Creates a bot for the lightbot game"""
    def __init__(self, terrain_map, height_map, x=0, y=9, direction="E", height=0):
        self.__x = x
        self.__y = y
        self.__height = height
        self.__direction = direction
        self.__height_map = height_map
        self.__terrain_map = terrain_map

    def turn_left(self):
        """Turns left"""
        if self.__direction == "E":
            self.__direction = "N"
        elif self.__direction == "N":
            self.__direction = "W"
        elif self.__direction == "W":
            self.__direction = "S"
        elif self.__direction == "S":
            self.__direction = "E"
    
    def turn_right(self):
        """Turns right"""
        if self.__direction == "E":
            self.__direction = "S"
        elif self.__direction == "N":
            self.__direction = "E"
        elif self.__direction == "W":
            self.__direction = "N"
        elif self.__direction == "S":
            self.__direction = "W"
    
    def go(self):
        """Goes forward"""
        if self.__direction == "N":
            self.__y -= 1
            if self.__y < 0 or self.__y > 9:
                self.__y += 1
            elif self.__height != self.__height_map[self.__y][self.__x]:
                self.__y += 1
        elif self.__direction == "W":
            self.__x -= 1
            if self.__x < 0 or self.__x > 9:
                self.__x += 1
            elif self.__height != self.__height_map[self.__y][self.__x]:
                self.__x += 1
        elif self.__direction == "E":
            self.__x += 1
            if self.__x < 0 or self.__x > 9:
                self.__x -= 1
            elif self.__height != self.__height_map[self.__y][self.__x]:
                self.__x -= 1
        elif self.__direction == "S":
            self.__y += 1
            if self.__y < 0 or self.__y > 9:
                self.__y -= 1
            elif self.__height != self.__height_map[self.__y][self.__x]:
                self.__y -= 1
     
    def jump(self):
        """Jumps"""
        if self.__direction == "N":
            self.__y -= 1
            if self.__y < 0 or self.__y > 9:
                self.__y += 1
            elif abs(self.__height - self.__height_map[self.__y][self.__x]) != 1:
                self.__y += 1
        elif self.__direction == "W":
            self.__x -= 1
            if self.__x < 0 or self.__x > 9:
                self.__x += 1
            elif abs(self.__height - self.__height_map[self.__y][self.__x]) != 1:
                self.__x += 1
        elif self.__direction == "E":
            self.__x += 1
            if self.__x < 0 or self.__x > 9:
                self.__x -= 1
            elif abs(self.__height - self.__height_map[self.__y][self.__x]) != 1:
                self.__x -= 1
        elif self.__direction == "S":
            self.__y += 1
            if self.__y < 0 or self.__y > 9:
                self.__y -= 1
            elif abs(self.__height - self.__height_map[self.__y][self.__x]) != 1:
                self.__y -= 1
     
    def light(self):
        """Lights up the floor"""
        self.__terrain_map[self.__y][self.__x] = 1
    
    def output(self) -> list:
        """Returns the final map of terrain"""
        return self.__terrain_map