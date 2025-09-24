import pandas as pd


# Read the file and create a DataFrame where each cell contains one character
def read_grid_to_dataframe(filename):
    with open(filename, 'r') as file:
        lines = [line.rstrip('\n') for line in file]
    
    # Convert each line to a list of characters
    grid_data = [list(line) for line in lines]
    
    # Create DataFrame
    df = pd.DataFrame(grid_data)
    
    return df


# Direction vectors: up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_chars = ['^', '>', 'v', '<']

def find_guard_start(df):
    """Find the guard's starting position and direction"""
    for char in direction_chars:
        positions = df == char
        if positions.any().any():
            row, col = positions.stack().idxmax()
            direction = direction_chars.index(char)
            return row, col, direction
    return None, None, None

def simulate_guard_patrol(df):
    """Simulate the guard's patrol and return visited positions"""
    # Find starting position
    start_row, start_col, start_dir = find_guard_start(df)
    if start_row is None:
        return set()
    
    # Current position and direction
    row, col, direction = start_row, start_col, start_dir
    visited = set()
    visited.add((row, col))
    
    rows, cols = df.shape
    
    while True:
        # Calculate next position
        dr, dc = directions[direction]
        next_row, next_col = row + dr, col + dc
        
        # Check if guard leaves the grid
        if (next_row < 0 or next_row >= rows or 
            next_col < 0 or next_col >= cols):
            break
        
        # Check if next position is an obstacle
        if df.iloc[next_row, next_col] == '#':
            # Turn right (90 degrees clockwise)
            direction = (direction + 1) % 4
        else:
            # Move forward
            row, col = next_row, next_col
            visited.add((row, col))
    
    return visited

# Usage
df = read_grid_to_dataframe('day06/input.txt')
print(f"Grid dimensions: {df.shape}")

# Find guard's starting position
start_row, start_col, start_dir = find_guard_start(df)
print(f"Guard starts at position ({start_row}, {start_col}) facing {direction_chars[start_dir]}")

# Simulate the patrol
visited_positions = simulate_guard_patrol(df)
print(f"Guard visited {len(visited_positions)} distinct positions")
