# Info:-
# Name   : Maaz 
# Dept   : CO-B
# Batch  : 4
# Sub    : Python Assignment-4
# Topic  : WAP to demonstrate the use of loop manipulation statements.
# Date   : 17-06-2023

# Program:-
# break:-
print("_________________________________________________________");
print("Demonstration of break statement:-");
for i in range(1,6):
    if i==3: 
        break
    else:
        print(i);

# continue:-
print("_________________________________________________________");
print("Demonstration of continue statement:-");
for i in range(1,6):
    if i==3: 
        continue
    else:
        print(i);

# pass:-
print("_________________________________________________________");
print("Demonstration of pass statement:-");
for i in range(1,6):
    if i==3:
        pass
    else:
        print(i)

# for loop with else:-
print("_________________________________________________________");
print("Demonstration of for loop with 'else' block:-");
for i in range(1,6):
    print(i);
else:
    print("[In else block of for loop.]");

# while loop with else:-
print("_________________________________________________________");
print("Demonstration of while loop with 'else' block:-");
i=1;
while i<=5:
    print(i);
    i+=1;
else:
        print("[In else block of while loop.]");
print("_________________________________________________________");
print();

# Output:-
# _________________________________________________________
# Demonstration of break statement:-
# 1
# 2
# _________________________________________________________
# Demonstration of continue statement:-
# 1
# 2
# 4
# 5
# _________________________________________________________
# Demonstration of pass statement:-
# 1
# 2
# 4
# 5
# _________________________________________________________
# Demonstration of for loop with 'else' block:-
# 1
# 2
# 3
# 4
# 5
# [In else block of for loop.]
# _________________________________________________________
# Demonstration of while loop with 'else' block:-
# 1
# 2
# 3
# 4
# 5
# [In else block of while loop.]
# _________________________________________________________
