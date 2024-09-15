import sorter
from emitter import Emitter
from receiver import Receiver
from photon import Photon
from mirror import Mirror
from board_displayer import BoardDisplayer

'''
Name:   Wenyu Fan

LaserCircuit - Responsible for storing all the components of the circuit and
handling the computation of running the circuit. It's responsible for delegating 
tasks to the specific components e.g. making each emitter emit a photon, getting 
each photon to move and interact with components, etc. In general, this class is
responsible for handling any task related to the circuit.

'''


class LaserCircuit:


    def __init__(self, width: int, height: int):
        '''        
        Initialise a LaserCircuit instance given a width and height. All 
        lists of components and photons are empty by default.
        board_displayer is initialised to a BoardDisplayer instance. clock is
        0 by default.

        emitters:        list[Emitter]  - all emitters in this circuit
        receivers:       list[Receiver] - all receivers in this circuit
        photons:         list[Photon]   - all photons in this circuit
        mirrors:         list[Mirror]   - all mirrors in this circuit
        width:           int            - the width of this circuit board
        height:          int            - the height of this circuit board
        board_displayer: BoardDisplayer - helper class for storing and 
                                          displaying the circuit board
        clock:           int            - a clock keeping track of how many 
                                          nanoseconds this circuit has run for

        Parameters
        ----------
        width  - the width to set this circuit board to
        height - the width to set this circuit board to
        '''
        self.emitters = []
        self.receivers = []
        self.photons = []
        self.mirrors = []
        self.width = width
        self.height = height
        self.board_displayer = BoardDisplayer(width, height)
        self.clock = 0


    def emit_photons(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Gets each emitter in this circuit's list of emitters to emit a photon.
        The photons emitted should be added to this circuit's photons list.
        '''
        i = 0
        while i < len(self.emitters):
            photon = self.emitters[i].emit_photon()
            self.photons.append(photon)
            i += 1


    def is_finished(self) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Returns whether or not this circuit has finished running. The
        circuit is finished running if every photon in the circuit has been
        absorbed.

        Returns
        -------
        True if the circuit has finished running or not, else False.
        '''
        i = 0
        while i < len(self.photons):
            if not self.photons[i].is_absorbed():
                return False
            i += 1
        return True


    def print_emit_photons(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for each emitter emitting a photon.
        
        It will also need to write the output into a
        /home/output/emit_photons.out output file. 
        
        You can assume the /home/output/ path exists.
        '''
        print("0ns: Emitting photons.")

        f = open("/home/output/emit_photons.out", "w")
        i = 0
        while i < len(self.emitters):
            emitter = self.emitters[i]
            output_str = emitter.__str__() + '\n'
            print(output_str.strip())
            f.write(output_str)
            i += 1
        f.close()


    def print_activation_times(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for the activation times for each receiver, sorted
        by activation time in ascending order. Any receivers that have not
        been activated should not be included.
        
        It will also need to write the output into a
        /home/output/activation_times.out output file.

        You can assume the /home/output/ path exists.
        '''
        print("\nActivation times:")
        
        activated_receivers = []
        i = 0
        while i < len(self.receivers):
            receiver = self.receivers[i]
            if receiver.is_activated():
                activated_receivers.append(receiver)
            i += 1

        sorted_receivers = sorter.sort_receivers_by_activation_time(activated_receivers)
        
        f = open("/home/output/activation_times.out", "w")
        i = 0
        while i < len(sorted_receivers):
            receiver_output = sorted_receivers[i]
            output_str = f"R{receiver_output.get_symbol()}: {receiver_output.get_activation_time()}ns\n"
            print(output_str.strip())
            f.write(output_str)
            i += 1
        f.close()


    def print_total_energy(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for the total energy absorbed for each receiver,
        sorted by total energy absorbed in descending order. Any receivers
        that have not been activated should not be included.
        
        It will also need to write the output into a
        /home/output/total_energy_absorbed.out output file.

        You can assume the /home/output/ path exists.
        '''
        print("\nTotal energy absorbed:")
        
        activated_receivers = []
        i = 0
        while i < len(self.receivers):
            receiver = self.receivers[i]
            if receiver.is_activated():
                activated_receivers.append(receiver)
            i += 1

        sorted_receivers = sorter.sort_receivers_by_total_energy(activated_receivers)

        f = open("/home/output/total_energy.out", "w")
        i = 0
        while i < len(sorted_receivers):
            receiver_output = sorted_receivers[i]
            output_str = receiver_output.__str__() + '\n'
            print(output_str.strip())
            f.write(output_str)
            i += 1
        f.close()

    
    def print_board(self) -> None:
        '''Calls the print_board method in board_displayer.'''
        self.board_displayer.print_board()


    def get_collided_emitter(self, entity: Emitter | Receiver | Photon | Mirror) -> Emitter | None:
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another emitter in the 
        circuit. 

        If it does, return the emitter already in the entity's position.
        Else, return None, indicating there is no emitter occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        An emitter if it has the same position as entity, else None.
        '''
        #remove the line below once you start implementing this function
        if entity is None:
            return None
        i = 0
        while i < len(self.emitters):
            if self.emitters[i].get_x() == entity.get_x() and self.emitters[i].get_y() == entity.get_y() and entity.get_symbol() != self.emitters[-1].get_symbol():
               return self.emitters[i]
            i += 1
        return None



    def get_collided_receiver(self, entity: Emitter | Receiver | Photon | Mirror) -> Receiver | None:
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another receiver in the 
        circuit. 

        If it does, return the receiver already in the entity's position.
        Else, return None, indicating there is no receiver occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        A receiver if it has the same position as entity, else None.
        '''
        #remove the line below once you start implementing this function
        if entity is None:
            return None

        i = 0
        while i < len(self.receivers):
            if self.receivers[i].get_x() == entity.get_x() and self.receivers[i].get_y() == entity.get_y() and entity.get_symbol() != self.receivers[-1].get_symbol():
               return self.receivers[i]
            i += 1
        return None


    def get_collided_mirror(self, entity: Emitter | Receiver | Photon | Mirror) -> Mirror | None:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another mirror in the 
        circuit. 

        If it does, return the mirror already in the entity's position.
        Else, return None, indicating there is no mirror occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        A mirror if it has the same position as entity, else None.
        '''
        #remove the line below once you start implementing this function
        if entity is None:
            return None
        
        i = 0
        while i < len(self.mirrors):
            if self.mirrors[i].get_x() == entity.get_x() and self.mirrors[i].get_y() == entity.get_y() and entity.get_symbol() != self.mirrors[-1].get_symbol():
                return self.mirrors[i]
            i += 1
        return None


    def get_collided_component(self, photon: Photon) -> Emitter | Receiver | Mirror | None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        # will require extensions in ADD-MY-MIRRORS
        '''
        Given a photon, returns the component it has collided with (if any).
        A collision occurs if the positions of photon and the component are
        the same.

        Parameters
        ----------
        photon - a photon to check for collision with the circuit's components

        Returns
        -------
        If the photon collided with a component, return that component.
        Else, return None.

        Hint
        ----
        Use the three collision methods above to handle this.
        '''
        collided_emitter = self.get_collided_emitter(photon)
        if collided_emitter is not None:
            return collided_emitter

        collided_receiver = self.get_collided_receiver(photon)
        if collided_receiver is not None:
            return collided_receiver

        collided_mirror = self.get_collided_mirror(photon)
        if collided_mirror is not None:
            return collided_mirror
        
        return None


    def tick(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Runs a single nanosecond (tick) of this circuit. If the circuit has
        already finished, this method should return out early.
        
        Otherwise, for each photon that has not been absorbed, this method is
        responsible for moving it, updating the board to show its new position
        and checking if it collided with a component (and handling it if did
        occur). At the end, we then increment clock.
        '''
        if self.is_finished():
            return

        self.clock += 1

        i = 0
        while i < len(self.photons):
            photon = self.photons[i]
            if not photon.is_absorbed():
                photon.move(self.width, self.height)
                self.board_displayer.add_photon_to_board(photon)
                
                component = self.get_collided_component(photon)
                if component is not None:
                    photon.interact_with_component(component, self.clock)
            
            i += 1
        

    def run_circuit(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Runs the entire circuit from start to finish. This involves getting
        each emitter to emit a photon, and continuously running tick until the
        circuit is finished running. All output in regards of running the 
        circuit should be contained in this method.
        '''
        print("\n========================")
        print("   RUNNING CIRCUIT...")
        print("========================\n")
        self.emit_photons()
        self.print_emit_photons()
        # this loop keeps running until the circuit is finished running
        if self.is_finished():
            print(f"\n0ns: 0/0 receiver(s) activated.")
            self.print_board() 

        while not self.is_finished():
            # TODO: call tick
            self.tick()
            # TODO: handle displaying receivers activated and board (if required)
            # HINT: you have a clock keep tracking of how many nanoseconds has passed
            if self.clock % 5 == 0 or self.is_finished():
                activated_receivers = []
                i = 0
                while i < len(self.receivers):
                    receiver = self.receivers[i]
                    if receiver.is_activated():
                        activated_receivers.append(receiver)
                    i += 1
                num_sorted = len(activated_receivers)
                num_self = len(self.receivers)
                print(f"\n{self.clock}ns: {num_sorted}/{num_self} receiver(s) activated.")
                self.board_displayer.print_board()

        # if we reach here (outside the loop), that means the circuit is finished running
        self.print_activation_times()
        self.print_total_energy()

        print("\n========================")
        print("   CIRCUIT FINISHED!")
        print("========================")
  
    def add_emitter(self, emitter: Emitter) -> bool:
        '''
        If emitter is not an Emitter instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The emitter's position is within the bounds of the circuit.
          2)  The emitter's position is not already taken by another emitter in
              the circuit.
          3)  The emitter's symbol is not already taken by another emitter in 
              the circuit.
          
        If at any point a check is not passed, an error message is printed
        stating the causeof the error and returns False, skipping any further
        checks. If all checks pass, then the following needs to occur:
          1)  emitter is added in the circuit's list of emitters. emitter
              needs to be added such that the list of emitters remains sorted
              in alphabetical order by the emitter's symbol. You can assume the
              list of emitters is already sorted before you add the emitter.
          2)  emitter's symbol is added into board_displayer.
          3)  The method returns True.   

        Paramaters
        ----------
        emitter - the emitter to add into this circuit's list of emitters

        Returns
        ----------
        Returns true if all checks are passed and the emitter is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.

        Hint
        ----
        Use the get_collided_emitter method to check for position collision.
        You will need to find your own way to check for symbol collisions
        with other emitters.
        '''
        if not isinstance(emitter, Emitter):
            return False

        if emitter.x < 0 or emitter.x >= self.width or emitter.y < 0 or emitter.y >= self.height:
            print(f"Error: position ({emitter.x}, {emitter.y}) is out-of-bounds of {self.width}x{self.height} circuit board")
            return False
        
        if self.get_collided_emitter(emitter) is not None:
            print(f"Error: position ({emitter.x}, {emitter.y}) is already taken by emitter '{self.get_collided_emitter(emitter).symbol}'")
            return False

        i = 0
        while i < len(self.emitters):
            if emitter.symbol == self.emitters[i].get_symbol():
                print(f"Error: symbol '{emitter.symbol}' is already taken")
                return False
            i += 1
        
        self.emitters.append(emitter)
        self.board_displayer.add_component_to_board(emitter)

        return True
      

    def get_emitters(self) -> list[Emitter]:
        '''Returns emitters.'''
        sorted_emitters = sorter.sort_emitters_by_symbol(self.emitters)
        return sorted_emitters

    
    def add_receiver(self, receiver: Receiver) -> bool:
        '''
        If receiver is not a Receiver instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The receiver's position is within the bounds of the circuit.
          2)  The receiver's position is not already taken by another emitter
              or receiver in the circuit.
          3)  The receiver's symbol is not already taken by another receiver in
              the circuit. 
             
        If at any point a check is not passed, an error message is printed stating
        the cause of the error and returns False, skipping any further checks. If 
        all checks pass, then the following needs to occur:
          1)  receiver is added in the circuit's list of receivers. receiver
              needs to be added such that the list of receivers  remains sorted
              in alphabetical order by the receiver's symbol. You can assume the
              list of receivers is already sorted before you add the receiver. 
          2)  receiver's symbol is added into board_displayer.
          3)  The method returns True.

        Paramaters
        ----------
        receiver - the receiver to add into this circuit's list of receivers

        Returns
        ----------
        Returns true if all checks are passed and the receiver is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.

        Hint
        ----
        Use the get_collided_emitter and get_collided_receiver methods to
        check for position collisions.
        You will need to find your own way to check for symbol collisions
        with other receivers.
        '''

        if not isinstance(receiver, Receiver):
            return False

        elif receiver.x < 0 or receiver.x >= self.width or receiver.y < 0 or receiver.y >= self.height:
            print(f"Error: position ({receiver.x}, {receiver.y}) is out-of-bounds of {self.width}x{self.height} circuit board")
            return False
        
        elif self.get_collided_receiver(receiver) is not None:
            print(f"Error: position ({receiver.x}, {receiver.y}) is already taken by receiver 'R{self.get_collided_receiver(receiver).symbol}'")
            return False

        elif self.get_collided_emitter(receiver) is not None:
            print(f"Error: position ({receiver.x}, {receiver.y}) is already taken by emitter '{self.get_collided_emitter(receiver).symbol}'")
            return False

        i = 0
        while i < len(self.receivers):
            if receiver.get_symbol() == self.receivers[i].get_symbol():
                print(f"Error: symbol '{receiver.symbol}' is already taken")
                return False
            i += 1

        self.receivers.append(receiver)
        self.board_displayer.add_component_to_board(receiver)

        return True


    def get_receivers(self) -> list[Receiver]:
        '''Returns receivers.'''
        sorted_receivers = sorter.sort_receivers_by_symbol(self.receivers)
        return sorted_receivers


    def add_photon(self, photon: Photon) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        If the photon passed in is not a Photon instance, it does not add it in
        and returns False. Else, it adds photon in this circuit's list of
        photons and returns True.

        Paramaters
        ----------
        photon - the photon to add into this circuit's list of photons

        Returns
        -------
        Returns True if the photon is added in, else False.
        '''
        if not isinstance(photon, Photon):
            return False
    
        self.photons.append(photon)
        return True


    def get_photons(self) -> list[Photon]:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns photons.'''
        return self.photons


    def add_mirror(self, mirror: Mirror) -> bool:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''
        If mirror is not a Mirror instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The mirror's position is within the bounds of the circuit.
          2)  The mirror's position is not already taken by another emitter, 
              receiver or mirror in the circuit.
             
        If at any point a check is not passed, an error message is printed
        stating the cause of theerror and returns False, skipping any further
        checks. If all checks pass, then the following needs to occur: 
          1)  mirror is added in the circuit's list of mirrors.
          2) mirror's symbol is added into board_displayer.
          3)   The method returns True.

        Paramaters
        ----------
        mirror - the mirror to add into this circuit's list of mirrors

        Returns
        ----------
        Returns true if all checks are passed and the mirror is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.
        '''
        if not isinstance(mirror, Mirror):
            return False

        elif mirror.x < 0 or mirror.x >= self.width or mirror.y < 0 or mirror.y >= self.height:
            print(f"Error: position ({mirror.x}, {mirror.y}) is out-of-bounds of {self.width}x{self.height} circuit board")
            return False
        
        elif self.get_collided_mirror(mirror) is not None:
            print(f"Error: position ({mirror.x}, {mirror.y}) is already taken by mirror '{self.get_collided_mirror(mirror).symbol}'")
            return False

        elif self.get_collided_emitter(mirror) is not None:
            print(f"Error: position ({mirror.x}, {mirror.y}) is already taken by emitter '{self.get_collided_emitter(mirror).symbol}'")
            return False

        elif self.get_collided_receiver(mirror) is not None:
            print(f"Error: position ({mirror.get_x()}, {mirror.get_y()}) is already taken by receiver '{self.get_collided_receiver(mirror).get_symbol()}'")
            return False

        self.mirrors.append(mirror)
        self.board_displayer.add_component_to_board(mirror)

        return True


    def get_mirrors(self) -> list[Mirror]:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''Returns mirrors.'''
        return self.mirrors

    
    def get_width(self) -> int:
        '''Returns width.'''
        return self.width


    def get_height(self) -> int:
        '''Returns height.'''
        return self.height
