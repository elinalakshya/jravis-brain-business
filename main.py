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

# JRAVIS-BRAIN — FULL PUBLISH MODE MAIN FILE
# Sends continuous publishing tasks to jravis-backend

from publishing_mode import run_publishing_loop

if __name__ == "__main__":
    print("🔥 JRAVIS-BRAIN — PUBLISH MODE STARTING")
    print("🤖 Generating & publishing tasks 24/7")
    run_publishing_loop()


# JRAVIS-BRAIN — FULL PUBLISH MODE

from publishing_mode import run_publishing_loop

if __name__ == "__main__":
    print("🔥 JRAVIS-BRAIN — PUBLISH MODE STARTING")
    print("🤖 Generating & publishing tasks 24/7")
    run_publishing_loop()

