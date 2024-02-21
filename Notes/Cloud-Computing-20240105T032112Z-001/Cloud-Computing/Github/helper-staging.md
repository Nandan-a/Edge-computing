BHIoT$ git status 
On branch feature-div
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   calculator.py

BHIoT$ git restore --staged calculator.py

The most similar command is
	status
BHIoT$ git status
On branch feature-div
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   calculator.py

no changes added to commit (use "git add" and/or "git commit -a")

res_mul = mul(20,10)
print(res_mul)
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
res_div = div(num1,num2)
print(f"{num1} / {num2} = {res_div}")
-----------------------------------------------------------