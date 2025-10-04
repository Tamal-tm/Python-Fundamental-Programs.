# Using readLines() and comprehension

f=open(r"C:\Users\catas\OneDrive\Desktop\VS Code Progs\Python_Progs\Python Fundamentals\List.py\file_list.txt")
lines=f.readlines()

print(lines)

new_lines=[x.strip() for x in lines]
print(new_lines)

# Using for loop and comprehension

f=open(r"C:\Users\catas\OneDrive\Desktop\VS Code Progs\Python_Progs\Python Fundamentals\List.py\file_list.txt")
line=[line for line in f]

print(line)

new_line=[x.strip() for x in line]
print(new_line)
