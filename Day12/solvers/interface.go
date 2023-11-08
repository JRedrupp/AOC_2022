package solvers

import "aoc2022/day12/position"

type PathSolverInterface interface {

	// Create the PositionMap from the given file.
	Initialize(path_to_map string) (*position.PositionMap, error)

	// Solve the path.
	Solve(p_map *position.PositionMap, start_index int) ([]position.Position, error)
}
