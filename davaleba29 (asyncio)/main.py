import asyncio
import time

# ---------1 davaleba--------------


# async def my_task_1():
#     print("This task has started: task1")
#     await asyncio.sleep(5)
#     print("This task has ended: task1")
#
#
# async def my_task_2():
#     print("This task has started: task2")
#     await asyncio.sleep(2)
#     print("This task has ended: task2")
#
#
# async def main():
#     all_tasks = await asyncio.gather(my_task_1(), my_task_2())
#
# start = time.time()
# asyncio.run(main())
# print(time.time() - start)


# ---------2 davaleba---------------


async def numbers(num, delay):
    await asyncio.sleep(delay)
    print(num)


async def main():
    all_numbers = []
    for i in range(1, 11):
        num = i
        delay = i
        all_numbers.append(numbers(num, delay))
    await asyncio.gather(*all_numbers)

start = time.time()
asyncio.run(main())
print(time.time() - start)
