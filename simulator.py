from .utils.vector import Vector2

class Simulator:
    def __init__(self, world, Engine, Solver):
        self.t = 0
        self.world = world

        self.engine = Engine(self.world)

        # Engine uses World to represent the state
        # of the world while Solver uses a
        # vector to represent the current state of
        # the ODE system.
        # The method Engine.make_solver_state computes
        # the vector of state variables (the positions
        # and velocities of the bodies) as a Vector

        y0 = self.engine.make_solver_state()

        self.solver = Solver(self.engine.derivatives, self.t, y0)

    def step(self, h):
        y = self.solver.integrate(self.t + h)

        for i in range(len(self.world)):
            b_i = self.world.get(i)

            b_i.position.set_x(y[2 * i])
            b_i.position.set_y(y[2 * i + 1])

            b_i.velocity.set_x(y[len(self.world) + 2 * i])
            b_i.velocity.set_y(y[len(self.world) + 2 * i + 1])

        for i in range(len(self.world)):
            b_i = self.world.get(i)
            pos_i = b_i.position
            mass_i = b_i.mass
            vel_i = b_i.velocity
            vi = vel_i[0]*vel_i[0] + vel_i[1]*vel_i[1]
            rad_i = b_i.radius

            for j in range(i+1,len(self.world)):
                b_j = self.world.get(j)
                pos_j = b_j.position
                rad_j = b_j.radius
                d = pos_j - pos_i
                nd = (d[0]*d[0]+d[1]*d[1])**0.5
                if nd < (rad_i + rad_j):
                    mass_j = b_j.mass
                    vel_j = b_j.velocity
                    Ei = mass_i* (vel_i[0]**2+vel_i[1]**2)
                    Ej = mass_j* (vel_j[0]**2+vel_j[1]**2)
                    if Ej>Ei:
                        b_j.mass = mass_j + mass_i
                        b_i.mass = 0
                        b_j.velocity = 1/(mass_j+mass_i)*(mass_i*vel_i + mass_j*vel_j)
                        b_i.velocity = Vector2(0,0)
                        b_i.radius = 0
                        b_j.radius = (rad_i**3+rad_j**3)**(1/3)
                    else :
                        b_j.mass = mass_j + mass_i
                        b_j.mass = 0
                        b_i.velocity = 1/(mass_j+mass_i)*(mass_i*vel_i + mass_j*vel_j)
                        b_j.velocity = Vector2(0,0)
                        b_j.radius = -1
                        b_i.radius = (rad_i**3+rad_j**3)**(1/3)

        self.t += h
