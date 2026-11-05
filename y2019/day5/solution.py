from pathlib import Path
from time import perf_counter
def print_code_with_param(a: tuple[int,...]):
    # print(a)
    return None

def get_param(data: list[int], ptr: int, count: int, mode: int) -> list[int]:
    response_data = []
    mode_pos = 100
    # print(data)
    for p in range(count):
        if int(mode/mode_pos) % 10 == 1:
            response_data.append(data[ptr+p+1])
        else:
            response_data.append(data[data[ptr+p+1]])
        mode_pos *= 10
    if count == 1:
        return response_data[0]
    else:
        return response_data

def intcode(code: list[int], ptr1: int, ptr2: int) -> None:
    ptr = 0
    buf = 0
    while True:
        # print(code)
        if code[ptr] == 99:
            print_code_with_param((code[ptr]))
            break
        elif code[ptr]%100 == 1:
            if code[ptr+3] < len(code) and (int(code[ptr]/100)%10 == 1 or code[ptr+1] < len(code)) and (int(code[ptr]/1000)%10 == 1 or code[ptr+2] < len(code)):
                print_code_with_param((code[ptr], code[ptr+1], code[ptr+2], code[ptr+3]))
                a, b = get_param(code, ptr, 2, code[ptr])
                code[code[ptr+3]] = a + b
            ptr += 4
        elif code[ptr]%100 == 2:
            if code[ptr+3] < len(code) and (int(code[ptr]/100)%10 == 1 or code[ptr+1] < len(code)) and (int(code[ptr]/1000)%10 == 1 or code[ptr+2] < len(code)):
                print_code_with_param((code[ptr], code[ptr+1], code[ptr+2], code[ptr+3]))
                a, b = get_param(code, ptr, 2, code[ptr])
                code[code[ptr+3]] = a * b
            ptr += 4
        elif code[ptr]%100 == 3:
            print_code_with_param((code[ptr], code[ptr+1], ptr1))
            if code[ptr+1] < len(code):
                code[code[ptr+1]] = ptr1
            ptr += 2
        elif code[ptr]%100 == 4:
            print_code_with_param((code[ptr], code[ptr+1]))
            buf = get_param(code, ptr, 1, code[ptr])
            ptr += 2
        elif code[ptr]%100 == 5:
            print_code_with_param((code[ptr], code[ptr+1], code[ptr+2]))
            a, b = get_param(code, ptr, 2, code[ptr])
            if a!= 0:
                ptr = b
            else:
                ptr += 3
        elif code[ptr]%100 == 6:
            print_code_with_param((code[ptr], code[ptr+1], code[ptr+2]))
            a, b = get_param(code, ptr, 2, code[ptr])
            if a == 0:
                ptr = b
            else:
                ptr += 3
        elif code[ptr]%100 == 7:
            print_code_with_param((code[ptr], code[ptr+1], code[ptr+2], code[ptr+3]))
            a, b = get_param(code, ptr, 2, code[ptr])
            if a < b:
                code[code[ptr+3]] = 1
            else:
                code[code[ptr+3]] = 0
            ptr += 4
        elif code[ptr]%100 == 8:
            print_code_with_param((code[ptr], code[ptr+1], code[ptr+2], code[ptr+3]))
            a, b = get_param(code, ptr, 2, code[ptr])
            if a == b:
                code[code[ptr+3]] = 1
            else:
                code[code[ptr+3]] = 0
            ptr += 4
        else:
            print("Unknow code:" ,{code[ptr]})
            break
        
    return buf

def solve(data: list[str], ptr1, ptr2) -> int:
    code = list(map(int, data[0].split(',')))
    return intcode(code, ptr1, ptr2)

def solve2(data: list[str], ptr1) -> int:
    code = list(map(int, data[0].split(',')))
    return intcode(code, ptr1, 2)

if __name__ == "__main__":
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    start = perf_counter()
    print(solve(data, 1, 2))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")

    start = perf_counter()
    print(solve2(data, 5))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")