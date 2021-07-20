











def arithmetic_arranger(problems, val=False):
    arranged_problems = ''
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    # list of all operations in str format
    operations = list(map(lambda x: x.split()[1], problems))
    if set(operations) != {'+', '-'} and len(set(operations)) != 2:
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems

    numbers = []  # list of all operands in str format
    for i in problems:
        p = i.split()
        numbers.extend([p[0], p[2]])

    if not all(map(lambda x: x.isdigit(), numbers)):
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems

    if not all(map(lambda x: len(x) < 5, numbers)):
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems

    top_row = ''
    dashes = ''
    values = list(map(lambda x: eval(x), problems))
    solutions = ''
    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i+1])) + 2
        top_row += numbers[i].rjust(space_width)
        dashes += '-' * space_width
        solutions += str(values[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            top_row += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    bottom_row = ''
    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
        bottom_row += operations[i // 2]
        bottom_row += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            bottom_row += ' ' * 4

    if val:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))
    return arranged_problems














# import re
# def arithmetic_arranger(problems,solve=False):
#   if len(problems)>=6:
#     return "Error:Too many problems."
#   first=""
#   second=""
#   lines=""
#   sumx=""
#   string=""
#   for i in problems:
#     if(re.search("[^\s0-9.+-]",i)):
#       if(re.search("[/]",i) or re.search("[*]",i)):
#         return "Error:Operator must be '+' or '-'."
#       return "Error:Numbers must only contain digits"
#     firstNum=i.split(" ")[0]
#     operator=i.split(" ")[1]
#     SecondNum=i.split(" ")[2]

#     if(len(firstNum)>=5 or len(SecondNum)>=5):
#       return "Error:Numbers cannot be more than four digits."
#     sum=""
#     if(operator=="+"):
#       sum=str(int(firstNum)+int(SecondNum))
#     elif(operator=="-"):
#       sum=str(int(firstNum)-int(SecondNum))
        


#     length=max(len(firstNum),len(SecondNum))+2
#     top=str(firstNum).rjust(length)
#     bottom=operator+str(SecondNum).rjust(length-1)
#     line=""
#     result=str(sum).rjust(length)
#     for s in range(length):
#       line+="-"
#     if i!=problems[-1]:
#       first+=top+'  '
#       second+=bottom+'  '
#       lines+=line+'  '
#       sumx+=result+'  '
#     else:
#       first+=top
#       second+=bottom
#       lines+=line
#       sumx+=result

#   if solve:
#         arranged_problems=first+ "/n"+second + "/n" +lines + "/n"+sumx
#   else:
#         arranged_problems=first+ "/n"+second+"/n"+lines
#   return arranged_problems




# a=arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
# print(a)
