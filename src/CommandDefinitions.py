def movement_patterns() :
    return {
        "north": (0, -1),
        "south": (0, 1),
        "east": (1, 0),
        "west": (-1, 0)
    }

def fire_patterns():
    return {
        "alpha": ((-1, -1), (-1, 1), (1, -1), (1, 1)),
        "beta": ((-1, 0), (0, -1), (0, 1), (1, 0)),
        "gamma": ((-1, 0), (0, 0), (1, 0)),
        "delta": ((0, -1), (0, 0), (0, 1))
    }
