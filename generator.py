import math
import random
import string

class WordSearch():
    def __init__(self, words):
        self.words = words
        self.words_copy = words.copy()
        self.size = self.__computeGridSize()
        self.grid = [ [ "_" for i in range(self.size) ] for i in range(self.size) ]
        self.directions = [{"x_step": 0, "y_step": 1}, {"x_step": 1, "y_step": 0}, {"x_step": 1, "y_step": 1}, {"x_step": 1, "y_step": -1},
                           {"x_step": 0, "y_step": -1}, {"x_step": -1, "y_step": 0}, {"x_step": -1, "y_step": -1}, {"x_step": -1, "y_step": 1}]

    def __computeGridSize(self):
        total_characters = sum(len(word) for word in self.words)
        average_word_length = total_characters // len(self.words)
        max_word_length = max(len(word) for word in self.words)
        
        # Calculate initial grid size based on number of words and average word length
        grid_size = math.ceil(math.sqrt(len(self.words) * average_word_length))
        
        grid_size = max(grid_size, max_word_length)
        
        grid_size *= 2
        return grid_size

    def __randomCoords(self) -> tuple:
        return (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
    
    def __valid_direction(self, word, coords) -> dict:
        x_pos, y_pos = coords
        random.shuffle(self.directions)
        valid_direction = True
        for direction in self.directions:
            for i in range(len(word)):
                try: 
                    if (x_pos + i * (direction["x_step"])) < 0 or (y_pos + i * (direction["y_step"])) < 0:
                        valid_direction = False
                        break
                    if self.grid[(y_pos + i * (direction["y_step"]))][(x_pos + i * (direction["x_step"]))] != "_" and self.grid[(y_pos + i * (direction["y_step"]))][(x_pos + i * (direction["x_step"]))] != word[i]:
                        valid_direction = False
                        break
                except IndexError:
                    valid_direction = False
                    break

            if valid_direction:
                return direction
        return None

    def __place_word(self, word, coords, direction):
        x_pos, y_pos = coords

        for i in range(len(word)):
                self.grid[(y_pos + i*(direction["y_step"]))][(x_pos + i*(direction["x_step"]))] = word[i]

    def __fillBlankIn(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == "_":
                    self.grid[row][col] = random.choice(string.ascii_uppercase)
    
    def generate_word_search(self) -> list[list[chr]]:
        while len(self.words) != 0:
            # Get random coords, current word, and random direction
            coords = self.__randomCoords()
            word = self.words[0].upper()
            direction = self.__valid_direction(word, coords)
            if not direction:
                continue

            # Place word on board and remove from working words list
            self.__place_word(word, coords, direction)
            self.words.pop(0)

        # After all words are inserted, fill in blanks with random characters
        self.__fillBlankIn()
        return self.grid