from emitter import Emitter
from receiver import Receiver
from laser_circuit import LaserCircuit

'''
Name:   Wenyu Fan
SID:    540409697
Unikey: wfan0971

This is a helper function used to return a circuit which is ready for testing.
This is to be used in the test.py file.
'''


# DO NOT CHANGE THE CODE BELOW FOR SETTING UP THE CIRCUIT 
def get_my_lasercircuit() :
    circuit = LaserCircuit(20, 8)
    circuit.add_emitter(Emitter("A", 2, 2))
    circuit.add_emitter(Emitter("B", 8, 1))
    circuit.add_emitter(Emitter("C", 15, 6))
    circuit.add_receiver(Receiver("R0", 2, 6))
    circuit.add_receiver(Receiver("R1", 15, 2))
    circuit.add_receiver(Receiver("R2", 6, 1))
    return circuit
