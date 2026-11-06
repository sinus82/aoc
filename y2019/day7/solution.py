from pathlib import Path
from time import perf_counter
from itertools import permutations
def print_code_with_param(a: tuple[int,...]):
    # print(a)
    return None

def get_param(data: list[int], ptr: int, count: int, mode: int) -> int | list[int]:
    response_data = []
    mode_pos = 1
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

def intcode(code1: list[int], ptr1: list[int]) -> None:
    # print(code1)
    code = code1.copy()
    ptr = 0
    buf = 0
    ptr1_ptr = 0
    while True:
        # print(code)
        opcode = code[ptr] % 100
        modes = code[ptr] // 100
        if opcode == 99:
            print_code_with_param((code[ptr]))
            break
        elif opcode == 1: #Add
            # if code[ptr+3] < len(code) and (int(code[ptr]/100)%10 == 1 or code[ptr+1] < len(code)) and (int(code[ptr]/1000)%10 == 1 or code[ptr+2] < len(code)):
            print_code_with_param((code[ptr], code[ptr+1], code[ptr+2], code[ptr+3]))
            a, b = get_param(code, ptr, 2, modes)
            code[code[ptr+3]] = a + b
            ptr += 4
        elif opcode == 2: #Mul
            # if code[ptr+3] < len(code) and (int(code[ptr]/100)%10 == 1 or code[ptr+1] < len(code)) and (int(code[ptr]/1000)%10 == 1 or code[ptr+2] < len(code)):
            print_code_with_param((code[ptr], code[ptr+1], code[ptr+2], code[ptr+3]))
            a, b = get_param(code, ptr, 2, modes)
            code[code[ptr+3]] = a * b
            ptr += 4
        elif opcode == 3: #Input
            if ptr1_ptr == 2:
                # print(code)
                return (buf, code)
            print_code_with_param((code[ptr], code[ptr+1], ptr1))
            if code[ptr+1] < len(code) or True:
                code[code[ptr+1]] = ptr1[ptr1_ptr]
                ptr1_ptr += 1
            ptr += 2
        elif opcode == 4: #Output
            print_code_with_param((code[ptr], code[ptr+1]))
            buf = get_param(code, ptr, 1, modes)
            # print(buf)
            ptr += 2
        elif opcode == 5: #JumpIfTrue
            print_code_with_param((code[ptr], code[ptr+1], code[ptr+2]))
            a, b = get_param(code, ptr, 2, modes)
            if a != 0:
                ptr = b
            else:
                ptr += 3
        elif opcode == 6: #JumpIfFalse
            print_code_with_param((code[ptr], code[ptr+1], code[ptr+2]))
            a, b = get_param(code, ptr, 2, modes)
            if a == 0:
                ptr = b
            else:
                ptr += 3
        elif opcode == 7: #LessThan
            print_code_with_param((code[ptr], code[ptr+1], code[ptr+2], code[ptr+3]))
            a, b = get_param(code, ptr, 2, modes)
            if a < b:
                code[code[ptr+3]] = 1
            else:
                code[code[ptr+3]] = 0
            ptr += 4
        elif opcode == 8: #Equ
            print_code_with_param((code[ptr], code[ptr+1], code[ptr+2], code[ptr+3]))
            a, b = get_param(code, ptr, 2, modes)
            if a == b:
                code[code[ptr+3]] = 1
            else:
                code[code[ptr+3]] = 0
            ptr += 4
        else:
            print("Unknow code:" ,{code[ptr]})
            break
        
    return (buf, '99')

def solve(data: list[str]) -> int:
    code = list(map(int, data[0].split(',')))
    max_result = 0
    for p in permutations(range(5)):
        result = 0
        for phase in p:
            result = intcode(code, [phase, result])[0]
        if result > max_result:
            max_result = result

    return max_result

def solve2(data: list[str]) -> int:
    code = list(map(int, data[0].split(',')))
    max_result = 0
    for p in permutations(range(5)):
        a = (0,code.copy())
        b = (0,code.copy())
        c = (0,code.copy())
        d = (0,code.copy())
        e = (0,code.copy())
        x = 0
        while True:
            x += 1
            if x == 7:
                break
            print(a)
            print(" ")
            print(" ")
            a = intcode(a[1], [p[0]+5, e[0]])
            print(a)
            b = intcode(b[1], [p[1]+5, a[0]])
            c = intcode(c[1], [p[2]+5, b[0]])
            d = intcode(d[1], [p[3]+5, c[0]])
            e = intcode(e[1], [p[4]+5, d[0]])
            if(e[1] == '99'):
                # print("".join(str(i + 5) for i in p), ": ", e[0])
                if e[0] > max_result:
                    max_result = e[0]
                break
        break
    return max_result

if __name__ == "__main__":
    # data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    # start = perf_counter()
    # print(solve(data))
    # end = perf_counter()
    # print(f"Execution time: {(end - start) * 1000:.6f} ms")

    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    start = perf_counter()
    print(solve2(data))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")