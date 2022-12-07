variable = str(input('Type variable: '))

lst_digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lst_punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';',
                   '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~']
lst_keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
       'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
       'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

if variable == '_':
    print("True")
elif variable[0] in lst_digit or variable.isdigit():
    print("False")
elif any(i in lst_punctuation for i in variable):
    print("False")
elif variable in lst_keywords:
    print("False")
elif not variable.islower():
    print("False")
else:
    print("True")
