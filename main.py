import os
os.chdir("src/ui")

from sys import path
path.append('.')


from uz_train_schedule_app import run


if __name__ == "__main__":
	run()
