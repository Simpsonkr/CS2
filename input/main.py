int_input=int(input(print("Enter an Integer between 32 and 126.")))
float_input=float(input(print("Enter a Float")))
char_input=input(print("Enter a Character"))
string_input=str(input(print("Enter a String")))
print(f'{int_input} {float_input} {char_input} {string_input}')
print(f'{string_input} {char_input} {float_input} {int_input}')
int_to_str=chr(int_input)
print(f'{int_input} converted to a character is {int_to_str}')