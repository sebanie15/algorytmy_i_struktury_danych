"""
Stos –Zadanie wykorzystujacestos : Zajęcia
•Częstym błedem w programowaniu jest brakujący lub zbyteczny dodatkowy nawias. Wykorzystując stos możemy napisać
 algorytm do weryfikacji czy wyrażenie zawiera poprawnie zapisane nawiasy.
•Wyrażenie ”((()))” jest poprawne. “(()” jest niepoprawne.
•W jaki sposób za pomocą stosu możemy rozwiązać ten problem?
•Jeżeli znak jest lewym nawiasem, dodaj go na stos w przeciwnym wypadku sprawdź czy na stosie znajduje się lewy nawias;
 jeżeli tak to usuń go i czytaj kolejny znak; jeżeli nie zwróć False.
 Wykonuj to dla wszystkich znaków w napisie. Sprawdź na końcu czy stos jest pusty. Dla“(()” zostanie na nim jeden
 element.
 Jeżeli pusty to zwróć True, jeżeli nie to False.
•Wersja dla ambitniejszych: Napis złożony z trzech rodzajów nawiasów {[( np: “{{[()]}}”
•Wersja dla ambitnych: Napis może składać się z białych znaków, liczb i operatorów matematycznych np:
    ”12   + (2 * 3) / 17 +     [2 + [2 * 2]]”.
    Dalej interesują nas tylko nawiasy. Należy wymyśleć sposób do wyciągania kolejnych nawiasów pomijając inne znaki.
"""

# ad.1

from structures.queues import Stack


LEFT_PARENTHESIS = {'(', '{', '['}
RIGHT_PARENTHESIS = {')', '}', ']'}
OPERATORS = {
    '(': 0,
    '{': 0,
    '[': 0,
    '+': 1,
    '-': 1,
    ')': 1,
    '}': 1,
    ']': 1,
    '*': 2,
    '/': 2,
    '%': 2,
    '^': 3
}


def is_valid_brackets_count(value: str) -> bool:
    """	checks that the parentheses are written in the correct order and number the function is not sensitive to
    different types of parentheses

    Args:
        value: str
    Returns:
        True: '()' or '[]' or '{}' or '(]' or '{)' etc.
        False: '(()' or '[]]' or '{{}' or '(])' or '{)}' etc.
    """
    stack = Stack[str]()

    for char in value:
        if char in LEFT_PARENTHESIS:
            stack.push(char)
        elif char in RIGHT_PARENTHESIS:
            if stack and stack.front() in LEFT_PARENTHESIS:
                stack.pop()
            else:
                return False

    return not stack


def infix_notation_to_onp(infix_expresion: str) -> str:
    """Algorytm konwersji z notacji infiksowej do ONP

    Edsger Dijkstra wymyślił algorytm nazywany „stacją rozrządową”, ponieważ jest w działaniu bardzo podobny do
    kolejowej stacji rozrządowej. Tak jak algorytm liczący wartość wyrażenia ONP, ten także działa na bazie stosu.
    Do konwersji używane są dwie zmienne (typu ciągu znakowego) — wejście oraz wyjście. Jest także stos przechowujący
    operatory niedodane jeszcze do wyjścia. W uproszczeniu, program czyta po kolei każdą literę i wykonuje operację
    zależną od tej litery.

    Szczegóły algorytmu

    1. Póki zostały symbole do przeczytania wykonuj:

    2. Przeczytaj symbol.

        - Jeśli symbol jest liczbą dodaj go do kolejki wyjście.
        - Jeśli symbol jest funkcją włóż go na stos.
        - Jeśli symbol jest znakiem oddzielającym argumenty funkcji (np. przecinek):

            - Dopóki najwyższy element stosu nie jest lewym nawiasem, zdejmij element ze stosu i dodaj go do kolejki
              wyjście. Jeśli lewy nawias nie został napotkany oznacza to, że znaki oddzielające zostały postawione w
              złym miejscu lub nawiasy są źle umieszczone.

        - Jeśli symbol jest operatorem, o1, wtedy:

            1) dopóki na górze stosu znajduje się operator, o2 taki, że:

                        o1 jest lewostronnie łączny i jego kolejność wykonywania jest mniejsza lub równa kolejności
                        wyk. o2,
                        lub
                        o1 jest prawostronnie łączny i jego kolejność wykonywania jest mniejsza od o2,

                zdejmij o2 ze stosu i dołóż go do kolejki wyjściowej i wykonaj jeszcze raz 1)

            2) włóż o1 na stos operatorów.

        - Jeżeli symbol jest lewym nawiasem to włóż go na stos.
        - Jeżeli symbol jest prawym nawiasem to zdejmuj operatory ze stosu i dokładaj je do kolejki wyjście, dopóki
          symbol na górze stosu nie jest lewym nawiasem, kiedy dojdziesz do tego miejsca zdejmij lewy nawias ze stosu
          bez dokładania go do kolejki wyjście. Teraz, jeśli najwyższy element na stosie jest funkcją, także dołóż go do
          kolejki wyjście. Jeśli stos zostanie opróżniony i nie napotkasz lewego nawiasu, oznacza to, że nawiasy zostały
          źle umieszczone.

    Jeśli nie ma więcej symboli do przeczytania, zdejmuj wszystkie symbole ze stosu (jeśli jakieś są) i dodawaj je do
    kolejki wyjścia. (Powinny to być wyłącznie operatory, jeśli natrafisz na jakiś nawias oznacza to, że nawiasy zostały
     źle umieszczone.)

    Args:
        infix_expresion:

    Returns:
        str:
    """

    if not is_valid_brackets_count(infix_expresion):
        return ''

    infix_expresion = infix_expresion.rstrip()
    print(infix_expresion)
    stack = Stack()
    out = []
    comma = False
    for element in infix_expresion:
        if element.isdecimal() and not comma:  # liczba
            out.append(element)
        elif element.isdecimal() and comma:
            out[-1] += element
        elif element == '.':
            comma = True
            if out:
                out[-1] += element
            else:
                out.append('0.')
        elif element in LEFT_PARENTHESIS:  # '('
            comma = False
            stack.push(element)
        elif element in RIGHT_PARENTHESIS:  # ')' '}' ']'
            comma = False
            while stack:
                if not stack.front() in LEFT_PARENTHESIS:
                    out.append(stack.pop())
                if stack.front() in LEFT_PARENTHESIS:
                    stack.pop()
                    break
        elif element in OPERATORS:  # operator
            comma = False
            while stack and OPERATORS[stack.front()] >= OPERATORS[element]:
                out.append(stack.pop())
            stack.push(element)

    while stack:
        out.append(stack.pop())

    print(out)
    return ' '.join(out)


def is_valid_onp(onp: str) -> bool:
    """method checks if the given ONP string is correct

    Args:
        onp: str (ONP string)
    Returns:
        True: if onp is correct ONP string
    """
    onp = onp.split(' ')
    counter = 0
    for entry in onp:
        if entry.isdecimal():
            counter += 1
        else:
            counter -= 1

    return counter != 0


def calc_onp(infix_expresion: str) -> float:
    """

    Args:
        infix_expresion: str - ONP string
    Returns:
        float: the result of the ONP operation
    """

    def _calc_operation(operator: str, val_1: float, val_2: float) -> float:
        if operator == '+':
            return val_2 + val_1
        elif operator == '-':
            return val_2 - val_1
        elif operator == '*':
            return val_2 * val_1
        elif operator == '/':
            if val_1 != 0:
                return val_2 / val_1
        # TODO: raise exception or something else ;)
        elif operator == '%':
            return val_2 % val_1
        elif operator == '^':
            return val_2 ** val_1
        elif operator == '*':
            return val_2 * val_1

    if is_valid_brackets_count(infix_expresion):
        onp_list = infix_notation_to_onp(infix_expresion).split(' ')
        print(onp_list)
        stack = Stack()
        for entry in onp_list:
            if entry[0].isdecimal():
                stack.push(float(entry))
            else:
                stack.push(_calc_operation(entry, float(stack.pop()), float(stack.pop())))
        return stack.pop()


if __name__ == '__main__':
    s = "(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))"
    print(is_valid_brackets_count(s))

    s = "((())]"
    print(is_valid_brackets_count(s))

    print('-' * 40)

    operation = '3 +4*3.2 /([2-1)+2}^2'
    result = calc_onp(operation)
    print(f'wynik: calc_onp: {result}  - python: {3 + 4 * 3.2 / ((2 - 1) + 2) ** 2}')

    operation = '3+4*3/(2-1)+2^2'
    result = calc_onp(operation)
    print(f'wynik: calc_onp: {result}  - python: {3 + 4 * 3 / (2 - 1) + 2 ** 2}')
