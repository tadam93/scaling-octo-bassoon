from CommandDefinitions import *

class ScriptManager:
    """Accepts a command script file, loads the commands and manages access to the commands"""
    def __init__(self, command_script):
        self.commands = list()
        self.command_index = 0
        for command_line in open(command_script).readlines():
            for command in command_line.split(" "):
                command = command.strip().lower()
                if command not in movement_patterns() and command not in fire_patterns():
                    raise RuntimeError("Command not found: " + command)
            self.commands.append(command_line.strip())

    def get_command_count(self):
        return len(self.commands)

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.iter_index == len(self.commands):
            raise StopIteration
        command = self.commands[self.iter_index]
        self.iter_index += 1
        return command
