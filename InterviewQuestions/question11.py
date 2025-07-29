# Question11: 43:07 - Is python asynchronous or Synchronous? What is the default type? and what is asyncio?

# ✅ Is Python Synchronous or Asynchronous?
# 🔸 By default, Python is Synchronous.
# This means it executes one line at a time, in order.
# Each line waits for the previous one to finish before running.
# print("Start")
# print("Middle")
# print("End")
   
# 🔹 What is Asynchronous in Python?
# Asynchronous code doesn't wait — it can run other tasks while waiting for something to finish (like network calls, I/O, etc.)
# For example, in an async program:
# # fake async example
# await download_file()
# print("While it's downloading, do other things")

# ✅ What is asyncio?
# asyncio is a built-in Python library used to write asynchronous code using:
# async functions (called coroutines)
# await keyword (to pause and resume)
# It helps you run concurrent tasks without using threads.
# import asyncio
# async def greet():
#     print("Hello")
#     await asyncio.sleep(2)  # simulate delay (like API or file read)
#     print("World")

# asyncio.run(greet())

import time
import asyncio

def task(name):
    print(f"starting {name}")
    time.sleep(2)
    print(f"finished {name}")

# task("Diwakar")
# task("Kumar")



async def task(name):
    print(f"starting {name}")
    await asyncio.sleep(2)
    print(f"finished {name}")

async def main():
    await asyncio.gather( task("Diwakar"), task("Kumar")) # Run tasks concurrently

asyncio.run(main())


