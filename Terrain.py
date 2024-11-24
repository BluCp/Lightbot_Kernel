class Terrain:
    """Builds a terrain for the lightbot game"""
    def __init__(self, n: int=10, m: int=10):
        self.__n = n
        self.__m = m

    def build_terrain(self) -> list:
        """Creates a nxm matrix for terrain""" 
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
    

    
    
