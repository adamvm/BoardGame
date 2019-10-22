import unittest

from Compass import Compass

directions = {"N": {"x": 0, "y": 1},
              "E": {"x": 1, "y": 0},
              "S": {"x": 0, "y": -1},
              "W": {"x": -1, "y": 0}}


class Board(object):

    def __init__(self, size=5, position_x=0, position_y=0, direction="N"):
        self._dimension = {"x": range(0, size),
                           "y": range(0, size)}
        self._position = {"x": position_x,
                          "y": position_y}
        self._direction = Compass(directions, direction)

        if not self.is_position_valid(self._position):
            raise ValueError

    def __str__(self):
        coordinates = " ".join([str(self._position[k])
                                for k in self._position])
        return f"{coordinates} {self._direction}"

    def get_state(self) -> str:
        return str(self)

    def execute(self, command: str) -> str:
        execution = {
            "L": self._direction.turn_left,
            "R": self._direction.turn_right,
            "M": self._move}

        if not all([c in execution for c in command]):
            raise NotImplementedError

        for c in command:
            execution[c]()

        return self.get_state()

    def _move(self) -> None:
        shift = self._direction.get_shift()
        new_position = {k: self._position[k] + shift[k] for k in shift}
        if self.is_position_valid(new_position):
            self._position = new_position

    def is_position_valid(self, new_position: dict) -> bool:
        return all([new_position[k] in self._dimension[k]
                    for k in new_position])


class BoardTest(unittest.TestCase):
    def test_board_initial_state_default_values_set_and_read(self):
        test_bd = Board()
        self.assertEqual("0 0 N", test_bd.get_state())

    def test_board_initial_state_custom_initial_values_set_and_read(self):
        test_bd = Board(position_x=4, position_y=4, direction="S")
        self.assertEqual("4 4 S", test_bd.get_state())

    def test_board_initial_position_outside_board_should_raise_exception(self):
        self.assertRaises(ValueError,
                          Board, size=3, position_x=4,
                          position_y=5, direction="S")

    def test_command_not_supported_should_raise_exception(self):
        test_bd = Board()
        with self.assertRaises(NotImplementedError):
            test_bd.execute("S")

    def test_track_1(self):
        test_bd = Board()
        self.assertEqual("2 2 E", test_bd.execute("MRMLMRM"))

    def test_track_2(self):
        test_bd = Board()
        self.assertEqual("3 2 N", test_bd.execute("RMMMLMM"))

    def test_track_3(self):
        test_bd = Board()
        self.assertEqual("0 4 N", test_bd.execute("MMMMM"))

    def test_track_4(self):
        test_bd = Board()
        self.assertEqual("4 0 N", test_bd.execute("RMMMMML"))

    def test_track_5(self):
        test_bd = Board()
        self.assertEqual("0 0 S", test_bd.execute("LLMM"))
