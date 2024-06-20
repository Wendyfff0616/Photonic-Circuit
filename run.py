import sys
import input_parser
from emitter import Emitter
from receiver import Receiver
from mirror import Mirror
from laser_circuit import LaserCircuit


'''
Name:   Wenyu Fan
SID:    540409697
Unikey: wfan0971

run - Runs the entire program. It needs to take in the inputs and process them
into setting up the circuit. The user can specify optional flags to perform
additional steps, such as -RUN-MY-CIRCUIT to run the circuit and -ADD-MY-MIRRORS
to include mirrors in the circuit.

You are free to add more functions, as long as you aren't modifying the
existing scaffold.
'''


def is_run_my_circuit_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Returns whether or not '-RUN-MY-CIRCUIT' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    i = 0
    while i < len(args):
        if args[i] == '-RUN-MY-CIRCUIT':
            return True
        else:
            i += 1
    return False



def is_add_my_mirrors_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Returns whether or not '-ADD-MY-MIRRORS' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    i = 0
    while i < len(args):
        if args[i] == '-ADD-MY-MIRRORS':
            return True
        else:
            i += 1
    return False


def initialise_circuit() -> LaserCircuit:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Gets the inputs for the board size, emitters and receivers and processes
    it to create a LaserCircuit instance and return it. You should be using
    the functions you have implemented in the input_parser module to handle
    validating each input.

    Returns
    -------
    A LaserCircuit instance with a width and height specified by the user's
    inputted size. The circuit should also include each emitter and receiver
    the user has inputted.
    '''
    print("Creating circuit board...")
    while True:
        size_input = input("> ")
        board_size = input_parser.parse_size(size_input)
        if board_size is not None:
            break
    print(f"{board_size[0]}x{board_size[1]} board created.\n")

    width, height = board_size
    circuit = LaserCircuit(width, height)

    emitter_count = 0
    print("Adding emitter(s)...")
    while emitter_count <= 10:
        if emitter_count == 10:
            break
        emitter_input = input("> ")
        if emitter_input == 'END EMITTERS':
            break
        emitter = input_parser.parse_emitter(emitter_input)
        if emitter is not None:
            if circuit.add_emitter(emitter):
                emitter_count += 1
    print(f"{emitter_count} emitter(s) added.\n")

    receiver_count = 0
    print("Adding receiver(s)...")
    while receiver_count <= 10:
        if receiver_count == 10:
            break
        receiver_input = input("> ")
        if receiver_input == 'END RECEIVERS':
            break
        receiver = input_parser.parse_receiver(receiver_input)
        if receiver is not None:
            if circuit.add_receiver(receiver):
                    receiver_count += 1
    print(f"{receiver_count} receiver(s) added.\n")

    return circuit


def set_pulse_sequence(circuit: LaserCircuit, file_obj) -> None:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Handles setting the pulse sequence of the circuit. 
    The lines for the pulse sequence will come from the a file named
    /home/input/<file_name>.in. 
    You should be using the functions you have implemented in the input_parser module 
    to handle validating lines from the file.

    Parameter
    ---------
    circuit - The circuit to set the pulse sequence for.
    file_obj - A file like object returned by the open()
    '''
    print("Setting pulse sequence...")
    symbol_with_pulse_sequence = []

    sequence_count = 1
    while True:
        line = file_obj.readline()
        line = line.strip()

        if line.rstrip() == "":
            print("Pulse sequence set.")
            break

        i = 0
        emitters_not_set = ""
        while i < len(circuit.emitters):
            if not circuit.emitters[i].is_pulse_sequence_set():
                emitters_not_set += circuit.emitters[i].symbol + ", "
            i += 1
        emitters_not_set = emitters_not_set.rstrip(", ")

        if emitters_not_set == "":
            print("Pulse sequence set.")
            break

        print(f"-- ({emitters_not_set})")

        print(f"Line {sequence_count}: {line}")

        parts = input_parser.parse_pulse_sequence(line)
        
        symbol = parts[0]
        frequency = parts[1]
        direction = parts[2]

        i = 0
        found = False
        while i < len(circuit.emitters):
            if symbol == circuit.emitters[i].symbol:
                 found = True
                 break
            i += 1
        if found == False:
            print(f"Error: emitter '{symbol}' does not exist")
            sequence_count += 1
            continue

        i = 0
        found = False
        while i < len(symbol_with_pulse_sequence):
            if symbol == symbol_with_pulse_sequence[i]:
                found = True
                break
            i += 1
        if found == True:
            print(f"Error: emitter '{symbol}' already has its pulse sequence set")
            sequence_count += 1
            continue

        symbol_with_pulse_sequence.append(symbol)
        i = 0
        while i < len(circuit.emitters):
            if symbol == circuit.emitters[i].symbol:
                circuit.emitters[i].frequency = frequency
                circuit.emitters[i].direction = direction
                circuit.emitters[i].pulse_sequence_set = True
            i += 1
        
        sequence_count += 1
        
    


def add_mirrors(circuit: LaserCircuit) -> None:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Handles adding the mirrors into the circuit. You should be using the
    functions you have implemented in the input_parser module to handle
    validating each input. 
    
    Parameters
    ----------
    circuit - the laser circuit to add the mirrors into
    '''
    print("Adding mirror(s)...")
    mirror_count = 0
    add = True
    while add == True:
        user_input = input("> ")
        if user_input == 'END MIRRORS':
            print(f"{mirror_count} mirror(s) added.")
            add = False
            break
        mirror = input_parser.parse_mirror(user_input)
        if mirror is not None:
            if circuit.add_mirror(mirror) == True:
                mirror_count += 1



def main(args: list[str]) -> None:
    # only requires implementation once you reach GET-MY-INPUTS
    # will require extensions in RUN-MY-CIRCUIT and ADD-MY-MIRRORS
    '''
    Responsible for running all code related to the program.

    Parameters
    ----------
    args - the command line arguments of the program
    '''

    #remove the line below once you start implementing this function
    circuit = initialise_circuit()

    if is_add_my_mirrors_enabled(args):
        print("<ADD-MY-MIRRORS FLAG DETECTED!>\n")
        add_mirrors(circuit)
        print()
        circuit.print_board()
        print()
    else:
        circuit.print_board()
        print()

    if is_run_my_circuit_enabled(args):
        print("<RUN-MY-CIRCUIT FLAG DETECTED!>\n")
        pulse_file_path = '/home/input/pulse_sequence.in'
        try:
            pulse_file = open(pulse_file_path, 'r')
            set_pulse_sequence(circuit, pulse_file)
            pulse_file.close()
            circuit.run_circuit()
        except FileNotFoundError:
            print("Error: -RUN-MY-CIRCUIT flag detected but /home/input/pulse_sequence.in does not exist")
            return 
    
    

if __name__ == '__main__':
    '''
    Entry point of program. We pass the command line arguments to our main
    program. We do not recommend modifying this.
    '''
    main(sys.argv)
