#!/usr/bin/env python3

import sys
import signal

from copy import deepcopy


# Catch ^C.
def handle_sigint(s, f):
    print('Stopping script...')
    sys.exit(0)


signal.signal(signal.SIGINT, handle_sigint)

# Starting coordinates.
start_x = 12
start_y = 4

# Default board state.
default_board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


# Store game board state and associated path for each attempt.
class Attempt:
    # Current coordinates.
    x = y = 0

    # Path used to reach the associated game board state.
    path = []

    # Game board state.
    board = []

    # Constructor.
    def __init__(self, x, y, path, board):
        self.x = x
        self.y = y
        self.path = path
        self.board = board

    # Get a list of directions which can currently be accessed.
    def available_directions(self):

        # Start with an empty list.
        directions = []

        # Check all four directions every time.
        if self.can_move_up():
            directions.append("up")
        if self.can_move_down():
            directions.append("down")
        if self.can_move_left():
            directions.append("left")
        if self.can_move_right():
            directions.append("right")

        # Return the list of moveable directions.
        return directions

    # Check for non-visited cell in the up direction.
    def can_move_up(self):

        # Don't move off the board.
        if self.y == 0: return False

        # Check one space up.
        return bool(self.board[self.y - 1][self.x])

    # Check for non-visited cell in the down direction.
    def can_move_down(self):

        # Don't move off the board.
        if self.y == 8: return False

        # Check one space down.
        return bool(self.board[self.y + 1][self.x])

    # Check for non-visited cell to the left.
    def can_move_left(self):

        # Don't move off the board.
        if self.x == 0: return False

        # Check one space to the left.
        return bool(self.board[self.y][self.x - 1])

    # Check for non-visited cell to the right.
    def can_move_right(self):

        # Don't move off the board.
        if self.x == 12: return False

        # Check one space to the right.
        return bool(self.board[self.y][self.x + 1])

    # Move in the given direction.
    def move(self, direction):

        # Check the direction and update the current position.
        if direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1

        # Update the path with the current direction.
        self.path.append(direction)

        # Mark the current position as visited in
        # the game board.
        self.board[self.y][self.x] = 0

    # Check if the game board is solved.
    def solved(self):

        # Check every row.
        for row in range(len(self.board)):

            # Check every column.
            for column in range(len(self.board[row])):

                # Return _not_ solved if any available
                # spaces are found.
                if self.board[row][column]: return False

        # If no available spaces were found, this must
        # be a solved attempt.
        return True


# Initial execution point of the script.
def main():
    # Create an initial attempt to represent where
    # we begin in the puzzle.
    attempt = Attempt(start_x, start_y, [], default_board)

    # Begin processing the initial Attempt instance.
    process(attempt)


# Continue the given attempt by moving in the given direction.
def process(attempt, direction=''):
    # Check if a direction was given.
    if direction:
        # Update the attempt by moving in the given direction.
        attempt.move(direction)

    # Check if this attempt is a solution.
    if attempt.solved():
        # Print solution.
        print(attempt.path)

    # Iterate over each available direction (there will
    # be none if the attempt is solved).
    for direction in attempt.available_directions():
        # Make a new Attempt instance, continuing where
        # the previous attempt left off.
        new_attempt = deepcopy(attempt)

        # Call this process function again for the new attempt.
        process(new_attempt, direction)

    # Remove the previous attempt from memory.
    del attempt


# Execute main function.
if __name__ == "__main__":
    main()
