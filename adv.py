from room import Room
from player import Player
from world import World
from util import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


traversal_path = []

# When we backtrack, switch directions
reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# stack to keep track of directions while we go through graph
stack = Stack()

# push our starting room into stack
stack.push([player.current_room])

# alL posible directions we could go in an array
paths = ['n', 's', 'e', 'w']


# print(room_graph)
# rooms = player.current_room.get_exits()

# print(rooms)
# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
print("current_room", player.current_room)


while stack.size() > 0:
    direction = stack.pop()
    # Travel to popped direction
    player.travel(direction)

    # check if current room has been visited
    if player.current_room not in visited_rooms:
        # Reverse direction in case we've been in the room
        traversal_path.append(reverse[direction])
        # push reversed direction into stack
        stack.push(reverse[direction])
        # add room currently in to visited
        visited_rooms.add(player.current_room)

    # loop through paths and check if current room has any viable paths
    for next_direction in paths:
        # get current room player in
        curr_room = player.current_room
        # for every room found, initialize a variable
        next_room = curr_room.get_room_in_direction(next_direction)
        # print("this is next_room",  next_room,
        #       "this is next_direction", next_direction)
        # if room hasn't been visited and is not none, add it to traversal_path, and stack
        if next_room != None and next_room not in visited_rooms:
            traversal_path.append(next_direction)
            stack.push(next_direction)
            break

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
