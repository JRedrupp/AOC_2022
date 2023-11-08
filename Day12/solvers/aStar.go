package solvers

import (
	"aoc2022/day12/position"
	"bufio"
	"log"
	"math"
	"os"
)

type AStarSolver struct {
	PART_2 bool
}

func (t AStarSolver) Initialize(path_to_map string) (*position.PositionMap, error) {
	p_arr := []position.Position{}

	// Read the file.
	file, err := os.Open(path_to_map)
	if err != nil {
		log.Println(err)
		return nil, err
	}
	defer file.Close()

	// Read the file line by line.
	scanner := bufio.NewScanner(file)
	var y = 0
	var max_x = 0
	var start_index []int
	var end_index int

	for scanner.Scan() {
		line := scanner.Text()
		for i, c := range line {
			var h rune
			switch c {
			case 'S':
				start_index = append(start_index, len(p_arr))
				h = []rune("a")[0]
			case 'E':
				end_index = len(p_arr)
				h = []rune("z")[0]
			case 'a':
				if t.PART_2 {
					start_index = append(start_index, len(p_arr))
				}
				h = c
			default:
				h = c
			}
			p_arr = append(p_arr, position.New(i, y, int(h)))
		}
		y++
		if len(line) > max_x {
			max_x = len(line)
		}

	}
	p_map := position.NewPositionMap(p_arr, max_x, start_index, end_index)
	return &p_map, nil

}

func (t AStarSolver) Solve(p_map *position.PositionMap, start_index int) ([]position.Position, error) {

	var start = p_map.GetPositionAtIndex(start_index)
	var end = p_map.GetPositionAtIndex(p_map.GetEndIndex())

	// The set of discovered nodes that may need to be (re-)expanded.
	// Initially, only the start node is known.
	// This is usually implemented as a min-heap or priority queue rather than a hash-set.
	var openSet = make(map[position.Position]struct{})
	openSet[start] = struct{}{}

	// For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from the start
	// to n currently known.
	var cameFrom = make(map[position.Position]position.Position)

	// For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
	var gScore = make(costMap)
	gScore[start] = 0

	// For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
	// how cheap a path could be from start to finish if it goes through n.
	var fScore = make(scoreMap)
	fScore[start] = simple_heuristic(start, end)

	// Run until the open set is empty.
	for len(openSet) > 0 {

		// Get the node in the open set with the lowest score.
		current := getLowestScore(openSet, fScore, simple_heuristic, gScore, end)

		// If we've reached the end, reconstruct the path.
		if current.Equals(end) {
			return reconstruct_path(cameFrom, current), nil
		}

		// Remove the current node from the open set.
		delete(openSet, current)

		// For each neighbor of the current node...
		for _, neighbor := range position.GetNeighbors(current, p_map) {
			// d(current,neighbor) is the weight of the edge from current to neighbor
			// tentative_gScore is the distance from start to the neighbor through current
			tentative_gScore := gScore.getCost(current) + current.EdgeWeight(neighbor)
			if tentative_gScore < gScore.getCost(neighbor) {
				// This path to neighbor is better than any previous one. Record it!
				cameFrom[neighbor] = current
				gScore[neighbor] = tentative_gScore
				fScore[neighbor] = gScore.getCost(neighbor) + simple_heuristic(neighbor, end)
				openSet[neighbor] = struct{}{}
			}
		}

	}

	// Unsolvable.
	return []position.Position{}, nil
}

func simple_heuristic(start position.Position, end position.Position) int {
	return start.Distance(end)
}

type costMap map[position.Position]int

func (c costMap) getCost(p position.Position) int {
	// If the position is not in the map, return the max int value.
	if val, ok := c[p]; ok {
		return val
	}
	return math.MaxInt32
}

type scoreMap map[position.Position]int

func (s scoreMap) getScore(p position.Position, h func(position.Position, position.Position) int, c costMap, end position.Position) int {
	// For node n, fScore[n] := gScore[n] + h(n)
	if val, ok := s[p]; ok {
		return val
	}
	return c.getCost(p) + h(p, end)

}

func reconstruct_path(cameFrom map[position.Position]position.Position, current position.Position) []position.Position {
	// total_path := {current}
	// while current in cameFrom.Keys:
	//     current := cameFrom[current]
	//     total_path.prepend(current)
	// return total_path

	total_path := []position.Position{current}

	for {
		if val, ok := cameFrom[current]; ok {
			current = val
			total_path = append([]position.Position{current}, total_path...)
		} else {
			break
		}
	}
	return total_path

}

func getLowestScore(openSet map[position.Position]struct{}, fScore scoreMap, h func(position.Position, position.Position) int, gScore costMap, end position.Position) position.Position {
	var current position.Position
	var currentScore = math.MaxInt32
	for pos := range openSet {
		score := fScore.getScore(pos, h, gScore, end)
		if score < currentScore {
			current = pos
			currentScore = score
		}
	}
	return current
}
