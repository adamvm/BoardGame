import unittest


class Compass(object):
    def __init__(self, possible_directions, current_direction):
        self._current_direction = current_direction
        self._dir_iteration = list(possible_directions.keys())
        self._directions = possible_directions

    def get_direction(self) -> str:
        return self._current_direction

    def turn_right(self) -> None:
        index = self._dir_iteration.index(self._current_direction)
        if index + 1 < len(self._dir_iteration):
            self._current_direction = self._dir_iteration[index + 1]
        else:
            self._current_direction = self._dir_iteration[0]

    def turn_left(self) -> None:
        index = self._dir_iteration.index(self._current_direction)
        if index - 1 < 0:
            self._current_direction = self._dir_iteration[-1]
        else:
            self._current_direction = self._dir_iteration[index - 1]

    def get_shift(self) -> str:
        return self._directions[self._current_direction]

    def __str__(self):
        return self._current_direction


class CompassTest(unittest.TestCase):
    directions = {"N": {"x": 0, "y": 1},
                  "E": {"x": 1, "y": 0},
                  "S": {"x": 0, "y": -1},
                  "W": {"x": -1, "y": 0}}

    def test_initial_direction(self):
        test_comp = Compass(self.directions, "S")
        self.assertEqual("S", test_comp.get_direction())

    def test_move_right_simple_case(self):
        test_comp = Compass(self.directions, "N")
        test_comp.turn_right()
        self.assertEqual("E", test_comp.get_direction())

    def test_move_right_corner_case(self):
        test_comp = Compass(self.directions, "W")
        test_comp.turn_right()
        self.assertEqual("N", test_comp.get_direction())

    def test_move_left_simple_case(self):
        test_comp = Compass(self.directions, "E")
        test_comp.turn_left()
        self.assertEqual("N", test_comp.get_direction())

    def test_move_left_corner_case(self):
        test_comp = Compass(self.directions, "N")
        test_comp.turn_left()
        self.assertEqual("W", test_comp.get_direction())

    def test_get_movement_first_element(self):
        test_comp = Compass(self.directions, "N")
        self.assertEqual({"x": 0, "y": 1}, test_comp.get_shift())

    def test_get_movement_another_element(self):
        test_comp = Compass(self.directions, "S")
        self.assertEqual({"x": 0, "y": -1}, test_comp.get_shift())
