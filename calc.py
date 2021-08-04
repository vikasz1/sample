
print("Please enter two number with a space")
num = input().split()
print(num)
print("please choose an option\n1.Add\n2.Substract\n3.Multiply\n4.Divide")
op = int(input())

if op == 1:
    print(f"Addition : ",int(num[0])+int(num[1]))
elif op == 2:
    print("Substration : ",int(num[0])-int(num[1]))
elif op == 3:
    print("Multiplication : ",int(num[0])*int(num[1]))
elif op == 4:
    print("Division : ",int(num[0])/int(num[1]))