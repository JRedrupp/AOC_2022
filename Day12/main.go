package main

import (
	"aoc2022/day12/position"
	"aoc2022/day12/solvers"
	"fmt"
	"os"
)

const PART_2 = true

func main() {

	// Pick your solver
	solver := solvers.AStarSolver{
		PART_2: PART_2,
	}

	args := os.Args[1:]
	if len(args) == 0 {
		fmt.Fprint(os.Stderr, "Please provide a path to a map file.\n")
		fmt.Fprint(os.Stderr, "Usage: day12 <path_to_map>\n")
		return
	}

	path := args[0]
	run(solver, path)
}

func run(solver solvers.PathSolverInterface, path_to_map string) {

	position_map, err := solver.Initialize(path_to_map)
	if err != nil {
		return
	}
	position_map.Print()

	best_path, fewest_steps := iterMultipleStarts(position_map, solver)

	fmt.Println("Path:")
	for _, p := range best_path {
		fmt.Println(p)
	}
	fmt.Println("Steps:", fewest_steps)
}

func iterMultipleStarts(position_map *position.PositionMap, solver solvers.PathSolverInterface) ([]position.Position, int) {
	var best_path []position.Position
	var fewest_steps int

	for _, start_index := range position_map.GetStartIndex() {
		path, err := solver.Solve(position_map, start_index)
		if err != nil {
			fmt.Println("WARN: Could not solve for start index", start_index)
			continue
		}

		if len(path) != 0 {
			if (fewest_steps == 0 && len(path) != 0) || len(path)-1 < fewest_steps {
				fewest_steps = len(path) - 1
				best_path = path
			}
		}
	}

	return best_path, fewest_steps
}
