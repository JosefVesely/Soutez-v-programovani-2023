# Josef Veselý

def je_cele_cislo(num) -> bool:
    return float(num) % 1 == 0.0

def get_number(text):
    while True:
        num = input(text)
        num = num.replace(",", ".")

        # Je číslo zlomek?
        if "|" in num:
            citatel = num.split("|")[0]
            jmenovatel = num.split("|")[1]

            try:
                citatel = float(citatel)
                jmenovatel = float(jmenovatel)

                if jmenovatel == 0.0:
                    print("=> Chyba vstupu (čitatel se nesmí rovnat 0)")
                    continue

                return citatel / jmenovatel

            except ValueError: 
                print("=> Chyba vstupu (zlomek)")

        try:
            num = float(num)
            return num
        except ValueError: 
            print("=> Chyba vstupu")

def get_operand(text):
    while True:
        operand = input(text)
        if operand in ["+", "-", "*", "/"]:
            return operand
        else:
            print("=> Chyba vstupu")

def get_result(operand1, operator, operand2):
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        result = operand1 / operand2
    
    # Zbav se desetinné čárky, když je výsledek celé číslo
    if je_cele_cislo(result):
        result = int(result)
    return result


while True:
    operand1 = get_number("Operand 1: ")
    operator = get_operand("Operátor: ")
    operand2 = get_number("Operand 2: ")

    result = get_result(operand1, operator, operand2)


    print("-" * 10)
    print(f"Výsledek: {result}\n")