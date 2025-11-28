# JRAVIS Business Brain — 12 Stream Scheduler

import time
from config import STREAM_INTERVALS
from utils import send_task

# Import all 12 brain stream builders
import streams.stream1_brain as stream1
import streams.stream2_brain as stream2
import streams.stream3_brain as stream3
import streams.stream4_brain as stream4
import streams.stream5_brain as stream5
import streams.stream6_brain as stream6
import streams.stream7_brain as stream7
import streams.stream8_brain as stream8
import streams.stream9_brain as stream9
import streams.stream10_brain as stream10
import streams.stream11_brain as stream11
import streams.stream12_brain as stream12

LAST_RUN = {i: 0 for i in range(1, 13)}

def schedule_all_streams():
    current = time.time()
    streams = [
        stream1, stream2, stream3, stream4, stream5, stream6,
        stream7, stream8, stream9, stream10, stream11, stream12
    ]

    for i, module in enumerate(streams, start=1):
        if current - LAST_RUN[i] >= STREAM_INTERVALS[i]:
            print(f"🧠 Triggering Stream {i}")
            payload = module.build_task()
            send_task(payload)
            LAST_RUN[i] = current
