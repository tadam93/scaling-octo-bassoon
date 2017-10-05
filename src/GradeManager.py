class GradeManager:
    def __init__(self):
        self.shot_count = 0
        self.movement_count = 0

    def record_shot(self):
        self.shot_count += 1

    def record_movement(self):
        self.movement_count += 1

    def calculate(self, field_manager, remaining_commands):
        if field_manager.contains_mines():
            return 0

        if remaining_commands > 0:
            return 1

        starting_score = 10 * field_manager.get_starting_mine_count()
        shot_penalty = min(5*self.shot_count, 5*field_manager.get_starting_mine_count())
        movement_penalty = min(2*self.movement_count, 3*field_manager.get_starting_mine_count())

        return starting_score - shot_penalty - movement_penalty
