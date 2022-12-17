from __future__ import annotations

from moves import Moves
from result import Result


class Game:

    def __init__(self, opponent_moves, intended_results):
        self.opponent_moves: list[Moves] = opponent_moves
        self.intended_results: list[Result] = intended_results
        self.current_score: int = 0

    def turns_remaining(self) -> int:
        return len(self.opponent_moves)

    @staticmethod
    def determine_player_move(opponent_move: Moves, intended_result: Result) -> Moves:
        return {
            (Moves.ROCK, Result.WIN): Moves.PAPER,
            (Moves.PAPER, Result.WIN): Moves.SCISSORS,
            (Moves.SCISSORS, Result.WIN): Moves.ROCK,
            (Moves.ROCK, Result.LOSS): Moves.SCISSORS,
            (Moves.PAPER, Result.LOSS): Moves.ROCK,
            (Moves.SCISSORS, Result.LOSS): Moves.PAPER,
            (Moves.ROCK, Result.DRAW): Moves.ROCK,
            (Moves.PAPER, Result.DRAW): Moves.PAPER,
            (Moves.SCISSORS, Result.DRAW): Moves.SCISSORS,
        }[(opponent_move, intended_result)]

    def play_all_turns(self):
        for i, (opponent_move, intended_result) in enumerate(zip(self.opponent_moves, self.intended_results)):
            player_move = self.determine_player_move(opponent_move, intended_result)
            self.update_score(player_move, intended_result)

    def update_score(self, player_move: Moves, result: Result):
        score: int = 0
        if result == Result.WIN:
            score += 6
        if result == Result.DRAW:
            score += 3
        if player_move == Moves.ROCK:
            score += 1
        if player_move == Moves.PAPER:
            score += 2
        if player_move == Moves.SCISSORS:
            score += 3
        self.current_score += score

    def play_turn(self):
        opponent_move = self.opponent_moves.pop(0)
        intended_result = self.intended_results.pop(0)
        player_move = self.determine_player_move(opponent_move, intended_result)
        self.current_score += self.get_score_from_moves(player_move, intended_result)

    def get_total_score(self) -> int:
        return self.current_score

    @classmethod
    def from_file(cls, filename) -> Game:
        opponent_moves = []
        intended_results = []
        with open(filename) as file:
            for line in file:
                moves = line.strip().split()
                opponent_moves.append(Moves(moves[0]))
                intended_results.append(Result(moves[1]))
        return Game(opponent_moves, intended_results)

    @staticmethod
    def get_score_from_moves(player_move: Moves, result: Result) -> int:
        score: int = 0
        if result == Result.WIN:
            score += 6
        if result == Result.DRAW:
            score += 3
        if player_move == Moves.ROCK:
            score += 1
        if player_move == Moves.PAPER:
            score += 2
        if player_move == Moves.SCISSORS:
            score += 3
        return score
