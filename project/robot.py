class Robot:
    def __init__(self, name, model, year):
        self.name = name        # Name of the robot
        self.model = model      # Model of the robot
        self.year = year        # Year of manufacture

    def introduce(self):
        """Method to introduce the robot."""
        introduction = (f"Hello! I am {self.name}, "
                        f"a {self.model} model, "
                        f"manufactured in {self.year}.")
        return introduction

    def perform_task(self, task):
        """Method to simulate the robot performing a task."""
        return f"{self.name} is now performing the task: {task}."


# Creating an instance of the Robot class
robot1 = Robot("RoboHelper", "XJ-9", 2026)

# Introducing the robot
print(robot1.introduce())

# Simulating the robot performing a task
print(robot1.perform_task("cleaning the house"))
