from worker import Worker
from app import LongTask


if __name__ == "__main__":
    long_task = LongTask()
    worker = Worker(task=long_task)


    worker.start()