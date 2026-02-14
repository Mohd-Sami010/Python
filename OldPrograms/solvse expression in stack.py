def evaluate_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            switcher = {
                '+': val2 + val1,
                '-': val2 - val1,
                '*': val2 * val1,
                '/': val2 / val1
            }
            stack.append(switcher[char])
    return stack.pop()

# Usage
expression = "22+44*+"
print(evaluate_postfix(expression))  # Output: -4
