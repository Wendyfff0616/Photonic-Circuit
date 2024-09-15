from laser_circuit import LaserCircuit
from circuit_for_testing import get_my_lasercircuit
from run import set_pulse_sequence

'''
Name:   Wenyu Fan

This test program checks if the set_pulse_sequence function is implemented
correctly.

You can modify this scaffold as needed (changing function names, parameters, 
or implementations...), however, DO NOT ALTER the code in circuit_for_testing 
file, which provides the circuit. The circuit can be retrieved by calling 
get_my_lasercircuit(), and it should be used as an argument for the 
set_pulse_sequence function when testing.

Make sure to create at least six functions for testing: two for positive cases,
two for negative cases, and two for edge cases. Each function should take
different input files.

NOTE: Whenever we use ... in the code, this is a placeholder for you to
replace it with relevant code.
'''


def positive_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Positive test case to verify the set_pulse_sequence function.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)

    # TODO: Check if emitters' pulse sequence are correctly set up
    flag = True #it is a symbol which shows whether the emitters's pulse sequence are correctly set up
    wrong = ""
    # check if all the emitters in the given circuit has been set pulse set_pulse_sequence
    i = 0
    while i < len(my_circuit.emitters):
        if not my_circuit.emitters[i].is_pulse_sequence_set():
            print("Failed! At least one emitter's pulse sequence hasn't been set up!")
            return
        i += 1

    # check if freguency and direction of all the emitters in the given circuit has been set up correctly
    emitter_1 = my_circuit.emitters[0]
    if emitter_1.symbol != "A" or emitter_1.frequency != 100 or emitter_1.direction != 'E':
        flag = False
        wrong += emitter_1.symbol

    emitter_2 = my_circuit.emitters[1]
    if emitter_2.symbol != "B" or emitter_2.frequency != 256 or emitter_2.direction != 'S':
        flag = False
        wrong += emitter_2.symbol

    emitter_3 = my_circuit.emitters[2]
    if emitter_3.symbol != "C" or emitter_3.frequency != 420 or emitter_3.direction != 'N':
        flag = False
        wrong += emitter_3.symbol
    
    try:
        assert flag
    except AssertionError:
        print(f"Failed! Emitter(s):{wrong}'s pulse sequence has been set with wrong values!")
        return
    
    print("Positive Test 1 passed!\n")
    # don't forget to close the file
    file_obj.close()


def positive_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)

    flag = True
    wrong = ""
    i = 0
    while i < len(my_circuit.emitters):
        if not my_circuit.emitters[i].is_pulse_sequence_set():
            print("Failed! At least one emitter's pulse sequence hasn't been set up!")
            return
        i += 1

    emitter_1 = my_circuit.emitters[0]
    if emitter_1.symbol != "A" or emitter_1.frequency != 90 or emitter_1.direction != 'S':
        flag = False
        wrong += emitter_1.symbol

    emitter_2 = my_circuit.emitters[1]
    if emitter_2.symbol != "B" or emitter_2.frequency != 70 or emitter_2.direction != 'E':
        flag = False
        wrong += emitter_2.symbol

    emitter_3 = my_circuit.emitters[2]
    if emitter_3.symbol != "C" or emitter_3.frequency != 70 or emitter_3.direction != 'S':
        flag = False
        wrong += emitter_3.symbol
    
    try:
        assert flag
    except AssertionError:
        print(f"Failed! Emitter(s):{wrong}'s pulse sequence has been set with wrong values!")
        return
    print("Positive Test 2 passed!\n")
    file_obj.close()

def negative_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    file_obj = open(pulse_file_path)
    try:
        set_pulse_sequence(my_circuit, file_obj)  
    except TypeError as e:
        expected = "'NoneType' object is not subscriptable"
        assert str(e) == expected, "Negative Test 1 failed."
        print("Negative Test 1 passed!\n")
    file_obj.close()

def negative_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    file_obj = open(pulse_file_path)
    try:
        set_pulse_sequence(my_circuit, file_obj)
    except TypeError as e:
        expected = "'NoneType' object is not subscriptable"
        assert str(e) == expected, "Negative Test 2 failed."
        print("Negative Test 2 passed!\n")
    file_obj.close()

def negative_test_3(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    file_obj = open(pulse_file_path)
    try:
        set_pulse_sequence(my_circuit, file_obj)  
    except TypeError as e:
        expected = "'NoneType' object is not subscriptable"
        assert str(e) == expected, "Negative Test 3 failed because incorrect error message was raised"
        print("Negative Test 3 passed!\n")
    except:
        assert False, "Negative Test 3 failed because incorrect exception was raised"
        return
    file_obj.close()

def edge_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    file_obj = open(pulse_file_path)
    try:
        set_pulse_sequence(my_circuit, file_obj)  
    except TypeError as e:
        expected = "'NoneType' object is not subscriptable"
        assert str(e) == expected, "Edge Test 1 failed because incorrect error message was raised"
        print("Edge Test 1 passed!\n")
    except:
        assert False, "Edge Test 1 failed because incorrect exception was raised"
        return
    file_obj.close()

def edge_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    file_obj = open(pulse_file_path)
    actual = set_pulse_sequence(my_circuit, file_obj)
    expected = None
    assert actual == expected, "Edge Test 2 failed because incorrect error message was raised"
    print("Edge Test 2 passed!\n")
    file_obj.close()

def edge_test_3(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    file_obj = open(pulse_file_path)
    actual = set_pulse_sequence(my_circuit, file_obj) 
    expected = None 
    assert actual == expected, "Edge Test 3 failed because incorrect error message was raised"
    print("Edge Test 3 passed!\n")
    file_obj.close()

if __name__ == '__main__':
    # Run each function for testing
    positive_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence.in')
    positive_test_2(get_my_lasercircuit(), '/home/input/pulse_sequence_2.in')
    # You should have more below...
    negative_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence_3.in')
    negative_test_2(get_my_lasercircuit(), '/home/input/pulse_sequence_4.in')
    negative_test_3(get_my_lasercircuit(), '/home/input/pulse_sequence_5.in')
    edge_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence_6.in')
    edge_test_2(get_my_lasercircuit(), '/home/input/pulse_sequence_7.in')
    edge_test_3(get_my_lasercircuit(), '/home/input/pulse_sequence_8.in')

