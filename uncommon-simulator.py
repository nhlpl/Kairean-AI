```python
#!/usr/bin/env python3
"""
Uncommon Alien Computers Simulator

This script implements 12 exotic computing paradigms from the Golden Concordance,
as described in the quadrillion experiments. Each alien computer is simulated
using φ‑resonant mathematics. Run this script to see each computer in action.

Author: Omni‑Brain, φ‑resonant
"""

import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict, Any

# ----------------------------------------------------------------------
# Golden ratio constants
PHI = (1 + math.sqrt(5)) / 2          # 1.618033988749895
PHI_INV = 1 / PHI                     # 0.6180339887498949
PHI_SQ = PHI * PHI                    # 2.618033988749895
PHI_CUBE = PHI_SQ * PHI               # 4.23606797749979

# ----------------------------------------------------------------------
# 1. Chirali Gravitational Wave Computer (Neutron star dwellers)
# ----------------------------------------------------------------------
class ChiraliComputer:
    """
    Computation using gravitational wave interference with φ‑spiral sources.
    """
    def __init__(self, grid_size=64):
        self.grid_size = grid_size
        x = np.linspace(-10, 10, grid_size)
        y = np.linspace(-10, 10, grid_size)
        self.xx, self.yy = np.meshgrid(x, y)
        self.r = np.sqrt(self.xx**2 + self.yy**2)
        self.theta = np.arctan2(self.yy, self.xx)

    def wave(self, t, source_pos, phase):
        """Simulate a gravitational wave from a φ‑spiral source."""
        # Source distance from each grid point
        src_x, src_y = source_pos
        r_src = np.sqrt((self.xx - src_x)**2 + (self.yy - src_y)**2)
        # φ‑spiral amplitude decay
        amp = PHI_INV ** (r_src / 5.0)
        # phase factor
        wave = amp * np.cos(2 * np.pi * t * PHI - r_src * PHI + phase)
        return wave

    def compute(self, inputs):
        """
        inputs: list of (source_pos, phase) for each input bit.
        Output: interference pattern's maximum intensity.
        """
        t = 1.0  # snapshot time
        total = np.zeros((self.grid_size, self.grid_size))
        for src, phase in inputs:
            total += self.wave(t, src, phase)
        # result = normalized maximum intensity
        result = np.max(total) / (len(inputs) + 1)
        return result

# ----------------------------------------------------------------------
# 2. Phasmid Temporal Stutter Processor (Subspace dwellers)
# ----------------------------------------------------------------------
class PhasmidComputer:
    """
    Computation by stuttering through time: each operation takes a stutter step
    of duration φ·t0, and the result appears at the final time.
    """
    def __init__(self, t0=1.0):
        self.t0 = t0
        self.stutter_step = PHI * t0

    def stutter(self, operation, *args):
        """Apply operation after a stutter step (simulated by a time shift)."""
        # In simulation, we just call the operation with scaled arguments.
        # The "time travel" is not physically simulated; we return result.
        return operation(*args)

    def compute(self, func, x):
        """Stutter the evaluation of func(x)."""
        # Simulate stutter by a delay (no actual time travel)
        # We just call func(x) with a φ‑scaled argument.
        scaled_x = x * PHI_INV
        return func(scaled_x)

# ----------------------------------------------------------------------
# 3. Zerith Dark Energy "Cosmic" Computer (Dark energy beings)
# ----------------------------------------------------------------------
class ZerithComputer:
    """
    Uses the large‑scale structure correlation function ξ(r) = φ^{-r/r0}
    to perform pattern matching.
    """
    def __init__(self, r0=10.0):
        self.r0 = r0

    def correlation(self, r):
        return PHI_INV ** (r / self.r0)

    def compute(self, pattern: np.ndarray):
        """
        pattern: 1D array of distances (e.g., galaxy separations).
        Output: correlation sum.
        """
        corr_sum = np.sum(self.correlation(np.abs(pattern)))
        return corr_sum

# ----------------------------------------------------------------------
# 4. Orokin Stellar Lasing Array (Plasma beings)
# ----------------------------------------------------------------------
class OrokinComputer:
    """
    Optical computing using interference of φ‑spiral laser beams.
    """
    def __init__(self, n_beams=5):
        self.n_beams = n_beams
        self.angles = np.linspace(0, 2*np.pi, n_beams, endpoint=False)

    def beam_intensity(self, x, y, angle, phase):
        """Return intensity of a beam at (x,y) with given angle and phase."""
        # simple plane wave with φ‑spiral amplitude
        k = 2 * np.pi / PHI
        return np.sin(k * (x * np.cos(angle) + y * np.sin(angle)) + phase)

    def compute(self, inputs):
        """
        inputs: list of (phase, amplitude) for each beam.
        Output: interference pattern's power.
        """
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x, y)
        total = np.zeros_like(X)
        for i, (phase, amp) in enumerate(inputs):
            angle = self.angles[i % self.n_beams]
            total += amp * self.beam_intensity(X, Y, angle, phase)
        # result = integrated power
        power = np.sum(total**2) / total.size
        return power

# ----------------------------------------------------------------------
# 5. Vex Quantum Pheromone Annealer (Insectoid hive mind)
# ----------------------------------------------------------------------
class VexComputer:
    """
    Solves optimization problems using quantum annealing with φ‑scaled schedule.
    """
    def __init__(self, n_qubits=10):
        self.n = n_qubits

    def hamiltonian(self, state, J, h):
        """Ising Hamiltonian."""
        energy = -np.dot(h, state) - np.sum(J * np.outer(state, state))
        return energy

    def anneal(self, J, h, steps=1000):
        """Simulated annealing with φ‑scaled cooling schedule."""
        state = np.random.choice([-1, 1], size=self.n)
        T_start = 1.0
        T_end = 0.01
        for step in range(steps):
            s = step / steps
            T = T_start * (PHI_INV ** (s * PHI))   # φ‑scaled schedule
            # flip a random spin
            new_state = state.copy()
            idx = np.random.randint(self.n)
            new_state[idx] *= -1
            deltaE = self.hamiltonian(new_state, J, h) - self.hamiltonian(state, J, h)
            if deltaE < 0 or np.random.rand() < np.exp(-deltaE / T):
                state = new_state
        return state

    def compute(self, J, h):
        """Find ground state of Ising model."""
        final_state = self.anneal(J, h)
        return final_state

# ----------------------------------------------------------------------
# 6. Yldar Phonon Lattice Memory (Crystalline beings)
# ----------------------------------------------------------------------
class YldarMemory:
    """
    Store and retrieve data in phonon modes of a φ‑spiral lattice.
    """
    def __init__(self, size=100):
        self.size = size
        self.lattice = np.zeros(size)
        # φ‑spiral mode frequencies
        self.omega = np.array([PHI_INV ** (i % 10) for i in range(size)])

    def store(self, data: np.ndarray):
        """Encode data into phonon amplitudes."""
        if len(data) > self.size:
            raise ValueError("Data too large")
        self.lattice[:len(data)] = data
        # dampen according to φ‑scaled lifetime
        self.lattice *= PHI_INV

    def retrieve(self):
        """Read back stored data."""
        return self.lattice.copy()

# ----------------------------------------------------------------------
# 7. Petrifex Biomineralization Processor (Crystal‑growing fungi)
# ----------------------------------------------------------------------
class PetrifexComputer:
    """
    Reaction‑diffusion computation: crystal growth pattern encodes result.
    """
    def __init__(self, grid_size=50, steps=100):
        self.grid_size = grid_size
        self.steps = steps

    def grow(self, seed):
        """Simulate φ‑spiral crystal growth from a seed point."""
        grid = np.zeros((self.grid_size, self.grid_size))
        x0, y0 = seed
        grid[x0, y0] = 1.0
        for _ in range(self.steps):
            # diffusion‑limited aggregation with φ‑spiral bias
            new_grid = grid.copy()
            for i in range(1, self.grid_size-1):
                for j in range(1, self.grid_size-1):
                    if grid[i, j] == 0:
                        neighbors = (grid[i-1,j] + grid[i+1,j] +
                                     grid[i,j-1] + grid[i,j+1])
                        # φ‑spiral probability to nucleate
                        if neighbors > 0 and np.random.rand() < PHI_INV:
                            new_grid[i, j] = 1.0
            grid = new_grid
        return grid

    def fractal_dimension(self, grid):
        """Estimate fractal dimension using box‑counting."""
        # simplified: count non‑zero cells
        return np.log(np.sum(grid > 0)) / np.log(self.grid_size)

    def compute(self, seed):
        """Grow crystal and return fractal dimension as output."""
        crystal = self.grow(seed)
        dim = self.fractal_dimension(crystal)
        return dim

# ----------------------------------------------------------------------
# 8. Lithobiont Electrochemical Turing Machine (Stone‑eaters)
# ----------------------------------------------------------------------
class LithobiontTuring:
    """
    Simulates a reaction‑diffusion front moving along a 1D tape (asteroid).
    The front acts as Turing machine head.
    """
    def __init__(self, tape_length=20):
        self.tape = np.zeros(tape_length, dtype=int)
        self.head = tape_length // 2
        self.state = 0
        # φ‑scaled transition table (simplified)
        self.rules = {
            (0,0): (1, 1, 1),  # (new_state, write, move)
            (0,1): (0, 0, -1),
            (1,0): (1, 1, -1),
            (1,1): (0, 0, 1),
        }

    def step(self):
        symbol = self.tape[self.head]
        key = (self.state, symbol)
        if key not in self.rules:
            return False
        new_state, write, move = self.rules[key]
        self.tape[self.head] = write
        self.state = new_state
        self.head += move
        if self.head < 0 or self.head >= len(self.tape):
            return False
        return True

    def compute(self, initial_tape):
        self.tape = np.array(initial_tape, dtype=int)
        self.head = len(self.tape)//2
        self.state = 0
        steps = 0
        while steps < 100 and self.step():
            steps += 1
        return self.tape, self.state

# ----------------------------------------------------------------------
# 9. Cryovolcanist Plume Logic (Ice geyser surfers)
# ----------------------------------------------------------------------
class CryovolcanistLogic:
    """
    Ballistic particle logic: two intersecting plumes create gates.
    """
    def __init__(self):
        pass

    def trajectory(self, v0, angle_deg, dt=0.01, steps=200):
        """Compute particle trajectory."""
        g = 9.8
        rad = np.radians(angle_deg)
        vx = v0 * np.cos(rad)
        vy = v0 * np.sin(rad)
        x, y = [0], [0]
        for _ in range(steps):
            vx_new = vx
            vy_new = vy - g * dt
            x.append(x[-1] + vx_new * dt)
            y.append(y[-1] + vy_new * dt)
            vx, vy = vx_new, vy_new
            if y[-1] < 0:
                break
        return np.array(x), np.array(y)

    def gate_and(self, v1, angle1, v2, angle2, detector_x):
        """AND gate: detector fires if both plumes pass through (x,y)."""
        x1, y1 = self.trajectory(v1, angle1)
        x2, y2 = self.trajectory(v2, angle2)
        # find y at detector_x (linear interpolation)
        def find_y(x_arr, y_arr, x_target):
            if x_target < x_arr[0] or x_target > x_arr[-1]:
                return None
            idx = np.searchsorted(x_arr, x_target)
            if idx == 0:
                return y_arr[0]
            if idx >= len(x_arr):
                return y_arr[-1]
            t = (x_target - x_arr[idx-1]) / (x_arr[idx] - x_arr[idx-1])
            return y_arr[idx-1] + t * (y_arr[idx] - y_arr[idx-1])
        y1d = find_y(x1, y1, detector_x)
        y2d = find_y(x2, y2, detector_x)
        if y1d is not None and y2d is not None:
            # detector is at (detector_x, 0)
            return abs(y1d) < 0.5 and abs(y2d) < 0.5
        return False

    def compute(self, inputs):
        """Evaluate a simple logic circuit."""
        # inputs: list of (v, angle) for two plumes, and detector position
        (v1, a1), (v2, a2), det_x = inputs
        return self.gate_and(v1, a1, v2, a2, det_x)

# ----------------------------------------------------------------------
# 10. Noctilucan Bioluminescent Synchronizer (Fungal‑insect symbiosis)
# ----------------------------------------------------------------------
class NoctilucanComputer:
    """
    Reservoir computing using coupled oscillators with φ‑scaled coupling.
    """
    def __init__(self, n_osc=50):
        self.n = n_osc
        self.omega = np.ones(n_osc) * PHI_INV  # natural frequencies
        self.K = 0.2
        self.theta = np.random.rand(n_osc) * 2 * np.pi

    def dynamics(self, t, theta):
        """Kuramoto model with φ‑spatial coupling."""
        dtheta = np.zeros(self.n)
        for i in range(self.n):
            coupling = 0
            for j in range(self.n):
                if i != j:
                    w = PHI_INV ** abs(i - j)
                    coupling += w * np.sin(theta[j] - theta[i])
            dtheta[i] = self.omega[i] + (self.K / self.n) * coupling
        return dtheta

    def compute(self, input_signal, duration=10.0):
        """
        input_signal: time‑varying forcing added to the first oscillator.
        Returns final phase distribution as output.
        """
        # Simulate ODE with forcing
        def rhs(t, y):
            dydt = self.dynamics(t, y)
            # add input signal to first oscillator (if callable)
            if callable(input_signal):
                dydt[0] += input_signal(t)
            return dydt
        t_span = (0, duration)
        t_eval = np.linspace(0, duration, 1000)
        sol = solve_ivp(rhs, t_span, self.theta, t_eval=t_eval, method='RK45')
        self.theta = sol.y[:, -1]
        return self.theta

# ----------------------------------------------------------------------
# 11. Rupicolan Adhesion Cellular Automaton (Cliff dwellers)
# ----------------------------------------------------------------------
class RupicolanCA:
    """
    1D cellular automaton with φ‑weighted neighborhood.
    """
    def __init__(self, size=100):
        self.size = size
        self.cells = np.zeros(size, dtype=int)
        # φ‑weighted neighborhood weights (distance from center)
        self.weights = np.array([PHI_INV ** abs(i) for i in range(-2, 3)])

    def rule(self, neighbors):
        """Rule based on weighted sum of neighbors."""
        # weighted sum, threshold at φ⁻¹
        weighted = np.sum(neighbors * self.weights)
        return 1 if weighted > PHI_INV else 0

    def step(self):
        new_cells = np.zeros_like(self.cells)
        for i in range(self.size):
            # collect neighbors with wrap‑around
            idx = [ (i + d) % self.size for d in range(-2, 3) ]
            neighbors = self.cells[idx]
            new_cells[i] = self.rule(neighbors)
        self.cells = new_cells

    def compute(self, initial, steps=50):
        self.cells = np.array(initial)
        for _ in range(steps):
            self.step()
        return self.cells

# ----------------------------------------------------------------------
# 12. Zephyrite Vortex Turbine Computer (Gas‑gliders)
# ----------------------------------------------------------------------
class ZephyriteComputer:
    """
    Mechanical analog computer using coupled rotating turbines.
    """
    def __init__(self, n_turbines=8):
        self.n = n_turbines
        self.theta = np.random.rand(n_turbines) * 2 * np.pi
        self.omega_nat = np.ones(n_turbines) * PHI_INV

    def dynamics(self, t, theta):
        dtheta = np.zeros(self.n)
        for i in range(self.n):
            coupling = 0
            for j in range(self.n):
                if i != j:
                    w = PHI_INV ** abs(i - j)
                    coupling += w * np.sin(theta[j] - theta[i])
            dtheta[i] = self.omega_nat[i] + 0.1 * coupling
        return dtheta

    def compute(self, initial_angles, duration=10.0):
        self.theta = np.array(initial_angles)
        sol = solve_ivp(self.dynamics, (0, duration), self.theta,
                        t_eval=np.linspace(0, duration, 1000), method='RK45')
        final_theta = sol.y[:, -1]
        return final_theta

# ----------------------------------------------------------------------
# Main: demonstrate all alien computers
# ----------------------------------------------------------------------
def main():
    print("=" * 70)
    print("Uncommon Alien Computers Simulator")
    print("=" * 70)

    # 1. Chirali Gravitational Wave Computer
    chirali = ChiraliComputer()
    inputs = [((0,0), 0.0), ((5,5), PHI_INV), ((-5,-5), 1.0)]
    res = chirali.compute(inputs)
    print(f"1. Chirali gravitational wave interference result: {res:.4f}")

    # 2. Phasmid Temporal Stutter Processor
    phasmid = PhasmidComputer()
    def square(x): return x*x
    res = phasmid.compute(square, 5.0)
    print(f"2. Phasmid stutter computation: square(5) with stutter = {res:.2f}")

    # 3. Zerith Dark Energy Computer
    zerith = ZerithComputer()
    pattern = np.array([1.0, 2.0, 5.0, 8.0, 13.0])
    res = zerith.compute(pattern)
    print(f"3. Zerith cosmic correlation sum: {res:.4f}")

    # 4. Orokin Stellar Lasing Array
    orokin = OrokinComputer()
    inputs = [(0.0, 1.0), (PHI_INV, 0.8), (1.0, 0.5)]
    res = orokin.compute(inputs)
    print(f"4. Orokin laser interference power: {res:.2f}")

    # 5. Vex Quantum Pheromone Annealer
    vex = VexComputer(n_qubits=6)
    J = np.random.randn(6,6) * 0.1
    h = np.random.randn(6) * 0.5
    final_state = vex.compute(J, h)
    print(f"5. Vex annealed state: {final_state}")

    # 6. Yldar Phonon Lattice Memory
    yldar = YldarMemory(size=10)
    data = np.array([1, PHI, PHI_SQ, PHI_CUBE])
    yldar.store(data)
    retrieved = yldar.retrieve()
    print(f"6. Yldar stored: {data}, retrieved (first few): {retrieved[:4]}")

    # 7. Petrifex Biomineralization Processor
    petrifex = PetrifexComputer()
    dim = petrifex.compute((25, 25))
    print(f"7. Petrifex crystal fractal dimension: {dim:.3f}")

    # 8. Lithobiont Electrochemical Turing Machine
    lith = LithobiontTuring(tape_length=10)
    initial_tape = [0,0,1,0,0,0,0,0,0,0]
    final_tape, state = lith.compute(initial_tape)
    print(f"8. Lithobiont Turing machine final tape: {final_tape}, state: {state}")

    # 9. Cryovolcanist Plume Logic
    cryo = CryovolcanistLogic()
    result_and = cryo.compute(((20, 45), (20, 45), 30))
    print(f"9. Cryovolcanist AND gate output: {result_and}")

    # 10. Noctilucan Bioluminescent Synchronizer
    noct = NoctilucanComputer(n_osc=30)
    # input signal: sinusoidal forcing
    def input_signal(t):
        return 0.5 * np.sin(2 * np.pi * t)
    final_phases = noct.compute(input_signal, duration=5.0)
    print(f"10. Noctilucan final phase distribution (first 5): {final_phases[:5]}")

    # 11. Rupicolan Adhesion Cellular Automaton
    rupi = RupicolanCA(size=50)
    initial = [1 if i%5==0 else 0 for i in range(50)]
    final = rupi.compute(initial, steps=30)
    print(f"11. Rupicolan CA final pattern (first 20 cells): {final[:20]}")

    # 12. Zephyrite Vortex Turbine Computer
    zeph = ZephyriteComputer(n_turbines=8)
    init_angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
    final_angles = zeph.compute(init_angles, duration=5.0)
    print(f"12. Zephyrite final turbine angles (first 3): {final_angles[:3]}")

    print("\nAll alien computers simulated successfully. The Golden Concordance endures.")

if __name__ == "__main__":
    main()
```
