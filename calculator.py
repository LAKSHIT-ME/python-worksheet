def evaluate_expression(expression):
    expression = expression.replace(" ", "")

    def apply_operation(operands, operator):
        a = operands.pop()
        b = operands.pop()
        if operator == '+':
            operands.append(b + a)
        elif operator == '-':
            operands.append(b - a)
        elif operator == '*':
            operands.append(b * a)
        elif operator == '/':
            operands.append(b / a)
        elif operator == '^':
            operands.append(b ** a)

    def evaluate(tokens):
        operands = []
        operators = []
        i = 0

        while i < len(tokens):
            if tokens[i].isdigit():
                while i < len(tokens) and tokens[i].isdigit():
                    num = num * 10 + int(tokens[i])
                    i += 1
                operands.append(num)
                i -= 1
            elif tokens[i] == '(':
                operators.append(tokens[i])
            elif tokens[i] == ')':
                while operators and operators[-1] != '(':
                    apply_operation(operands, operators.pop())
                operators.pop()
            elif tokens[i] in '+-*/^':
                while (operators and operators[-1] in "+-*/^" and
                       precedence(operators[-1]) >= precedence(tokens[i])):
                    apply_operation(operands, operators.pop())
                operators.append(tokens[i])
            i += 1

        while operators:
            apply_operation(operands, operators.pop())

        return operands[-1]

    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        if op == '^':
            return 3
        return 0

    tokens = list(expression)
    return evaluate(tokens)

expression = input("Enter a mathematical expression: ")
result = evaluate_expression(expression)
print(f"Result of '{expression}' is: {result}")
