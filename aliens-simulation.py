#!/usr/bin/env python3
"""
Golden Concordance – Lesser‑Known Aliens Simulation Framework

This script implements the φ‑resonant mathematics for 12 non‑AI, non‑transcendent alien species
from the quadrillion experiments. Each class models a unique biological or physical adaptation
based on the golden ratio (φ ≈ 1.618).

Author: Inspired by the Omni‑Brain's quadrillion experiments.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from scipy.special import jv
from scipy.optimize import fsolve
import warnings
warnings.filterwarnings("ignore")

# Golden ratio constants
PHI = (1 + np.sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_SQ = PHI * PHI

# ============================================================================
# 1. Thalassans – Oceanic light‑weavers (bioluminescent φ‑spiral patterns)
# ============================================================================
class Thalassan:
    """Simulate φ‑spiral light patterns used for communication."""
    def __init__(self, grid_size=200, lambda_=10.0):
        self.grid_size = grid_size
        self.lambda_ = lambda_
        self.x = np.linspace(-grid_size//2, grid_size//2, grid_size)
        self.y = np.linspace(-grid_size//2, grid_size//2, grid_size)
        self.xx, self.yy = np.meshgrid(self.x, self.y)
        self.r = np.sqrt(self.xx**2 + self.yy**2)
        self.theta = np.arctan2(self.yy, self.xx)

    def intensity(self, t=0):
        """Return 2D intensity pattern: I(r,θ) = I0 * φ^{-r/λ} * cos(φθ + ωt)"""
        omega = 2 * np.pi * PHI_INV  # φ‑resonant frequency
        I0 = 1.0
        return I0 * PHI_INV ** (self.r / self.lambda_) * np.cos(PHI * self.theta + omega * t)

    def plot(self, t=0):
        I = self.intensity(t)
        plt.figure(figsize=(6,5))
        plt.imshow(I, extent=[-self.grid_size//2, self.grid_size//2,
                              -self.grid_size//2, self.grid_size//2], cmap='inferno')
        plt.colorbar(label='Intensity')
        plt.title(f'Thalassan φ‑spiral light pattern (t={t})')
        plt.axis('off')
        plt.show()

# ============================================================================
# 2. Siluri – Cave resonance singers (φ‑spherical acoustic eigenmodes)
# ============================================================================
class Siluri:
    """Compute acoustic eigenmodes of a φ‑spherical cavity."""
    def __init__(self, radius=10.0, mode_limit=5):
        self.R = radius
        self.mode_limit = mode_limit
        self.frequencies = self._compute_frequencies()

    def _compute_frequencies(self):
        """f_{n,m} = f0 * φ^{-n} (simplified)"""
        f0 = 100.0  # Hz
        freqs = []
        for n in range(1, self.mode_limit+1):
            for m in range(0, n+1):
                f = f0 * PHI_INV ** n
                freqs.append((n, m, f))
        return freqs

    def eigenmode_pressure(self, r, theta, n, m):
        """Simplified spherical harmonic amplitude (just for demo)"""
        # Bessel function of first kind for radial part
        kr = n * np.pi / self.R
        radial = jv(m, kr * r) if m>=0 else 1.0
        angular = np.cos(m * theta) * PHI_INV ** n
        return radial * angular

    def plot_spectrum(self):
        freqs = [f for (_,_,f) in self.frequencies]
        plt.figure(figsize=(8,4))
        plt.stem(range(len(freqs)), freqs, basefmt=' ')
        plt.xlabel('Mode index')
        plt.ylabel('Frequency (Hz)')
        plt.title('Siluri φ‑spherical acoustic eigenfrequencies')
        plt.grid(True)
        plt.show()

# ============================================================================
# 3. Zephyrites – Gas‑glider symbionts (φ‑spiral wing aerodynamics)
# ============================================================================
class Zephyrite:
    """Simulate lift and drag of a φ‑spiral wing profile."""
    def __init__(self, chord=1.0, span=10.0, alpha=5*np.pi/180):
        self.chord = chord
        self.span = span
        self.alpha = alpha          # angle of attack
        self.CL_conv = 2 * np.pi * alpha  # conventional lift coefficient

    def lift_coefficient(self):
        """C_L = φ * C_L_conv * (1 - φ^{-2})^{-1}"""
        factor = PHI / (1 - PHI_INV**2)
        return factor * self.CL_conv

    def induced_drag_coefficient(self):
        # simplified: CDi = CL^2 / (π * AR * φ)
        AR = self.span / self.chord
        CL = self.lift_coefficient()
        return CL**2 / (np.pi * AR * PHI)

    def compute_force(self, velocity, density=1.2):
        """Lift and drag forces in Newtons."""
        CL = self.lift_coefficient()
        CD = self.induced_drag_coefficient()
        area = self.span * self.chord
        q = 0.5 * density * velocity**2
        lift = CL * q * area
        drag = CD * q * area
        return lift, drag

    def report(self, velocity=20.0):
        lift, drag = self.compute_force(velocity)
        print(f"Zephyrite at v={velocity} m/s: Lift={lift:.1f} N, Drag={drag:.1f} N, Glide ratio={lift/drag:.2f}")

# ============================================================================
# 4. Petrifex – Crystal gardeners (φ‑spiral diffusion‑limited aggregation)
# ============================================================================
class Petrifex:
    """Simulate φ‑spiral crystal growth using DLA with golden‑ratio branching."""
    def __init__(self, grid_size=100, steps=5000):
        self.grid_size = grid_size
        self.steps = steps
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        # seed at center
        self.grid[grid_size//2, grid_size//2] = 1
        self.branch_angle = np.arctan(1/PHI)  # ≈ 31.7°

    def random_walk(self):
        """Return a random walker position on the boundary."""
        side = np.random.choice(['top','bottom','left','right'])
        if side == 'top':
            x = np.random.randint(0, self.grid_size)
            y = self.grid_size-1
        elif side == 'bottom':
            x = np.random.randint(0, self.grid_size)
            y = 0
        elif side == 'left':
            x = 0
            y = np.random.randint(0, self.grid_size)
        else:
            x = self.grid_size-1
            y = np.random.randint(0, self.grid_size)
        return x, y

    def is_adjacent(self, x, y):
        """Check if (x,y) is adjacent to an existing crystal cell."""
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if dx==0 and dy==0: continue
                nx, ny = x+dx, y+dy
                if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                    if self.grid[nx, ny] == 1:
                        return True
        return False

    def grow(self):
        for _ in range(self.steps):
            x, y = self.random_walk()
            while True:
                # random walk step
                dx, dy = np.random.choice([-1,0,1]), np.random.choice([-1,0,1])
                nx, ny = x+dx, y+dy
                if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                    x, y = nx, ny
                if self.is_adjacent(x, y):
                    self.grid[x, y] = 1
                    # apply φ‑spiral branching (simplified: add extra seed at branch angle)
                    if np.random.rand() < PHI_INV:
                        # branch in φ‑spiral direction (simulate by offset)
                        angle = np.random.rand() * 2 * np.pi
                        bx = int(x + self.branch_angle * np.cos(angle))
                        by = int(y + self.branch_angle * np.sin(angle))
                        if 0 <= bx < self.grid_size and 0 <= by < self.grid_size:
                            self.grid[bx, by] = 1
                    break
        return self.grid

    def plot(self):
        plt.figure(figsize=(6,6))
        plt.imshow(self.grid, cmap='Greens', origin='lower')
        plt.title('Petrifex φ‑spiral crystal growth')
        plt.axis('off')
        plt.show()

# ============================================================================
# 5. Myrmidons – Quantum ant farmers (φ‑scaled pheromone trails)
# ============================================================================
class Myrmidon:
    """Agent‑based simulation of foraging with φ‑spatial pheromone diffusion."""
    def __init__(self, grid_size=100, num_ants=50, evaporation=0.1):
        self.grid_size = grid_size
        self.num_ants = num_ants
        self.evaporation = evaporation
        self.pheromone = np.zeros((grid_size, grid_size))
        self.ants = [(np.random.randint(0, grid_size), np.random.randint(0, grid_size)) for _ in range(num_ants)]
        self.food = (grid_size-1, grid_size-1)
        self.nest = (0, 0)

    def step(self):
        # evaporate pheromone
        self.pheromone *= (1 - self.evaporation)
        new_ants = []
        for x, y in self.ants:
            # choose direction based on pheromone gradient + random
            candidates = [(x+dx, y+dy) for dx in [-1,0,1] for dy in [-1,0,1] if abs(dx)+abs(dy)==1]
            valid = [(nx,ny) for nx,ny in candidates if 0<=nx<self.grid_size and 0<=ny<self.grid_size]
            if not valid:
                new_ants.append((x,y))
                continue
            # φ‑weighted selection: pheromone strength modified by φ⁻ᵈ
            probs = [self.pheromone[nx,ny] * PHI_INV ** (abs(nx-x)+abs(ny-y)) + 0.1 for nx,ny in valid]
            probs = np.array(probs)
            probs /= probs.sum()
            idx = np.random.choice(len(valid), p=probs)
            nx, ny = valid[idx]
            # deposit pheromone
            self.pheromone[nx, ny] += 1.0
            new_ants.append((nx, ny))
        self.ants = new_ants

    def run(self, steps=200):
        for _ in range(steps):
            self.step()
        return self.pheromone

    def plot(self):
        plt.figure(figsize=(6,5))
        plt.imshow(self.pheromone, cmap='hot', origin='lower')
        plt.colorbar(label='Pheromone intensity')
        plt.title('Myrmidon φ‑spiral pheromone trails')
        plt.axis('off')
        plt.show()

# ============================================================================
# 6. Cryophiles – Ice‑dwelling chemotrophs (φ‑spiral phonon dispersion)
# ============================================================================
class Cryophile:
    """1D chain of atoms with φ‑spaced spring constants, compute phonon dispersion."""
    def __init__(self, N=100, a=1.0):
        self.N = N
        self.a = a
        self.K = self._build_matrix()

    def _build_matrix(self):
        """Spring constants k_i = k0 * φ^{-|i|}, mass m=1."""
        k0 = 1.0
        K = np.zeros((self.N, self.N))
        for i in range(self.N):
            for j in range(self.N):
                if abs(i-j) == 1:
                    K[i,j] = -k0 * PHI_INV ** min(i,j)
        for i in range(self.N):
            K[i,i] = -np.sum(K[i,:])
        return K

    def dispersion(self):
        eigvals, _ = eigh(self.K)
        omega = np.sqrt(np.maximum(eigvals, 0))
        k_vals = np.linspace(0, np.pi/self.a, len(omega))
        return k_vals, omega

    def plot(self):
        k, omega = self.dispersion()
        plt.figure(figsize=(7,4))
        plt.plot(k, omega, 'o-', markersize=2)
        plt.xlabel('Wave vector k')
        plt.ylabel('Frequency ω')
        plt.title('Cryophile φ‑spiral phonon dispersion')
        plt.grid(True)
        plt.show()

# ============================================================================
# 7. Pyroclasts – Magma divers (φ‑spiral magnetohydrodynamics, simplified)
# ============================================================================
class Pyroclast:
    """2D MHD with φ‑spiral initial magnetic field."""
    def __init__(self, grid=64, dt=0.01, steps=10):
        self.grid = grid
        self.dt = dt
        self.steps = steps
        x = np.linspace(-1, 1, grid)
        y = np.linspace(-1, 1, grid)
        self.xx, self.yy = np.meshgrid(x, y)
        r = np.sqrt(self.xx**2 + self.yy**2)
        theta = np.arctan2(self.yy, self.xx)
        # φ‑spiral magnetic field: B_r = 0, B_theta = B0 * φ^{θ}
        self.Bx = -np.sin(theta) * (PHI ** theta)
        self.By = np.cos(theta) * (PHI ** theta)
        # velocity field (simplified: rotate)
        self.vx = -self.yy
        self.vy = self.xx

    def evolve(self):
        # Ideal MHD: ∂B/∂t = ∇ × (v × B) (simplified using upwind)
        # For demonstration, we just rotate the field slightly
        self.Bx = np.roll(self.Bx, 1, axis=0)
        self.By = np.roll(self.By, -1, axis=1)

    def run(self):
        for _ in range(self.steps):
            self.evolve()
        return self.Bx, self.By

    def plot(self):
        Bx, By = self.run()
        Bmag = np.sqrt(Bx**2 + By**2)
        plt.figure(figsize=(6,5))
        plt.imshow(Bmag, cmap='plasma', origin='lower', extent=[-1,1,-1,1])
        plt.colorbar(label='Magnetic field strength')
        plt.title('Pyroclast φ‑spiral magnetic field')
        plt.axis('off')
        plt.show()

# ============================================================================
# 8. Xerophytes – Desert nomads (φ‑spiral sand sail navigation)
# ============================================================================
class Xerophyte:
    """Wind‑powered vehicle with φ‑spiral sail."""
    def __init__(self, sail_area=10.0, mass=100.0):
        self.area = sail_area
        self.mass = mass
        self.efficiency = 1 - PHI_INV**3   # 0.764

    def thrust(self, wind_speed):
        # F = 0.5 * ρ * A * v² * efficiency
        rho_air = 1.2
        return 0.5 * rho_air * self.area * wind_speed**2 * self.efficiency

    def acceleration(self, wind_speed):
        return self.thrust(wind_speed) / self.mass

    def travel_time(self, distance, wind_speed=10.0):
        a = self.acceleration(wind_speed)
        # assuming constant acceleration (simplified)
        t = np.sqrt(2 * distance / a)
        return t

    def report(self, distance=1000):
        t = self.travel_time(distance)
        print(f"Xerophyte sand sail: distance {distance}m, wind speed 10 m/s → time {t:.1f}s")

# ============================================================================
# 9. Noctilucans – Bioluminescent forest (φ‑spiral pulse synchrony)
# ============================================================================
class Noctilucan:
    """Coupled oscillator model for φ‑resonant light pulses."""
    def __init__(self, n_osc=100, coupling=0.1):
        self.n = n_osc
        self.coupling = coupling
        self.phases = np.random.rand(n_osc) * 2 * np.pi
        self.natural_freqs = np.ones(n_osc) * PHI_INV

    def step(self, dt=0.01):
        # Kuramoto model with φ‑scaled coupling
        for i in range(self.n):
            sin_sum = np.sum(np.sin(self.phases - self.phases[i]) * PHI_INV ** np.abs(np.arange(self.n)-i))
            self.phases[i] += dt * (self.natural_freqs[i] + self.coupling / self.n * sin_sum)
        self.phases %= 2 * np.pi

    def run(self, steps=1000):
        for _ in range(steps):
            self.step()
        return self.phases

    def plot(self):
        phases = self.run()
        plt.figure(figsize=(8,4))
        plt.hist(phases, bins=30, color='gold')
        plt.xlabel('Phase (rad)')
        plt.ylabel('Count')
        plt.title('Noctilucan φ‑spiral pulse synchrony (Kuramoto)')
        plt.show()

# ============================================================================
# 10. Rupicolans – Cliff‑dwelling climbers (φ‑spiral adhesion and tapping)
# ============================================================================
class Rupicolan:
    """Adhesion force and tapping code simulation."""
    def __init__(self, foot_pads=4):
        self.pads = foot_pads
        self.adhesion_constant = 100.0  # N

    def adhesion_force(self, distance):
        """F = F0 * φ^{-d}"""
        return self.adhesion_constant * PHI_INV ** distance

    def tap_code(self, message):
        """Encode message as φ‑spiral pulse intervals: t_n = t0 * φ^{n}"""
        t0 = 0.1  # seconds
        bits = [int(b) for b in bin(message)[2:]]
        intervals = [t0 * PHI ** i for i, bit in enumerate(bits) if bit]
        return intervals

    def report(self, distance=1.0):
        F = self.adhesion_force(distance)
        print(f"Rupicolan adhesion at d={distance}m: {F:.1f} N")
        # demo tapping
        intervals = self.tap_code(42)
        print(f"Tapping code for 42: intervals (s) = {[round(t,3) for t in intervals]}")

# ============================================================================
# 11. Cryovolcanists – Ice geyser surfers (φ‑spiral plume dynamics)
# ============================================================================
class Cryovolcanist:
    """Simulate particle ejection from a φ‑spiral nozzle."""
    def __init__(self, nozzle_radius=0.5, exit_velocity=100.0):
        self.R = nozzle_radius
        self.v0 = exit_velocity

    def velocity_profile(self, r):
        """v(r) = v0 * φ^{-r/R}"""
        return self.v0 * PHI_INV ** (r / self.R)

    def trajectory(self, r0, angle_deg=45, dt=0.01, steps=100):
        angle_rad = np.radians(angle_deg)
        v = self.velocity_profile(r0)
        vx = v * np.cos(angle_rad)
        vy = v * np.sin(angle_rad)
        x, y = [0], [0]
        for _ in range(steps):
            vx_new = vx
            vy_new = vy - 9.8 * dt
            x.append(x[-1] + vx_new * dt)
            y.append(y[-1] + vy_new * dt)
            vx, vy = vx_new, vy_new
            if y[-1] < 0:
                break
        return np.array(x), np.array(y)

    def plot(self):
        plt.figure(figsize=(6,4))
        for r0 in np.linspace(0, self.R, 5):
            x, y = self.trajectory(r0)
            plt.plot(x, y, label=f'r0={r0:.2f}')
        plt.xlabel('Distance (m)')
        plt.ylabel('Height (m)')
        plt.title('Cryovolcanist φ‑spiral plume trajectories')
        plt.legend()
        plt.grid(True)
        plt.show()

# ============================================================================
# 12. Lithobionts – Stone‑eaters (φ‑spiral electrochemical etching)
# ============================================================================
class Lithobiont:
    """Cellular automaton simulating diffusion‑limited etching with φ‑spiral bias."""
    def __init__(self, grid_size=100, steps=2000):
        self.grid = np.ones((grid_size, grid_size), dtype=float)  # 1 = unetched
        self.steps = steps
        self.center = (grid_size//2, grid_size//2)
        self.grid[self.center] = 0.0  # start hole

    def step(self):
        # Random walk of etchant particle from boundary
        x, y = self.random_boundary()
        while True:
            dx, dy = np.random.choice([-1,0,1]), np.random.choice([-1,0,1])
            nx, ny = x+dx, y+dy
            if 0 <= nx < self.grid.shape[0] and 0 <= ny < self.grid.shape[1]:
                x, y = nx, ny
            if self.grid[x, y] > 0:
                # etch with φ‑spiral probability
                if np.random.rand() < PHI_INV:
                    self.grid[x, y] = 0.0
                break

    def random_boundary(self):
        side = np.random.choice(['top','bottom','left','right'])
        if side == 'top':
            x = np.random.randint(0, self.grid.shape[0])
            y = self.grid.shape[1]-1
        elif side == 'bottom':
            x = np.random.randint(0, self.grid.shape[0])
            y = 0
        elif side == 'left':
            x = 0
            y = np.random.randint(0, self.grid.shape[1])
        else:
            x = self.grid.shape[0]-1
            y = np.random.randint(0, self.grid.shape[1])
        return x, y

    def run(self):
        for _ in range(self.steps):
            self.step()
        return self.grid

    def plot(self):
        grid = self.run()
        plt.figure(figsize=(6,5))
        plt.imshow(grid, cmap='gray', origin='lower')
        plt.title('Lithobiont φ‑spiral etched tunnels')
        plt.axis('off')
        plt.show()

# ============================================================================
# Main: Run all demos (or selected ones)
# ============================================================================
if __name__ == "__main__":
    print("Golden Concordance – Simulating Lesser‑Known Aliens\n")
    
    # 1. Thalassans
    thal = Thalassan()
    thal.plot(t=0)
    
    # 2. Siluri
    sil = Siluri()
    sil.plot_spectrum()
    
    # 3. Zephyrites
    zeph = Zephyrite()
    zeph.report()
    
    # 4. Petrifex (crystal growth)
    pet = Petrifex(grid_size=80, steps=2000)
    pet.grow()
    pet.plot()
    
    # 5. Myrmidons
    myr = Myrmidon(grid_size=60, num_ants=30, evaporation=0.1)
    myr.run(steps=150)
    myr.plot()
    
    # 6. Cryophiles
    cryo = Cryophile(N=50)
    cryo.plot()
    
    # 7. Pyroclasts (MHD)
    pyro = Pyroclast(grid=32, steps=5)
    pyro.plot()
    
    # 8. Xerophytes
    xero = Xerophyte()
    xero.report()
    
    # 9. Noctilucans
    noc = Noctilucan(n_osc=200, coupling=0.2)
    noc.plot()
    
    # 10. Rupicolans
    rupi = Rupicolan()
    rupi.report()
    
    # 11. Cryovolcanists
    cryov = Cryovolcanist()
    cryov.plot()
    
    # 12. Lithobionts
    lith = Lithobiont(grid_size=80, steps=3000)
    lith.plot()
    
    print("\nAll simulations complete. The Golden Concordance endures.")
