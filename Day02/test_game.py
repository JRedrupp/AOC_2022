import unittest

from moves import Moves
from result import Result
from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.opponent_moves = [Moves.ROCK, Moves.PAPER, Moves.SCISSORS]
        self.intended_results = [Result.WIN, Result.LOSS, Result.DRAW]
        self.game = Game(self.opponent_moves, self.intended_results)

    def test_game_instantiation(self):
        # Test instantiating the Game class
        self.assertEqual(self.game.opponent_moves, self.opponent_moves)
        self.assertEqual(self.game.intended_results, self.intended_results)
        self.assertEqual(self.game.current_score, 0)

    def test_turns_remaining(self):
        # Test the turns_remaining method
        self.assertEqual(self.game.turns_remaining(), 3)

    def test_determine_player_move(self):
        # Test the determine_player_move method
        self.assertEqual(
            self.game.determine_player_move(Moves.ROCK, Result.WIN), Moves.PAPER
        )
        self.assertEqual(
            self.game.determine_player_move(Moves.PAPER, Result.WIN), Moves.SCISSORS
        )
        self.assertEqual(
            self.game.determine_player_move(Moves.SCISSORS, Result.WIN), Moves.ROCK
        )
        self.assertEqual(
            self.game.determine_player_move(Moves.ROCK, Result.LOSS), Moves.SCISSORS
        )
        self.assertEqual(
            self.game.determine_player_move(Moves.PAPER, Result.LOSS), Moves.ROCK
        )
        self.assertEqual(
            self.game.determine_player_move(Moves.SCISSORS, Result.LOSS), Moves.PAPER
        )
        self.assertEqual(
            self.game.determine_player_move(Moves.ROCK, Result.DRAW), Moves.ROCK
        )
        self.assertEqual(
            self.game.determine_player_move(Moves.PAPER, Result.DRAW), Moves.PAPER
        )
        self.assertEqual(
            self.game.determine_player_move(Moves.SCISSORS, Result.DRAW),
            Moves.SCISSORS,
        )

    def test_update_score(self):
        # Test the update_score method
        self.game.update_score(Moves.ROCK, Result.WIN)
        self.assertEqual(self.game.current_score, 7)

        self.game.update_score(Moves.PAPER, Result.DRAW)
        self.assertEqual(self.game.current_score, 12)

        self.game.update_score(Moves.SCISSORS, Result.LOSS)
        self.assertEqual(self.game.current_score, 15)

    def test_play_turn_and_get_total_score(self):
        # Test the play_turn and get_total_score methods
        self.game.play_turn()
        self.assertEqual(self.game.current_score, 8)
        self.assertEqual(self.game.turns_remaining(), 2)
        self.assertEqual(self.game.get_total_score(), 8)

        self.game.play_turn()
        self.assertEqual(self.game.current_score, 9)
        self.assertEqual(self.game.turns_remaining(), 1)
        self.assertEqual(self.game.get_total_score(), 9)

        self.game.play_turn()
        self.assertEqual(self.game.current_score, 15)
        self.assertEqual(self.game.turns_remaining(), 0)
        self.assertEqual(self.game.get_total_score(), 15)


