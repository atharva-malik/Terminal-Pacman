import copy

blinky = ["Β", "β"]
pinky = ["Φ", "φ"]
inky = ["Ν", "ν"] # The greek letter Iota looked too much like the map which is why I had to use Nu
clyde = ["$", "€"] # Lore: Clyde is different from everyone else that's his symbol is special 
class Board:
    def __init__(self):
        self.map_size = (31, 28)
        self.pacman_map = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["|", "*", "*", "*", "*", "*", "*", "*", "*", "*", "|", "|", "*", "*", "*", "*", "|", "|", "*", "*", "*", "*", "*", "*", "*", "*", "*", "|"],
            ["|", "*", "|", "-", "-", "-", "-", "-", "|", "*", "|", "|", "*", "-", "-", "*", "|", "|", "*", "|", "-", "-", "-", "-", "-", "|", "*", "|"],
            ["|", "*", "|", "-", "-", "-", "-", "-", "|", "*", "-", "-", "*", "|", "|", "*", "-", "-", "*", "|", "-", "-", "-", "-", "-", "|", "*", "|"],
            ["|", "*", "*", "*", "|", "|", "*", "*", "*", "*", "*", "*", "*", "|", "|", "*", "*", "*", "*", "*", "*", "*", "|", "|", "*", "*", "*", "|"],
            ["-", "-", "-", "*", "|", "|", "*", "-", "-", "*", "|", "-", "-", "-", "-", "-", "-", "|", "*", "-", "-", "*", "|", "|", "*", "-", "-", "-"],
            [" ", " ", "|", "*", "|", "|", "*", "|", "|", "*", "|", "-", "-", "-", "-", "-", "-", "|", "*", "|", "|", "*", "|", "|", "*", "|", " ", " "],
            ["-", "-", "-", "*", "-", "-", "*", "|", "|", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "|", "|", "*", "-", "-", "*", "-", "-", "-"],
            ["*", "*", "*", "*", "*", "*", "*", "|", "|", "*", "|", "-", "-", "-", "-", "-", "-", "|", "*", "|", "|", "*", "*", "*", "*", "*", "*", "*"],
            ["-", "-", "-", "*", "|", "-", "-", "|", "|", "*", "|", "-", "-", "-", "-", "-", "-", "|", "*", "|", "|", "-", "-", "|", "*", "-", "-", "-"],
            [" ", " ", "|", "*", "|", "-", "-", "-", "|", "*", "|", "-", "-", "-", "-", "-", "-", "|", "*", "|", "-", "-", "-", "|", "*", "|", " ", " "],
            [" ", " ", "|", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "B", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "|", " ", " "],
            [" ", " ", "|", "*", "-", "-", "*", "-", "-", "*", "|", "-", "-", " ", " ", "-", "-", "|", "*", "-", "-", "*", "-", "-", "*", "|", " ", " "],
            ["-", "-", "-", "*", "|", "|", "*", "|", "|", "*", "|", " ", " ", " ", " ", " ", " ", "|", "*", "|", "|", "*", "|", "|", "*", "-", "-", "-"],
            ["|", "*", "*", "*", "|", "|", "*", "|", "|", "*", "|", " ", " ", " ", " ", " ", " ", "|", "*", "|", "|", "*", "|", "|", "*", "*", "*", "|"],
            ["|", "*", "|", "-", "-", "|", "*", "|", "|", "*", "|", " ", "P", "I", "C", " ", " ", "|", "*", "|", "|", "*", "|", "-", "-", "|", "*", "|"],
            ["|", "*", "|", "-", "-", "|", "*", "-", "-", "*", "|", "-", "-", "-", "-", "-", "-", "|", "*", "-", "-", "*", "|", "-", "-", "|", "*", "|"],
            ["|", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "|"],
            ["-", "-", "-", "*", "-", "-", "*", "-", "-", "*", "|", "-", "-", "-", "-", "-", "-", "|", "*", "-", "-", "*", "-", "-", "*", "-", "-", "-"],
            [" ", " ", "|", "*", "|", "|", "*", "|", "|", "*", "|", "-", "-", "-", "-", "-", "-", "|", "*", "|", "|", "*", "|", "|", "*", "|", " ", " "],
            [" ", " ", "|", "*", "|", "|", "*", "|", "|", "*", "*", "*", "*", "|", "|", "*", "*", "*", "*", "|", "|", "*", "|", "|", "*", "|", " ", " "],
            [" ", " ", "|", "*", "|", "|", "*", "|", "-", "-", "-", "|", "*", "|", "|", "*", "|", "-", "-", "-", "|", "*", "|", "|", "*", "|", " ", " "],
            ["-", "-", "-", "*", "|", "|", "*", "|", "-", "-", "-", "|", "*", "-", "-", "*", "|", "-", "-", "-", "|", "*", "|", "|", "*", "-", "-", "-"],
            ["|", "*", "*", "*", "|", "|", "*", "*", "*", "*", "*", "*", "*", "P", "*", "*", "*", "*", "*", "*", "*", "*", "|", "|", "*", "*", "*", "|"],
            ["|", "*", "|", "-", "-", "-", "-", "-", "-", "|", "*", "|", "-", "-", "-", "-", "|", "*", "|", "-", "-", "-", "-", "-", "-", "|", "*", "|"],
            ["|", "*", "|", "-", "-", "-", "-", "-", "-", "|", "*", "|", "-", "-", "-", "-", "|", "*", "|", "-", "-", "-", "-", "-", "-", "|", "*", "|"],
            ["|", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "|", "|", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "|"],
            ["|", "*", "|", "-", "-", "|", "*", "|", "-", "-", "-", "|", "*", "|", "|", "*", "|", "-", "-", "-", "|", "*", "|", "-", "-", "|", "*", "|"],
            ["|", "*", "|", "-", "-", "|", "*", "|", "-", "-", "-", "|", "*", "-", "-", "*", "|", "-", "-", "-", "|", "*", "|", "-", "-", "|", "*", "|"],
            ["|", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "|"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ]
        self.actual_map = copy.deepcopy(self.pacman_map)
        self.score = 0
        self.pac = PacMan()
        self.blinky = Blinky()
        # self.pinky = Pinky()
        # self.inky = Inky()
        # self.clyde = Clyde()
        self.ghosts = [self.blinky] #, self.pinky, self.inky, self.clyde]
        self.spawn()
    
    def check_for_win(self):
        for i in self.actual_map:
            for j in i:
                if j == "*" or j == "O":
                    return False
        return True
    
    def spawn(self):
        for i in range(len(self.actual_map)):
            for j in range(len(self.actual_map[i])):
                if self.actual_map[i][j] == "P":
                    self.pac.pos = [i, j]
                    self.actual_map[i][j] = self.pac.pacman[self.pac.direction]
                    break
        for i in range(len(self.actual_map)):
            for j in range(len(self.actual_map[i])):
                if self.actual_map[i][j] == "B":
                    self.blinky.pos = [i, j]
                    self.actual_map[i][j] = " "
                    break
    
    def ghost_move(self, ghost, direction):
        walls = ["|", "-", " "]
        position = ghost.pos
        if ghost.is_eaten:
            ghost_eaten_move()
            return
        if direction == "R":
            # Travelling right
            if position[1] == self.map_size[1]-1:
                ghost.pos[1] = 0
                self.actual_map[position[0]][position[1]] = " "
                self.actual_map[position[0]][0] = ghost.sprite[0]
            else:
                ghost.pos[1] += 1
                self.actual_map[position[0]][position[1]] = " "
                self.actual_map[position[0]][position[1] + 1] = ghost.sprite[0]
        elif direction == "L":
            # Travelling left
            if position[1] == 0:
                ghost.pos[1] = self.map_size[1]-1
                self.actual_map[position[0]][position[1]] = " "
                self.actual_map[position[0]][(self.map_size[1]-1)] = ghost.sprite[0]
            else:
                ghost.pos[1] -= 1
                self.actual_map[position[0]][position[1]] = " "
                self.actual_map[position[0]][position[1] - 1] = ghost.sprite[0]
        # Travelling up or down
        elif direction == "D":
            # Travelling down
            ghost.pos[0] += 1
            self.actual_map[position[0]][position[1]] = " "
            self.actual_map[position[0] + 1][position[1]] = ghost.sprite[0]
        elif direction == "U":
            # Travelling up
            ghost.pos[0] -= 1
            self.actual_map[position[0]][position[1]] = " "
            self.actual_map[position[0] - 1][position[1]] = ghost.sprite[0]
    
    def move(self):
        #! TODO: UPDATE SCORE!
        walls = ["|", "-", " "] # The characters that represent walls
        position = self.pac.pos.copy()
        n_direction = self.pac.n_direction
        if n_direction == 3:
            if position[1] == self.map_size[1]-1:
                self.pac.direction = 3
            elif self.pacman_map[position[0]][position[1] + 1] not in walls:
                self.pac.direction = 3
        elif n_direction == 4:
            if position[1] == 0:
                self.pac.direction = 4
            elif self.pacman_map[position[0]][position[1] - 1] not in walls:
                self.pac.direction = 4
        elif n_direction == 1:
            if self.pacman_map[position[0] + 1][position[1]] not in walls:
                self.pac.direction = 1
        else:
            if self.pacman_map[position[0] - 1][position[1]] not in walls:
                self.pac.direction = 2
        
        direction = self.pac.direction
        
        if direction > 2:
            # Travelling left or right
            if direction == 3:
                # Travelling right
                if position[1] == self.map_size[1]-1:
                    self.pac.pos[1] = 0
                    self.actual_map[position[0]][position[1]] = " "
                    self.actual_map[position[0]][0] = self.pac.pacman[3]
                else:
                    if self.pacman_map[position[0]][position[1] + 1] not in walls:
                        self.pac.pos[1] += 1
                        self.actual_map[position[0]][position[1]] = " "
                        self.actual_map[position[0]][position[1] + 1] = self.pac.pacman[3]
            elif direction == 4:
                # Travelling left
                if position[1] == 0:
                    self.pac.pos[1] = self.map_size[1]-1
                    self.actual_map[position[0]][position[1]] = " "
                    self.actual_map[position[0]][(self.map_size[1]-1)] = self.pac.pacman[3]
                else:
                    if self.pacman_map[position[0]][position[1] - 1] not in walls:
                        self.pac.pos[1] -= 1
                        self.actual_map[position[0]][position[1]] = " "
                        self.actual_map[position[0]][position[1] - 1] = self.pac.pacman[4]
        elif direction <= 2 and direction > 0:
            # Travelling up or down
            if direction == 1:
                # Travelling down
                if self.pacman_map[position[0] + 1][position[1]] not in walls:
                    self.pac.pos[0] += 1
                    self.actual_map[position[0]][position[1]] = " "
                    self.actual_map[position[0] + 1][position[1]] = self.pac.pacman[1]
            elif direction == 2:
                # Travelling up
                if self.pacman_map[position[0] - 1][position[1]] not in walls:
                    self.pac.pos[0] -= 1
                    self.actual_map[position[0]][position[1]] = " "
                    self.actual_map[position[0] - 1][position[1]] = self.pac.pacman[2]
    
    def update(self):
        # Move pacman
        self.move()
        for ghost in self.ghosts:
            # Move ghosts
            self.ghost_move(ghost, ghost.get_movement(self.actual_map, self.pac.pos))
        if self.check_for_win():
            return True
    
    def __str__(self):
        # Print the map
        out = ""
        for i in self.actual_map:
            for j in i:
                out += j + " "
            out += "\n"
        return out


class PacMan:
    def __init__(self):
        self.pacman = ["0", "ᗣ", "ᗢ", "ᗧ", "ᗤ"]
        self.direction = 0 # The index of the appropriate sprite in the pacman list
        self.n_direction = -1 # The next direction
        self.pos = []


class Blinky:
    def __init__(self):
        self.sprite = ["Β", "β"]
        # self.target_pos = [] # The next position
        self.pos = [0,0]
        self.state = 1 # 0 = scatter, 1 = chase, 2 = frightened, 3 = eaten
        self.is_eaten = False
        self.directions = ["D", "U", "R", "L"]
        self.facing = 2 # The index of the direction it can't turn to
    
    def get_movement(self, actual_map, target_pos):
        m = copy.deepcopy(actual_map)
        walls = ["|", "-", " "]
        position = self.pos
        tilePos = []
        valid_directions = []
        direction = ""
        distances = []
        min_distance = 9999999999999999999999999999999999999
        for i in range(len(self.directions)):
            if i != self.facing:
                if i == 3:
                    if self.pos[1] == 30:
                        valid_directions.append("R")
                        tilePos.append([self.pos[0], 0])
                    elif m[position[0]][position[1] + 1] not in walls:
                        valid_directions.append("R")
                        tilePos.append([position[0], (position[1] + 1)])   
                elif i == 4:
                    if self.pos[1] == 0:
                        valid_directions.append("L")
                        tilePos.append([self.pos[0], 30])
                    elif m[position[0]][position[1] - 1] not in walls:
                        valid_directions.append("L")
                        tilePos.append([self.pos[0], 30])
                elif i == 1:
                    if m[position[0] + 1][position[1]] not in walls:
                        valid_directions.append("U")
                        tilePos.append([position[0] + 1, position[1]])
                else:
                    if m[position[0] - 1][position[1]] not in walls:
                        valid_directions.append("D")
                        tilePos.append([position[0] - 1, position[1]])
        if len(tilePos) == 1:
            return valid_directions[0]
        print(target_pos)
        print(tilePos)
        print(valid_directions)
        for i in range(len(tilePos)):
            print(i)
            distance = (tilePos[i][0] - target_pos[0])**2 + (tilePos[i][1] - target_pos[1])**2
            distance = distance**0.5
            if distance < min_distance:
                min_distance = distance
                direction = valid_directions[i]
        return direction