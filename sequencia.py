def validarSequencia(sequence):
    pilha = []
    for c in sequence:
        if c == '(':
            pilha.append(c)
        elif c == '{':
            pilha.append(c)
        elif c == '[':
            pilha.append(c)
        elif len(pilha) == 0:
            return False
        elif c == ')':
            if pilha.pop() != '(':
                return False
        elif c == '}':
            if pilha.pop() != '{':
                return False
        elif c == ']':
            if pilha.pop() != '[':
                return False
    return True


print(validarSequencia("[](){}[{()}]"))