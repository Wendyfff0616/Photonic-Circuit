# Photonic Circuit Simulator

A command-line Python simulator for building and running a simplified photonic circuit. The project models a circuit board with laser emitters, receivers, photons, and mirrors, then simulates how photons move through the board, reflect, get absorbed, and activate receivers over time.

This was originally developed for the INFO1110 programming assignment, then organized here as a compact object-oriented simulation project.

## Highlights

- Interactive circuit setup for board size, emitters, receivers, and optional mirrors.
- Input validation for component symbols, coordinates, board bounds, and pulse sequences.
- Photon movement simulation with nanosecond ticks.
- Mirror reflection behavior for `/`, `\`, `>`, `<`, `^`, and `v`.
- Receiver activation tracking, including activation time and absorbed energy.
- ASCII board rendering for visualizing the circuit state in the terminal.
- Output reports for emitted photons, receiver activation times, and total absorbed energy.

## Project Structure

| File | Purpose |
| --- | --- |
| `run.py` | CLI entry point. Builds the circuit, handles feature flags, and starts the simulation. |
| `laser_circuit.py` | Main simulation controller for components, photons, board updates, and reporting. |
| `emitter.py` | Defines laser emitters that produce photons from pulse sequences. |
| `photon.py` | Defines photon movement, absorption, and component interaction logic. |
| `receiver.py` | Defines receivers that absorb photon energy and record activation data. |
| `mirror.py` | Defines mirror reflection and absorption behavior. |
| `input_parser.py` | Validates user input for board size, components, mirrors, and pulse sequences. |
| `board_displayer.py` | Renders the circuit board as ASCII output. |
| `sorter.py` | Sorting helpers for emitters and receiver reports. |
| `test.py` | Test scaffold for pulse sequence behavior. |
| `test_plan.md` | Manual test plan and expected outcomes. |

## Requirements

- Python 3.10 or later
- No external Python packages required

## Quick Start

Clone the repository:

```bash
git clone https://github.com/fanwy16/Photonic-Circuit.git
cd Photonic-Circuit
```

Run the interactive circuit builder:

```bash
python3 run.py
```

Run with mirrors enabled:

```bash
python3 run.py -ADD-MY-MIRRORS
```

Run the full simulation:

```bash
python3 run.py -RUN-MY-CIRCUIT
```

Run the full simulation with mirrors:

```bash
python3 run.py -ADD-MY-MIRRORS -RUN-MY-CIRCUIT
```

## Input Format

The program prompts for circuit setup in this order.

### 1. Board Size

```text
<width> <height>
```

Example:

```text
20 8
```

### 2. Emitters

Emitters use symbols `A` to `J`.

```text
<symbol> <x> <y>
END EMITTERS
```

Example:

```text
A 2 2
B 8 1
C 15 6
END EMITTERS
```

### 3. Receivers

Receivers use symbols `R0` to `R9`.

```text
<symbol> <x> <y>
END RECEIVERS
```

Example:

```text
R0 2 6
R1 15 2
R2 6 1
END RECEIVERS
```

### 4. Mirrors

Mirrors are only requested when the `-ADD-MY-MIRRORS` flag is used. Supported symbols are `/`, `\`, `>`, `<`, `^`, and `v`.

```text
<symbol> <x> <y>
END MIRRORS
```

Example:

```text
/ 5 2
\ 10 4
END MIRRORS
```

## Pulse Sequence File

When `-RUN-MY-CIRCUIT` is enabled, the simulator reads pulse data from:

```text
/home/input/pulse_sequence.in
```

Each line configures one emitter:

```text
<emitter_symbol> <frequency_THz> <direction>
```

Directions must be one of `N`, `E`, `S`, or `W`.

Example:

```text
A 100 E
B 256 S
C 420 N
```

The simulation writes result files to `/home/output/`, following the original assignment environment convention:

- `/home/output/emit_photons.out`
- `/home/output/activation_times.out`
- `/home/output/total_energy.out`

For local development outside that environment, make sure `/home/input` and `/home/output` exist, or update the paths in `run.py` and `laser_circuit.py`.

## Example Session

```text
$ python3 run.py -ADD-MY-MIRRORS
Creating circuit board...
> 20 8
20x8 board created.

Adding emitter(s)...
> A 2 2
> B 8 1
> END EMITTERS
2 emitter(s) added.

Adding receiver(s)...
> R0 18 2
> R1 8 6
> END RECEIVERS
2 receiver(s) added.

<ADD-MY-MIRRORS FLAG DETECTED!>

Adding mirror(s)...
> / 10 2
> END MIRRORS
1 mirror(s) added.
```

The board is displayed in the terminal with components placed at their coordinates:

```text
+--------------------+
|                    |
|        B           |
|  A       /       0 |
|                    |
|                    |
|                    |
|        1           |
|                    |
+--------------------+
```

## Testing

The repository includes a test scaffold for `set_pulse_sequence`:

```bash
python3 test.py
```

The test script expects pulse sequence fixtures under `/home/input/`, matching the assignment runtime layout. See `test_plan.md` for the planned positive, negative, and edge cases.

## Design Notes

The simulator is intentionally small and explicit. Each circuit component owns its local behavior, while `LaserCircuit` coordinates the full simulation loop:

1. Emitters create photons from their configured pulse sequences.
2. Each clock tick moves active photons one cell in their current direction.
3. Collisions are resolved against emitters, receivers, and mirrors.
4. Receivers record activation time and accumulated energy.
5. The board and output reports are updated as the simulation progresses.

Although the theme is photonic computing, the project is a simplified programming model rather than a physically accurate optics simulator.

## License

This project is released under the MIT License. See `LICENSE` for details.
