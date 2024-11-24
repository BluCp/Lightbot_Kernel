from vpython import *


class Terrain:
    """Builds a terrain for the lightbot game"""
    def __init__(self, n: int=10, m: int=10):
        self.__n = n
        self.__m = m

    def build_terrain(self) -> list:
        """Creates a nxm matrix for terrain""" 
        # TODO make it like a matrix which contains the value of blue boxes ???
        matrix = list()
        for _ in range(self.__m):
            row = list()
            for _ in range(self.__n):
                row.append(0)
            matrix.append(row)
        return matrix
    # For now it is default (flat) TODO
    def build_height(self) -> list:
        """Creates a nxm matrix for height values """
        matrix = list()
        for _ in range(self.__m):
            row = list()
            for _ in range(self.__n):
                row.append(0)
            matrix.append(row)
        return matrix
    
    def display_terrain(self):
        """Display the terrain of nxm matrix"""
        # List of blue boxes
        """
        isBlue = [
                [True, False, True, False, True, False, True, False, True, False],
                [False, True, False, True, False, True, False, True, False, True],
                [True, False, True, False, True, False, True, False, True, False],
                [False, True, False, True, False, True, False, True, False, True],
                [True, False, True, False, True, False, True, False, True, False],
                [False, True, False, True, False, True, False, True, False, True],
                [True, False, True, False, True, False, True, False, True, False],
                [False, True, False, True, False, True, False, True, False, True],
                [True, False, True, False, True, False, True, False, True, False],
                [False, True, False, True, False, True, False, True, False, True]
                ]
        """

        cubes = []
        # Create a box containing coordinates i and j 
        for i in range(self.__m):
             for j in range(self.__n):
                cube = box()
                cubes.append(cube)
                # Change the position of the box
                cube.pos = vector(j, self.build_height()[i][j], i)
                # Color the box
                isBlue = [[(i + j) % 2 == 0 for j in range(self.__m)] for i in range(self.__n)]
                # Change the color of the box 
                cube.color = color.blue if isBlue[i][j] else color.green

    def see_size(self):
        """Gives the current size of the terrain"""
        return f"Terrain is {self.__n} x {self.__m}"

    def set_size(self):
        """Sets the size of the terrain"""
        if input("Do you want to change the size of the terrain. Default is 10x10 [y/n]: ").lower() == "y":
            self.__n = int(input("Please enter the column size of the terrain: "))
            self.__m = int(input("Please enter the row size of the terrain: "))
        else:
            print("As you wish")
    

    
    
