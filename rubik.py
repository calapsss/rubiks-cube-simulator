#!/usr/bin/env python
# Author: Charles Calapini
# Documentation: No help needed. Own work.
# AutoPEP8 for automating PEP COmpliance
class Cube:

    '''A class to represent a Rubik's Cube'''

    def __init__(self, arg1=None):
        '''Initialize the cube'''
        cfg = "WWWWWWWWW GGGGGGGGG RRRRRRRRR BBBBBBBBB OOOOOOOOO YYYYYYYYY"
        if arg1 is not None:
            cfg = arg1
            if (len(cfg.split(" ")) != 6):
                self.cube_config_one_string(cfg)
            else:
                self.cube_config_split(cfg)
        else:
            self.cube_config_split(cfg)

        pass

    def cube_config_split(self, configuration):
        '''Initialize the cube'''
        configs = configuration.split()

        self.cube = {'U': [[configs[0][0], configs[0][1], configs[0][2]],
                           [configs[0][3], configs[0][4], configs[0][5]],
                           [configs[0][6], configs[0][7], configs[0][8]]],
                     'L': [[configs[1][0], configs[1][1], configs[1][2]],
                           [configs[1][3], configs[1][4], configs[1][5]],
                           [configs[1][6], configs[1][7], configs[1][8]]],
                     'F': [[configs[2][0], configs[2][1], configs[2][2]],
                           [configs[2][3], configs[2][4], configs[2][5]],
                           [configs[2][6], configs[2][7], configs[2][8]]],
                     'R': [[configs[3][0], configs[3][1], configs[3][2]],
                           [configs[3][3], configs[3][4], configs[3][5]],
                           [configs[3][6], configs[3][7], configs[3][8]]],
                     'B': [[configs[4][0], configs[4][1], configs[4][2]],
                           [configs[4][3], configs[4][4], configs[4][5]],
                           [configs[4][6], configs[4][7], configs[4][8]]],
                     'D': [[configs[5][0], configs[5][1], configs[5][2]],
                           [configs[5][3], configs[5][4], configs[5][5]],
                           [configs[5][6], configs[5][7], configs[5][8]]]}

    def cube_config_one_string(self, cfg):
        '''Initialize the cube'''
        self.cube = {'U': [[cfg[0], cfg[1], cfg[2]],
                           [cfg[3], cfg[4], cfg[5]],
                           [cfg[6], cfg[7], cfg[8]]],
                     'L': [[cfg[9], cfg[10], cfg[11]],
                           [cfg[12], cfg[13], cfg[14]],
                           [cfg[15], cfg[16], cfg[17]]],
                     'F': [[cfg[18], cfg[19], cfg[20]],
                           [cfg[21], cfg[22], cfg[23]],
                           [cfg[24], cfg[25], cfg[26]]],
                     'R': [[cfg[27], cfg[28], cfg[29]],
                           [cfg[30], cfg[31], cfg[32]],
                           [cfg[33], cfg[34], cfg[35]]],
                     'B': [[cfg[36], cfg[37], cfg[38]],
                           [cfg[39], cfg[40], cfg[41]],
                           [cfg[42], cfg[43], cfg[44]]],
                     'D': [[cfg[45], cfg[46], cfg[47]],
                           [cfg[48], cfg[49], cfg[50]],
                           [cfg[51], cfg[52], cfg[53]]]}

    def __str__(self):
        '''Return a string representation of the cube'''
        str_cube = ""
        for i in range(3):
            for j in range(3):
                str_cube += self.cube['U'][i][j]

        str_cube += " "
        for i in range(3):
            for j in range(3):
                str_cube += self.cube['L'][i][j]

        str_cube += " "
        for i in range(3):
            for j in range(3):
                str_cube += self.cube['F'][i][j]

        str_cube += " "
        for i in range(3):
            for j in range(3):
                str_cube += self.cube['R'][i][j]

        str_cube += " "
        for i in range(3):
            for j in range(3):
                str_cube += self.cube['B'][i][j]

        str_cube += " "
        for i in range(3):
            for j in range(3):
                str_cube += self.cube['D'][i][j]

        return str_cube

    def get_color_at(self, face, row, col):
        '''Return the color at the specified face, row, and column'''
        if (face != 'U' and face != 'L' and face !=
                'F' and face != 'R' and face != 'B' and face != 'D'):
            raise ValueError("Invalid face")

        # Raises indexerror when not in range below 1 or above 3
        if (row < 1 or row > 3):
            raise IndexError("Invalid row")

        if (col < 1 or col > 3):
            raise IndexError("Invalid col")

        return self.cube[face][row - 1][col - 1]

    def print_cube(self):
        '''Print the cube in a more readable format'''
        print()
        for i in range(3):
            print(
                "- - -    " +
                self.cube['U'][i][0],
                self.cube['U'][i][1],
                self.cube['U'][i][2] +
                "    - - - " +
                "   - - - ")

        print()
        for i in range(3):
            print(
                self.cube['L'][i][0],
                self.cube['L'][i][1],
                self.cube['L'][i][2],
                "  ",
                self.cube['F'][i][0],
                self.cube['F'][i][1],
                self.cube['F'][i][2],
                "  ",
                self.cube['R'][i][0],
                self.cube['R'][i][1],
                self.cube['R'][i][2],
                "  ",
                self.cube['B'][i][0],
                self.cube['B'][i][1],
                self.cube['B'][i][2],
                end="\n")

        print()
        for i in range(3):
            print(
                "- - -    " +
                self.cube['D'][i][0],
                self.cube['D'][i][1],
                self.cube['D'][i][2] +
                "    - - - " +
                "   - - - ")

        print()

    def move(self, face, clockwise):
        '''Invokes appropriate method for the specified face'''
        if (clockwise):
            if face == 'U':
                self._move_up()
            elif face == 'L':
                self._move_left()
            elif face == 'F':
                self._move_front()
            elif face == 'R':
                self._move_right()
            elif face == 'B':
                self._move_back()
            elif face == 'D':
                self._move_down()
        else:
            if face == 'U':
                self._move_up()
                self._move_up()
                self._move_up()
            elif face == 'L':
                self._move_left()
                self._move_left()
                self._move_left()
            elif face == 'F':
                self._move_front()
                self._move_front()
                self._move_front()
            elif face == 'R':
                self._move_right()
                self._move_right()
                self._move_right()
            elif face == 'B':
                self._move_back()
                self._move_back()
                self._move_back()
            elif face == 'D':
                self._move_down()
                self._move_down()
                self._move_down()

    def _move_back(self):
        '''Moves the back face clockwise'''

        # Move the back face
        temp = self.cube['B'][0][0]
        self.cube['B'][0][0] = self.cube['B'][2][0]
        self.cube['B'][2][0] = self.cube['B'][2][2]
        self.cube['B'][2][2] = self.cube['B'][0][2]
        self.cube['B'][0][2] = temp
        temp = self.cube['B'][0][1]
        self.cube['B'][0][1] = self.cube['B'][1][0]
        self.cube['B'][1][0] = self.cube['B'][2][1]
        self.cube['B'][2][1] = self.cube['B'][1][2]
        self.cube['B'][1][2] = temp
        # Move the other faces
        temp = self.cube['U'][0][2] + \
            self.cube['U'][0][1] + self.cube['U'][0][0]
        self.cube['U'][0][2] = self.cube['R'][2][2]
        self.cube['U'][0][1] = self.cube['R'][1][2]
        self.cube['U'][0][0] = self.cube['R'][0][2]
        self.cube['R'][0][2] = self.cube['D'][2][2]
        self.cube['R'][1][2] = self.cube['D'][2][1]
        self.cube['R'][2][2] = self.cube['D'][2][0]
        self.cube['D'][2][0] = self.cube['L'][0][0]
        self.cube['D'][2][1] = self.cube['L'][1][0]
        self.cube['D'][2][2] = self.cube['L'][2][0]
        self.cube['L'][0][0] = temp[0]
        self.cube['L'][1][0] = temp[1]
        self.cube['L'][2][0] = temp[2]
        pass

    def _move_down(self):
        '''Moves the down face clockwise'''

        # Move the down face
        temp = self.cube['D'][0][0]
        self.cube['D'][0][0] = self.cube['D'][2][0]
        self.cube['D'][2][0] = self.cube['D'][2][2]
        self.cube['D'][2][2] = self.cube['D'][0][2]
        self.cube['D'][0][2] = temp
        temp = self.cube['D'][0][1]
        self.cube['D'][0][1] = self.cube['D'][1][0]
        self.cube['D'][1][0] = self.cube['D'][2][1]
        self.cube['D'][2][1] = self.cube['D'][1][2]
        self.cube['D'][1][2] = temp
        # Move the other faces
        temp = self.cube['L'][2]
        self.cube['L'][2] = self.cube['B'][2]
        self.cube['B'][2] = self.cube['R'][2]
        self.cube['R'][2] = self.cube['F'][2]
        self.cube['F'][2] = temp
        pass

    def _move_front(self):
        '''Moves the front face clockwise'''

        # Move the front face
        temp = self.cube['F'][0][0]
        self.cube['F'][0][0] = self.cube['F'][2][0]
        self.cube['F'][2][0] = self.cube['F'][2][2]
        self.cube['F'][2][2] = self.cube['F'][0][2]
        self.cube['F'][0][2] = temp
        temp = self.cube['F'][0][1]
        self.cube['F'][0][1] = self.cube['F'][1][0]
        self.cube['F'][1][0] = self.cube['F'][2][1]
        self.cube['F'][2][1] = self.cube['F'][1][2]
        self.cube['F'][1][2] = temp
        # Move the other faces
        temp = self.cube['U'][2][0] + \
            self.cube['U'][2][1] + self.cube['U'][2][2]
        self.cube['U'][2][0] = self.cube['L'][2][2]
        self.cube['U'][2][1] = self.cube['L'][1][2]
        self.cube['U'][2][2] = self.cube['L'][0][2]
        self.cube['L'][0][2] = self.cube['D'][0][0]
        self.cube['L'][1][2] = self.cube['D'][0][1]
        self.cube['L'][2][2] = self.cube['D'][0][2]
        self.cube['D'][0][2] = self.cube['R'][0][0]
        self.cube['D'][0][1] = self.cube['R'][1][0]
        self.cube['D'][0][0] = self.cube['R'][2][0]
        self.cube['R'][0][0] = temp[0]
        self.cube['R'][1][0] = temp[1]
        self.cube['R'][2][0] = temp[2]

        pass

    def _move_left(self):
        '''Moves the left face clockwise'''

        # Move the left face
        temp = self.cube['L'][0][0]
        self.cube['L'][0][0] = self.cube['L'][2][0]
        self.cube['L'][2][0] = self.cube['L'][2][2]
        self.cube['L'][2][2] = self.cube['L'][0][2]
        self.cube['L'][0][2] = temp
        temp = self.cube['L'][0][1]
        self.cube['L'][0][1] = self.cube['L'][1][0]
        self.cube['L'][1][0] = self.cube['L'][2][1]
        self.cube['L'][2][1] = self.cube['L'][1][2]
        self.cube['L'][1][2] = temp
        # Move the other faces
        temp = self.cube['U'][0][0] + \
            self.cube['U'][1][0] + self.cube['U'][2][0]
        self.cube['U'][0][0] = self.cube['B'][2][2]
        self.cube['U'][1][0] = self.cube['B'][1][2]
        self.cube['U'][2][0] = self.cube['B'][0][2]
        self.cube['B'][0][2] = self.cube['D'][2][0]
        self.cube['B'][1][2] = self.cube['D'][1][0]
        self.cube['B'][2][2] = self.cube['D'][0][0]
        self.cube['D'][2][0] = self.cube['F'][2][0]
        self.cube['D'][1][0] = self.cube['F'][1][0]
        self.cube['D'][0][0] = self.cube['F'][0][0]
        self.cube['F'][0][0] = temp[0]
        self.cube['F'][1][0] = temp[1]
        self.cube['F'][2][0] = temp[2]

        pass

    def _move_right(self):
        '''Moves the right face clockwise'''

        # Move the right face
        temp = self.cube['R'][0][0]
        self.cube['R'][0][0] = self.cube['R'][2][0]
        self.cube['R'][2][0] = self.cube['R'][2][2]
        self.cube['R'][2][2] = self.cube['R'][0][2]
        self.cube['R'][0][2] = temp
        temp = self.cube['R'][0][1]
        self.cube['R'][0][1] = self.cube['R'][1][0]
        self.cube['R'][1][0] = self.cube['R'][2][1]
        self.cube['R'][2][1] = self.cube['R'][1][2]
        self.cube['R'][1][2] = temp
        # Move the other faces
        temp = self.cube['U'][0][2] + \
            self.cube['U'][1][2] + self.cube['U'][2][2]
        self.cube['U'][0][2] = self.cube['F'][0][2]
        self.cube['U'][1][2] = self.cube['F'][1][2]
        self.cube['U'][2][2] = self.cube['F'][2][2]
        self.cube['F'][0][2] = self.cube['D'][0][2]
        self.cube['F'][1][2] = self.cube['D'][1][2]
        self.cube['F'][2][2] = self.cube['D'][2][2]
        self.cube['D'][2][2] = self.cube['B'][0][0]
        self.cube['D'][1][2] = self.cube['B'][1][0]
        self.cube['D'][0][2] = self.cube['B'][2][0]
        self.cube['B'][0][0] = temp[2]
        self.cube['B'][1][0] = temp[1]
        self.cube['B'][2][0] = temp[0]

        pass

    def _move_up(self):
        '''Moves the up face clockwise'''

        # Move the up face
        temp = self.cube['U'][0][0]
        self.cube['U'][0][0] = self.cube['U'][2][0]
        self.cube['U'][2][0] = self.cube['U'][2][2]
        self.cube['U'][2][2] = self.cube['U'][0][2]
        self.cube['U'][0][2] = temp
        temp = self.cube['U'][0][1]
        self.cube['U'][0][1] = self.cube['U'][1][0]
        self.cube['U'][1][0] = self.cube['U'][2][1]
        self.cube['U'][2][1] = self.cube['U'][1][2]
        self.cube['U'][1][2] = temp
        # Move the other faces
        temp = self.cube['F'][0]
        self.cube['F'][0] = self.cube['R'][0]
        self.cube['R'][0] = self.cube['B'][0]
        self.cube['B'][0] = self.cube['L'][0]
        self.cube['L'][0] = temp

        pass


def main(args):
    '''Main function'''

    filename = args[1]
    # open file in folder puzzles
    f = open(filename, 'r')
    config = f.readline()
    move_set = f.read()
    move_set = move_set.split()
    moves = []
    for move in move_set:
        if len(move) > 1:
            moves.append((move[0], False))
        else:
            moves.append((move[0], True))

    cube = Cube(config)
    cube.print_cube()

    for move in moves:
        print("Current move: ", move, "Clockwise: ", move[1])
        cube.move(move[0], clockwise=move[1])
        cube.print_cube()

    pass


if '__main__' == __name__:
    import sys
    main(sys.argv)