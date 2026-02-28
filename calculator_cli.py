from stack import Stack

history = []

def evaluate(expression):

    stack = Stack()
    tokens = expression.split()

    for token in tokens:

        if token.isdigit():
            stack.push(int(token))

        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.push(a + b)

            elif token == '-':
                stack.push(a - b)

            elif token == '*':
                stack.push(a * b)

            elif token == '/':
                stack.push(a / b)

    return stack.pop()


def main():

    print("CLI Calculator using Stack")

    while True:

        exp = input("\nEnter postfix expression (or 'exit'): ")

        if exp == "exit":
            break

        result = evaluate(exp)

        history.append(result)

        print("Result:", result)
        print("History:", history)


if __name__ == "__main__":
    main()