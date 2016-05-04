# pursuer-evader-ros

## About
This project was a part of [CSE568 (Robotic Algorithms)] (http://www.cse.buffalo.edu/shared/course.php?e=CSE&n=568) course at University at Buffalo.

## Project Goals

1. Create a evader robot that moves freely in the world. The world file is supplied and contains some obstacles in it which the evader should not crash into.
2. Create a pursuer robot that follows the evader robot in the world.

## How it was done

1. The evader robot has access to a laser rangefinder. Upon accessing the reading from the laser rangefinder, it can infer if a obstacle is in front of it or not. If the obstacle is in front of it, it turns a random angle and tries to proceed further. It does this till it is able to steer away from the obstacle.
2. The evader robot publishes its coordinates which the pursuer subsribes to. The pursuer is hence able to follow the evader robot.

## Technologies / Platforms

1. Ubuntu 14.04
2. Python 2.7
3. ROS