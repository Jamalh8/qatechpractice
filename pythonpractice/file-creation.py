# with open('example.txt', 'w') as file1:
#     file1.write('Hello\nthis\nis\na\ntest\nof\nnew\nlines')

file1= open('example.txt', 'r')

all_lines= file1.readline()
file1.seek(0)
all_lines1= file1.readline()
all_lines2= file1.readline()
all_lines3= file1.readline()
print(all_lines)
print(all_lines1)
print(all_lines2)
print(all_lines3)

file1.close()