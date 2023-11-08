package position

import (
	"fmt"
	"math"
)

type Position struct {
	x int
	y int
	h int
}

func New(x int, y int, h int) Position {
	return Position{x, y, h}
}

func (p Position) String() string {
	return fmt.Sprintf("(x: %d, y: %d, h: %d)", p.x, p.y, p.h)
}

// Equals returns true if the given position is equal to the current position.
func (p Position) Equals(other Position) bool {
	return p.x == other.x && p.y == other.y
}

func (p Position) Distance(other Position) int {
	// Distance = |x1 - x2| + |y1 - y2| + |h1 - h2|
	return int(math.Abs(float64(p.h-other.h) * 100))
}

func (p Position) EdgeWeight(other Position) int {
	// EdgeWeight = INF if h2 - h1 > 1
	// Going up should be preferred, as the end is always higher than the start.
	// Going flat is preferred over going down.

	var h_change = other.h - p.h
	if h_change > 1 {
		return math.MaxInt32
	} else if h_change == 1 {
		return 1
	} else if h_change == 0 {
		return 10
	} else {
		return 100
	}

}

type PositionMap struct {
	p_arr         []Position
	x_len         int
	p_start_index []int
	p_end_index   int
}

func GetNeighbors(p Position, p_map *PositionMap) []Position {
	neighbors := []Position{}

	// Up
	if p.y > 0 {
		neighbors = append(neighbors, p_map.p_arr[p.x+(p.y-1)*p_map.x_len])
	}

	// Down
	if p.y < len(p_map.p_arr)/p_map.x_len-1 {
		neighbors = append(neighbors, p_map.p_arr[p.x+(p.y+1)*p_map.x_len])
	}

	// Left
	if p.x > 0 {
		neighbors = append(neighbors, p_map.p_arr[p.x-1+p.y*p_map.x_len])
	}

	// Right
	if p.x < p_map.x_len-1 {
		neighbors = append(neighbors, p_map.p_arr[p.x+1+p.y*p_map.x_len])
	}

	return neighbors

}

func (pm *PositionMap) GetPositionAtIndex(index int) Position {
	return pm.p_arr[index]
}

func (pm *PositionMap) GetEndIndex() int {
	return pm.p_end_index
}

func NewPositionMap(p_arr []Position, x_len int, p_start_index []int, p_end_index int) PositionMap {
	return PositionMap{p_arr, x_len, p_start_index, p_end_index}
}

func (pm *PositionMap) GetStartIndex() []int {
	return pm.p_start_index
}

// Print prints the map.
func (pm *PositionMap) Print() {

	fmt.Println("Starts: ", pm.p_start_index)
	for _, p := range pm.p_start_index {
		fmt.Println("    ", pm.p_arr[p])
	}

	fmt.Println("End:", pm.p_arr[pm.p_end_index])
	fmt.Println("Map:")

	for _, p := range pm.p_arr {
		fmt.Print(string(p.h))
		if p.x == pm.x_len-1 {
			fmt.Println()
		}
	}
}
