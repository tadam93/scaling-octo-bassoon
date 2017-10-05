from CommandDefinitions import *
from ScriptManager import *
from FieldManager import *
from GradeManager import *
import sys


'''
Assumptions
Script file:
1. Command scripts may contain commands that don't exist
2. Capitalization doesn't matter
3. Command scripts may contain extra whitespace around the commands
4. There is a max two commands per line in the script file. One movement and one fire command
5. Only need to support English

Fields file:
1. Fields will always have at least one row
2. Fields can be any dimension
3. If a field has an even dimension, starting point defaults to the coordinate closest to the bottom right corner.
'''

def evaluate(field_path, script_path):
    evaluation_result = ""
    field_manager = FieldManager(field_path)
    script_manager = ScriptManager(script_path)
    grade_manager = GradeManager()
    step_count = 1
    for command_set in script_manager:
        # before command is executed
        evaluation_result += "Step " + str(step_count) + "\n\n"
        evaluation_result += str(field_manager.get_display()) + "\n\n"
        evaluation_result += command_set + "\n\n"

        for command in command_set.split(" "):
            if command in movement_patterns():
                field_manager.move(command)
                grade_manager.record_movement()
            elif command in fire_patterns():
                field_manager.fire(command)
                grade_manager.record_shot()

        dropped_below_mine_level = field_manager.drop()

        # after command is executed
        step_count += 1
        evaluation_result += str(field_manager.get_display()) + "\n\n"

        #stop running steps if there are leftover mines
        if field_manager.contains_mines() == False or dropped_below_mine_level == False:
            break

    grade = grade_manager.calculate(field_manager, script_manager.get_command_count() - step_count + 1)
    if grade > 0:
        evaluation_result += "pass (" + str(grade) + ")"
    else:
        evaluation_result += "fail (" + str(grade) + ")"
    return evaluation_result

def display_usage():
    print("Usage: ")
    print("python3 mineclearing_validator.py <path/to/field.txt> <path/to/script.txt>\n")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        display_usage()
        exit()

    field_path = sys.argv[1]
    script_path = sys.argv[2]
    try:
        print(evaluate(field_path, script_path))
    except FileNotFoundError as err:
        print(err)
