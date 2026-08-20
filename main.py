import threading
import time
import schedule
from datetime import datetime as dt

stop_task = False


def print_time():
	today = dt.now().strftime("%Y-%m-%d %H:%M:%S")
	print(f"\n{today}")


def run_task():
	schedule.every(3).seconds.do(print_time)
	while not stop_task:
		schedule.run_pending()
		time.sleep(1)


def main():
	global stop_task
	threading.Thread(target=run_task, daemon=True).start()
	while True:
		choice = input("Please enter the choice: ").strip().lower()
		if choice == "q":
			stop_task = True
			break
		else:
			print("If you want to quit, please enter 'q'")


main()
