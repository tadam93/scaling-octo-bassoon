from CommandDefinitions import *
from math import floor

class FieldManager:
    """Accepts a field  file, loads the field and manages displaying the field"""
    def __init__(self, field_script):
        absolute_mine_locations = list()
        row = 0
        total_cols = 0
        # calculate the absolute mine location based on the field being
        # in quadrant 4
        for line in open(field_script).readlines():
            row_characters = list(line.strip())
            if total_cols == 0:
                total_cols = len(row_characters)

            for col in range(0, len(row_characters)):
                character = row_characters[col]
                if character != ".":
                    absolute_mine_locations.append([col, row, character])
            row += 1

        # row keeps track of how many lines we traversed, effectively a total count
        total_rows = row
        ship_x = floor(total_rows / 2) #x coord
        ship_y = floor(total_cols / 2) #y coord

        # translate mines so they're relative to the ship location
        self.relative_mine_locations = self.convert_to_relative_locations(absolute_mine_locations, (ship_x, ship_y))
        self.starting_mine_count = len(self.relative_mine_locations)


    def fire(self, fire_command):
        fire_pattern = fire_patterns()[fire_command]
        for target in fire_pattern:
            for index in range(0, len(self.relative_mine_locations)):
                if target[0] == self.relative_mine_locations[index][0] and target[1] == self.relative_mine_locations[index][1]:
                    del self.relative_mine_locations[index]
                    break


    def contains_mines(self):
        return len(self.relative_mine_locations) > 0

    def get_starting_mine_count(self):
        return self.starting_mine_count

    def convert_to_relative_locations(self, mine_locations, ship_location):
        relative_mine_locations = list()
        for mine in mine_locations:
            relative_mine_location = [mine[0] - ship_location[0], mine[1] - ship_location[1],  mine[2]]
            relative_mine_locations.append(relative_mine_location)
        return relative_mine_locations

    def convert_to_absolute_locations(self, mine_locations, ship_location):
        absolute_mine_locations = list()
        for mine in mine_locations:
            absolute_mine_location = [mine[0] + ship_location[0], mine[1] - ship_location[1], mine[2]]
            absolute_mine_locations.append(absolute_mine_location)
        return absolute_mine_locations

    def move(self, command):
        movement_pattern = movement_patterns()[command]
        new_mine_locations = list()
        for mine in self.relative_mine_locations:
            new_mine_location = [mine[0] - movement_pattern[0], mine[1] + movement_pattern[1], mine[2]]
            new_mine_locations.append(new_mine_location)
        self.relative_mine_locations = new_mine_locations

    # returns false if ship is now at or below a level that mines exist on
    def drop(self):
        new_mine_locations = list()
        above_mines = True
        for mine in self.relative_mine_locations:
            old_char = ord(mine[2])
            new_char = '*'
            if old_char == ord('A'):
                new_char = 'z'
            elif old_char == ord('a'):
                new_char = '*'
                above_mines = False
            else:
                new_char = chr(old_char - 1)
            new_mine_locations.append([mine[0], mine[1], new_char])
        self.relative_mine_locations = new_mine_locations
        return above_mines

    def get_display(self):
        # calculate distance to furthest mine by row
        # calculate distance to furthest mine by column
        col_max = 0
        row_max = 0
        for mine in self.relative_mine_locations:
            if abs(mine[0]) > col_max:
                col_max = abs(mine[0])
            if abs(mine[1]) > row_max:
                row_max = abs(mine[1])
        # create field of '.'
        num_rows = row_max * 2 + 1
        num_cols = col_max * 2 + 1
        field_display_list = list()
        for r in range(0, num_rows):
            field_display_list.append("")
            for c in range(0, num_cols):
                field_display_list[r] += "."

        absolute_ship_location = [col_max, row_max]
        absolute_mine_locations = self.convert_to_absolute_locations(self.relative_mine_locations, absolute_ship_location)
        # place mines
        for index in range(0, len(absolute_mine_locations)):
            mine_location = absolute_mine_locations[index]
            field_row = list(field_display_list[abs(mine_location[1])])
            field_row[mine_location[0]] = mine_location[2]
            field_display_list[abs(mine_location[1])] = "".join(field_row)

        field_display = ""
        for line in field_display_list:
            field_display += line + "\n"
        return field_display.strip()
