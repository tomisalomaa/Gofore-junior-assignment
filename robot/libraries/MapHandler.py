def turn_string_into_list_of_characters(text_string):
    characters = list(text_string)
    return characters

# Given a map in a list of lists format,
# goes through each individual list to first determine
# which list contains the starting position marked as 'S'.
# If found, finds the index of 'S' within the list.
# If 'S' is found, returns y and x values that can be
# used as index values to refer S from the input map.
def find_robot_location(map):
    x = None
    y = None
    for idx, row in enumerate(map):
        print(row)
        if 'S' in row:
            y = idx
            break
    if y:
        for idx, col in enumerate(map[y]):
            if col == 'S':
                x = idx
                break
        return y, x
    else:
        return x

# Given a list of lists as a map and a starting location,
# traverses the map until a specific end spot is found.
def traverse_map(map, loc, direction=0, steps=0):
    steps_traversed = steps
    current_direction = direction
    y = loc[0]
    x = loc[1]
    current_spot = map[y][x] # Saved for map representation purposes
    # While no new position could not be determined,
    # continue trying to determine the next position.
    # If during a loop no new location could be determined (as in: 
    # the next step with a current direction would lead into an obstacle),
    # Turn 90 degrees right and try again.
    while y == loc[0] and x == loc[1]:
      if current_direction == 0 and map[y-1][x] and map[y-1][x] != '#':
          y -= 1
      elif current_direction == 90 and map[y][x+1] and map[y][x+1] != '#':
          x += 1
      elif current_direction == 180 and map[y+1][x] and map[y+1][x] != '#':
          y += 1
      elif current_direction == 270 and map[y][x-1] and map[y][x-1] != '#':
          x -= 1
      if y == loc[0] and x == loc[1]:
        current_direction += 90
        # If we have gone a whole circle, refer up again as 0.
        if current_direction >= 360:
          current_direction = 0
    # If next step leads to the goal 'E', add one to steps and
    # return step amount.
    # Otherwise continue from the updated position.
    if map[y][x] == 'E':
        return steps_traversed+1
    else:
        if current_spot != 'S' and steps_traversed > 0:
            map[loc[0]][loc[1]] = 'R'
            print_status(map, loc, steps_traversed)
            map[loc[0]][loc[1]] = 'o'
        return traverse_map(map, [y,x], current_direction, steps_traversed+1)

# Print current location, steps and the map that has been traversed.
def print_status(map, loc, steps_traversed):
    print('loc:', loc, 'steps:', steps_traversed)
    for row in map:
        print(row)