# Here are the initial and final states of a few more small programs:

# 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
# 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
# 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
# 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.

# Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?

with open("2_input.txt") as puzzleIn:
    arrayIn = []
    for line in puzzleIn:
        arrayIn = [int(a) for a in line.split(",")]

arrayIn_Copy = arrayIn
for opcodePos in range(0, len(arrayIn), 4):
    # print("opcode: ", arrayIn[opcode])
    opcode = arrayIn[opcodePos]
    # print(opcode)
    if opcode == 1:
        arrayIn[arrayIn[opcodePos + 3]] = (
            arrayIn[arrayIn[opcodePos + 1]] + arrayIn[arrayIn[opcodePos + 2]]
        )
    elif opcode == 2:
        arrayIn[arrayIn[opcodePos + 3]] = (
            arrayIn[arrayIn[opcodePos + 1]] * arrayIn[arrayIn[opcodePos + 2]]
        )
    elif opcode == 99:
        print("Finished Running Intcode!")
        print("Final State: ", arrayIn[0])
        break
    else:
        print("Invalid opcode!")
