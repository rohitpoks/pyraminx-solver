import copy


FACE_LEFT = 0
FACE_RIGHT = 1
FACE_BACK = 2
FACE_BOTTOM = 3

IS_DEBUG_MODE = False

def print_face(face):
    print("  " + face[0] + "  ")
    print(" " + face[1] + face[2] + face[3] + " ")
    print(face[4] + face[5] + face[6] + face[7] + face[8])


def custom_state_tests():
    faces = [[], [], [], []]
    face_left = "GGGGGGGGG"
    face_right = "BBBBBBBBB"
    face_back = "RRRRRRRRR"
    face_bottom = "YYYYYYYYY"
    for color in face_left:
        faces[0].append(color)

    for color in face_right:
        faces[1].append(color)

    for color in face_back:
        faces[2].append(color)

    for color in face_bottom:
        faces[3].append(color)

    face_name = ["left", "right", "back", "bottom"]
    count = 0
    for face in faces:
        print(face_name[count])
        print_face(face)
        print("----------")
        count += 1

    print()
    print("rotating top clockwise now......")
    print()

    count = 0
    faces = rotate_clockwise(faces, "top", 2, True)

    for face in faces:
        print(face_name[count])
        print(face_name)
        print_face(face)
        print("----------")
        count+= 1


def print_pyramid(faces):
    face_name = ["left", "right", "back", "bottom"]
    count = 0
    for face in faces:
        print(face_name[count])
        print_face(face)
        print("----------")
        count += 1


def prompt_for_start_state():
    print("For this to work, make sure one of the pyraminx's base triangle's vertex is facing you")
    print("I will refer to the left face, right face, bottom face, and the face behind you")
    left_face_string = input("Enter colors on left face as a string")
    right_face_string = input("Enter colors on right face as a string")
    back_face_string = input("Enter colors on the back face as a string")
    bottom_face_string = input("Enter colors on the bottom face as a string")
    encodings = [left_face_string, right_face_string, back_face_string, bottom_face_string]
    faces = [[], [], [], []]
    for encoding_index in range(4):
        for color in encodings[encoding_index]:
            faces[encoding_index].append(color)

    return faces

def get_solved_state():
    colors = 'Y', 'B', 'G', 'R'
    faces = []
    for color in colors:
        faces.append([])
        for i in range(9):
            faces[len(faces) - 1].append(color)
    return faces


def rotate_clockwise(faces, vertex, type, regular=True):
    # if regular is set to true, a regular rotation on the passed in 'vertex' is performed. Define regular rotations as follows:
    # if vertex == "top", rotates top counterclockwise
    # if vertex == "front", rotates front counterclockwise
    # if vertex == "left", rotates left towards the person
    # if vertex == "right", rotates right towards the person

    # if regular is set to false, the opposite rotations for the passed in 'vertex' are performed

    # if type is 1, a corner rotation is performed. else, if type is set to 2, a centre rotation is performed
    faces = copy.deepcopy(faces)
    # corner rotation
    if type == 1:
        if vertex == "top":
            # rotate left or clockwise
            temp = faces[FACE_LEFT][0]
            faces[FACE_LEFT][0] = faces[FACE_RIGHT][0]
            faces[FACE_RIGHT][0] = faces[FACE_BACK][0]
            faces[FACE_BACK][0] = temp
        elif vertex == "left":
            # rotate towards you
            temp = faces[FACE_LEFT][4]
            faces[FACE_LEFT][4] = faces[FACE_BACK][8]
            faces[FACE_BACK][8] = faces[FACE_BOTTOM][4]
            faces[FACE_BOTTOM][4] = temp
        elif vertex == "right":
            # rotate towards you
            temp = faces[FACE_BOTTOM][8]
            faces[FACE_BOTTOM][8] = faces[FACE_RIGHT][8]
            faces[FACE_RIGHT][8] = faces[FACE_BACK][4]
            faces[FACE_BACK][4] = temp
        else:
            # front, rotate clockwise
            temp = faces[FACE_LEFT][8]
            faces[FACE_LEFT][8] = faces[FACE_BOTTOM][0]
            faces[FACE_BOTTOM][0] = faces[FACE_RIGHT][4]
            faces[FACE_RIGHT][4] = temp
        if not regular:
            # one more "regular" rotation if not regular
            faces = rotate_clockwise(faces, vertex, type)

        return faces

    # type 2, centre rotations
    if vertex == "top":
        # rotate_clockwise
        faces = rotate_clockwise(faces, "top", 1)
        positions_to_swap = [1, 2, 3]
        for position in positions_to_swap:
            temp = faces[FACE_LEFT][position]
            faces[FACE_LEFT][position] = faces[FACE_RIGHT][position]
            faces[FACE_RIGHT][position] = faces[FACE_BACK][position]
            faces[FACE_BACK][position] = temp

    elif vertex == "left":
        faces = rotate_clockwise(faces, "left", 1)
        temp1 = faces[FACE_LEFT][1]
        temp2 = faces[FACE_LEFT][5]
        temp3 = faces[FACE_LEFT][6]

        faces[FACE_LEFT][1] = faces[FACE_BACK][6]
        faces[FACE_LEFT][5] = faces[FACE_BACK][7]
        faces[FACE_LEFT][6] = faces[FACE_BACK][3]

        faces[FACE_BACK][6] = faces[FACE_BOTTOM][1]
        faces[FACE_BACK][7] = faces[FACE_BOTTOM][5]
        faces[FACE_BACK][3] = faces[FACE_BOTTOM][6]

        faces[FACE_BOTTOM][1] = temp1
        faces[FACE_BOTTOM][5] = temp2
        faces[FACE_BOTTOM][6] = temp3

    elif vertex == "right":
        faces = rotate_clockwise(faces, "right", 1)

        temp1 = faces[FACE_RIGHT][3]
        temp2 = faces[FACE_RIGHT][7]
        temp3 = faces[FACE_RIGHT][6]

        faces[FACE_RIGHT][3] = faces[FACE_BACK][6]
        faces[FACE_RIGHT][7] = faces[FACE_BACK][5]
        faces[FACE_RIGHT][6] = faces[FACE_BACK][1]

        faces[FACE_BACK][6] = faces[FACE_BOTTOM][3]
        faces[FACE_BACK][5] = faces[FACE_BOTTOM][7]
        faces[FACE_BACK][1] = faces[FACE_BOTTOM][6]

        faces[FACE_BOTTOM][6] = temp3
        faces[FACE_BOTTOM][3] = temp1
        faces[FACE_BOTTOM][7] = temp2

    else:
        faces = rotate_clockwise(faces, "front", 1)

        temp1 = faces[FACE_RIGHT][1]
        temp2 = faces[FACE_RIGHT][5]
        temp3 = faces[FACE_RIGHT][6]

        faces[FACE_RIGHT][1] = faces[FACE_LEFT][6]
        faces[FACE_RIGHT][5] = faces[FACE_LEFT][7]
        faces[FACE_RIGHT][6] = faces[FACE_LEFT][3]

        faces[FACE_LEFT][6] = faces[FACE_BOTTOM][3]
        faces[FACE_LEFT][3] = faces[FACE_BOTTOM][1]
        faces[FACE_LEFT][7] = faces[FACE_BOTTOM][2]

        faces[FACE_BOTTOM][3] = temp1
        faces[FACE_BOTTOM][2] = temp2
        faces[FACE_BOTTOM][1] = temp3

    # if the rotation is not regular, rotate again
    if not regular:
        faces = rotate_clockwise(faces, vertex, type)

    return faces


def is_solved(faces):
    # check if the pyraminx is solved
    for face in faces:
        for i in range(1, len(face)):
            if face[i] != face[i-1]:
                return False

    return True


def encoded_state(state):
    # given a pyraminx state, encode it as a string
    encoded_state = ''
    for row in state:
        for color in row:
            encoded_state += color
        encoded_state += '\n'

    return encoded_state

def main(start_state=None):
    moves_to_solved_state = ""
    if start_state is None:
        start_state = prompt_for_start_state()
    debug_start_state = copy.deepcopy(start_state)
    seen_states_to_actions = {encoded_state(start_state) : ''}
    bfs_queue = [start_state]
    actions = []
    vertices = ["top", "front", "left", "right"]

    # assume correct corner rotations are performed and corners are aligned
    for vertex in vertices:
        actions.append([vertex, 2, True])

    for vertex in vertices:
        actions.append([vertex, 2, False])

    number_of_actions = 0
    has_seen_solved_state = False
    while bfs_queue and not has_seen_solved_state:
        queue_size = len(bfs_queue)
        print(len(seen_states_to_actions), queue_size)
        for queue_index in range(queue_size):
            next_state = bfs_queue.pop(0)

            if is_solved(next_state):
                print("Got to a solved state in", number_of_actions, "actions.")
                print()
                moves_to_solved_state = seen_states_to_actions[encoded_state(next_state)]
                if IS_DEBUG_MODE:
                    pyramid_state_after_each_move(start_state, moves_to_solved_state)

                print_solution(moves_to_solved_state, debug_start_state)
                has_seen_solved_state = True
                break

            steps = seen_states_to_actions[encoded_state(next_state)]

            for action_index in range(len(actions)):
                action = actions[action_index]
                neighbor = rotate_clockwise(next_state, action[0], action[1], action[2])
                neighbor_encoding = encoded_state(neighbor)
                if neighbor_encoding not in seen_states_to_actions:
                    steps_for_neighbor = copy.deepcopy(steps)
                    steps_for_neighbor += str(action_index)
                    bfs_queue.append(neighbor)
                    seen_states_to_actions[neighbor_encoding] = steps_for_neighbor
        number_of_actions += 1


def pyramid_state_after_each_move(faces, moves):
    moves_to_vertex = {'0' : ["top", True], '1': ["front", True], '2': ["left", True], '3': ["right", True],
                       '4' : ["top", False], '5': ["front", False], '6': ["left", False], '7': ["right", False]
                       }
    for move in moves:
        print_pyramid(faces)
        print("-------------")
        print("next move is,", move, " with arr:", moves_to_vertex[move])
        faces = rotate_clockwise(faces, moves_to_vertex[move][0], 2, moves_to_vertex[move][1])

    print_pyramid(faces)


def print_solution(path, faces=None):
    print("To solve, please follow these moves:")
    for i in range(len(path)):
        print(i + 1, end='. ')
        if path[i] == '0':
            print("Top: Clockwise")
        elif path[i] == '1':
            print("Front: Clockwise")
        elif path[i] == '2':
            print("Left: Towards You")
        elif path[i] == '3':
            print("Right: Towards you")
        elif path[i] == '4':
            print("Top: Counterclockwise")
        elif path[i] == '5':
            print("Front: Counterclockwise")
        elif path[i] == '6':
            print("Left: Away from you")
        else:
            print("Right: Away from you")


if __name__ == "__main__":
    if IS_DEBUG_MODE:
        custom_state_tests()
    else:
        main()