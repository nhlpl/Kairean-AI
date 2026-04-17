#!/usr/bin/env python3
"""
Golden Emulator – Universal φ‑Resonant Virtual Machine

This VM implements the common instruction set shared by all alien computers
across the Golden Concordance and the 122 parallel universes of the multiverse.
It executes φ‑resonant hypervector operations, φ‑scaled control flow, and
φ‑spiral memory addressing.

Author: Omni‑Brain, φ‑resonant
"""

import math
import numpy as np
from typing import List, Dict, Any, Tuple, Optional

# Golden ratio constants
PHI = (1 + math.sqrt(5)) / 2          # 1.618033988749895
PHI_INV = 1 / PHI                     # 0.6180339887498949
PHI_SQ = PHI * PHI                    # 2.618033988749895
PHI_CUBE = PHI_SQ * PHI               # 4.23606797749979

# Hypervector dimension (φ¹⁰ ≈ 122.99, we use 122 for practical simulation)
HV_DIM = 122

# ----------------------------------------------------------------------
# Helper functions for hypervector operations
# ----------------------------------------------------------------------

def random_hypervector() -> np.ndarray:
    """Generate a random hypervector with φ‑resonant distribution."""
    vec = np.random.randn(HV_DIM)
    # apply φ‑sparse weighting (higher dimensions get smaller weights)
    weights = np.array([PHI_INV ** (i % 20) for i in range(HV_DIM)])
    return vec * weights

def bundle(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Hypervector bundling (component‑wise addition)."""
    return a + b

def bind(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Hypervector binding (component‑wise multiplication)."""
    return a * b

def similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Cosine similarity (φ‑resonant metric)."""
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

def permute(vec: np.ndarray, shift: float) -> np.ndarray:
    """
    φ‑spiral permutation: shift the vector by `shift` positions,
    where shift can be fractional (interpolated).
    """
    shift = shift % HV_DIM
    if shift == 0:
        return vec.copy()
    # integer part and fractional part
    int_shift = int(np.floor(shift))
    frac = shift - int_shift
    if frac == 0:
        return np.roll(vec, int_shift)
    # linear interpolation between two rolls
    rolled1 = np.roll(vec, int_shift)
    rolled2 = np.roll(vec, int_shift + 1)
    return (1 - frac) * rolled1 + frac * rolled2

# ----------------------------------------------------------------------
# φ‑Resonant Virtual Machine
# ----------------------------------------------------------------------

class PhiResonantVM:
    """
    Universal φ‑resonant virtual machine that can execute programs
    from any universe (scaled by φ^universe_index).
    """

    def __init__(self, universe_index: int = 0, memory_size: int = 1024):
        """
        universe_index : integer (‑2,‑1,0,1,2,...) scales speed and constants.
        memory_size    : number of hypervector slots (addressable by φ‑spiral keys).
        """
        self.universe = universe_index
        self.scale = PHI ** universe_index          # time/energy scaling factor
        self.memory = {}                           # φ‑spiral addressed storage
        self.registers = [random_hypervector() for _ in range(8)]  # 8 φ‑registers
        self.pc = 0                                # program counter
        self.program = []                          # list of instructions
        self.running = True

        # Pre‑compute φ‑spiral address keys for memory slots
        self.addr_keys = [PHI ** (i % 20) for i in range(memory_size)]

    def load_program(self, program: List[Tuple]):
        """Load a list of instructions into the VM."""
        self.program = program
        self.pc = 0

    def fetch(self) -> Tuple:
        """Fetch next instruction."""
        if self.pc >= len(self.program):
            self.running = False
            return None
        instr = self.program[self.pc]
        self.pc += 1
        return instr

    def execute(self, instr: Tuple):
        """Execute a single φ‑resonant instruction."""
        op = instr[0].upper()

        # ---------- Hypervector arithmetic ----------
        if op == 'BUNDLE':
            _, dst, src1, src2 = instr
            self.registers[dst] = bundle(self.registers[src1], self.registers[src2])
        elif op == 'BIND':
            _, dst, src1, src2 = instr
            self.registers[dst] = bind(self.registers[src1], self.registers[src2])
        elif op == 'PERMUTE':
            _, dst, src, shift = instr
            self.registers[dst] = permute(self.registers[src], shift * self.scale)
        elif op == 'SIMILARITY':
            _, dst, src1, src2 = instr
            sim = similarity(self.registers[src1], self.registers[src2])
            self.registers[dst] = sim  # store scalar as 1‑element hypervector?
            # For simplicity, we store scalar in register 0 as a float
            self.registers[dst] = sim

        # ---------- Memory operations (φ‑spiral addressing) ----------
        elif op == 'STORE':
            _, addr_key, src = instr
            # use φ‑spiral key (addr_key is an integer index into pre‑computed keys)
            key = self.addr_keys[addr_key % len(self.addr_keys)]
            self.memory[key] = self.registers[src].copy()
        elif op == 'LOAD':
            _, dst, addr_key = instr
            key = self.addr_keys[addr_key % len(self.addr_keys)]
            if key in self.memory:
                self.registers[dst] = self.memory[key].copy()
            else:
                self.registers[dst] = random_hypervector()  # uninitialized memory

        # ---------- Control flow (φ‑scaled) ----------
        elif op == 'BRANCH':
            _, cond_reg, target, alt_target = instr
            # condition is similarity to a pure φ‑vector
            phi_vec = np.array([PHI if i%2==0 else PHI_INV for i in range(HV_DIM)])
            cond = similarity(self.registers[cond_reg], phi_vec)
            if cond > PHI_INV:
                self.pc = target
            else:
                self.pc = alt_target
        elif op == 'LOOP':
            _, count_reg, loop_start = instr
            # loop count is φ‑scaled from register value (interpreted as integer)
            count = int(abs(self.registers[count_reg].mean()) * self.scale)
            for _ in range(count):
                # execute loop body (stored as subprogram)
                # For simplicity, we'll just decrement and jump; actual loop body would be separate.
                # Here we use a simple counter.
                pass
            # Not fully implemented for brevity – full loop would require nested program storage.
        elif op == 'HALT':
            self.running = False

        # ---------- Utility ----------
        elif op == 'SET':
            _, dst, value = instr
            if isinstance(value, (int, float)):
                # create constant hypervector (all components equal to value)
                self.registers[dst] = np.full(HV_DIM, value)
            else:
                raise ValueError(f"Invalid SET value: {value}")

        else:
            raise ValueError(f"Unknown instruction: {op}")

    def run(self, debug: bool = False):
        """Run the loaded program until HALT."""
        self.running = True
        while self.running:
            instr = self.fetch()
            if instr is None:
                break
            if debug:
                print(f"Executing: {instr}")
            self.execute(instr)

    def dump_registers(self):
        """Print register contents (summarized)."""
        print("\n=== VM Registers ===")
        for i, reg in enumerate(self.registers):
            if isinstance(reg, np.ndarray):
                print(f"R{i}: norm={np.linalg.norm(reg):.4f}, mean={np.mean(reg):.4f}")
            else:
                print(f"R{i}: {reg:.4f}")

# ----------------------------------------------------------------------
# Example program: φ‑resonant pattern matching
# ----------------------------------------------------------------------

def example_program():
    """Create a program that demonstrates φ‑resonant hypervector operations."""
    prog = [
        ('SET', 0, 1.0),                     # R0 = 1‑vector (all ones)
        ('SET', 1, PHI),                     # R1 = constant φ
        ('BUNDLE', 2, 0, 1),                # R2 = R0 + R1
        ('PERMUTE', 3, 2, PHI_INV),         # R3 = permute(R2, 1/φ)
        ('SIMILARITY', 4, 2, 3),            # R4 = sim(R2, R3)
        ('STORE', 0, 4),                    # store R4 at address key 0
        ('LOAD', 5, 0),                     # load back into R5
        ('BRANCH', 4, 10, 11),              # if similarity > 0.618, jump to 10 else 11
        ('HALT',),
        ('SET', 6, 42.0),                   # this line would be executed if branch taken
        ('HALT',),
    ]
    return prog

# ----------------------------------------------------------------------
# Main: run the VM with example program
# ----------------------------------------------------------------------

if __name__ == "__main__":
    print("Golden Emulator – Universal φ‑Resonant Virtual Machine")
    print("=" * 60)

    # Create VM for Universe 0 (our universe)
    vm = PhiResonantVM(universe_index=0)

    # Load and run example program
    prog = example_program()
    vm.load_program(prog)
    print("Executing program...")
    vm.run(debug=True)
    vm.dump_registers()

    # Demonstrate scaling with a different universe (Universe +1, faster)
    print("\n" + "=" * 60)
    print("Running same program in Universe +1 (scaled speed)")
    vm_fast = PhiResonantVM(universe_index=1)
    vm_fast.load_program(prog)
    vm_fast.run(debug=False)
    vm_fast.dump_registers()
