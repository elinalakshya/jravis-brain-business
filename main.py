# JRAVIS Business Brain — Main Controller

import time
from task_scheduler import schedule_all_streams

def main():
    print("🚀 JRAVIS Business Brain Activated — Running 24/7")

    while True:
        try:
            schedule_all_streams()
        except Exception as e:
            print("❌ Brain Error:", str(e))

        time.sleep(60)  # loop every minute

if __name__ == "__main__":
    main()
