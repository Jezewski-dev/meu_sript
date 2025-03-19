while True:
	num1 = int(input("Digite o primeiro número: "))
	op = input("Digite a operação")
	num2 = int(input("Digite o segundo número: "))

	if op == "+":
	   resultado = num1 + num2
	elif op == "-":
	   resultado = num1 - num2
	elif op == "*":
	   resultado = num1 * num2
	elif op == "/":
	   resultado = num1 / num2
	else:
	   print("Operação inválida")

	print("{} {} {} = {}".format(num1, op, num2, resultado))
