Name:   Wenyu Fan
SID:    540409697
Unikey: wfan0971

**Test Cases**
Table 1. Summary of test cases for set_pulse_sequence
| File Name             | Function Name   | Description                                                      | Expected Error Message(s) (if any)                       | Pass/Fail |
| --------------------- | ----------------| -----------------------------------------------------------------| ---------------------------------------------------------| --------- |
| pulse_sequence.in     | positive_test_1 | Positive Case - configure the frequency for 3 emitters           | returns None                                             | Pass      |
| pulse_sequence_2.in   | positive_test_2 | Positive Case - configure the frequency for 3 emitters           | returns None                                             | Pass      |
| pulse_sequence_3.in   | negative_test_1 | Negative Case - 25.06 is a float value, not an integer           | prints "Error: frequency is not an integer"              | Pass      |
| pulse_sequence_4.in   | negative_test_2 | Negative Case - 9 is not a character                             | prints "Error: symbol is not between 'A' and 'J'"        | Pass      |
| pulse_sequence_5.in   | negative_test_3 | Negative Case - there should be exactly 3 tokens                 | prints "Error: <symbol> <frequency> <direction>"         | Pass      |
| pulse_sequence_6.in   | edge_test_1     | Edge Case - frequency shouldn't be equal to zero                 | prints "Error: frequency must be greater than zero"      | Pass      |
| pulse_sequence_7.in   | edge_test_2     | Edge Case - emitter 'A' already has its pulse sequence set       | prints "emitter 'A' already has its pulse sequence set"  | Pass      |
| pulse_sequence_8.in   | edge_test_3     | Edge Case - emitter 'E' does not exist                           | prints "Error: emitter 'E' does not exist                | Pass      |  
