# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 06:26:09 2021

@author: ISH KAPOOR
"""

"""Week I Assignment
Simulate the trajectory of a robot approximated using a unicycle model given the
following start states, dt, velocity commands and timesteps
State = (x, y, theta);
Velocity = (v, w)
1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50
Upload the completed python file and the figures of the three sub parts in classroom
"""
import numpy as np
import matplotlib.pyplot as plt


class Unicycle:

    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):

        """
        Write the Kinematics model here
        Expectation:
            1. Given v, w and the current state self.x, self.y, self.theta
                and control commands (v, w) for n timesteps, i.e. n * dt seconds,
                return the final pose (x, y, theta) after this time.
            2. Append all intermediate points into the self.x_points, self.y_points "list"
                for plotting the trajectory.
        Args:
            v (float): linear velocity
            w (float): angular velocity
            n (int)  : timesteps
        Return:
            x, y, theta (float): final pose 
        """

        for _ in range(n):
            self.x += v * np.cos(self.theta)
            self.y += v * np.sin(self.theta)
            self.theta += w * (self.dt)

            self.x_points.append(self.x)
            self.y_points.append(self.y)

        return self.x, self.y, self.theta

    def plot(self, v: float, w: float):

        """Function that plots the intermeditate trajectory of the Robot"""

        plt.title(f"Unicycle Model: {v}, {w}, by Ish")
        plt.xlabel("X-Coordinates (Ish)")
        plt.ylabel("Y-Coordinates (Ish)")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()

        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
        plt.show()
        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
        # plt.savefig(f"Unicycle_{v}_{w}.png")

if __name__ == "__main__":

    print("Unicycle Model Assignment")

    trajectory = [
        {'x': 0, 'y': 0, 'theta': 0, 'dt': 0.1, 'n': 25, 'v': 1, 'w': 0.5},
        {'x': 0, 'y': 0, 'theta': 1.57, 'dt': 0.2, 'n': 10, 'v': 0.5, 'w': 1},
        {'x': 0, 'y': 0, 'theta': 0.77, 'dt': 0.05, 'n': 50, 'v': 5, 'w': 4}
    ]

    for i in range(len(trajectory)):
        x = trajectory[i]['x']
        y = trajectory[i]['y']
        theta = trajectory[i]['theta']
        dt = trajectory[i]['dt']
        v = trajectory[i]['v']
        w = trajectory[i]['w']
        n = trajectory[i]['n']
        uCycle = Unicycle(x, y, theta, dt)
        pose = uCycle.step(v, w, n)
        x, y, theta = pose
        uCycle.plot(v, w)

    # make an object of the robot and plot various trajectories