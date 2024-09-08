import ctypes
import os
import sys
import asyncio

def load_add_lib():
    # Load the shared library
    lib_path = os.path.abspath("./libadd.so")
    add_lib = ctypes.CDLL(lib_path)

    # Define the argument types and return type for the add function
    add_lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
    add_lib.add.restype = ctypes.c_int
    return add_lib


def call_add_lib_blocking(arg1, arg2):
    add_lib = load_add_lib()
    result = add_lib.add(arg1, arg2)
    print(f"Result: {result}")
    
def call_add_lib_non_blocking():
    return asyncio.to_thread(call_add_lib_blocking, 12, 8)
    
# only here to illustrate that we are not blocking 
async def spinner():
    spinner_chars = ['|', '/', '-', '\\']
    while True:
        for char in spinner_chars:
            sys.stdout.write(f'\r{char}')
            sys.stdout.flush()
            await asyncio.sleep(0.5)
                
async def main():
    asyncio.create_task(spinner())
    # call_add_lib_blocking(3, 5)
    await call_add_lib_non_blocking()


if __name__ == '__main__':
    asyncio.run(main())