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


class CalcBase:

    def __init__(self):
        self.operations = {
            '+': self._sum,
            '-': self._sub,
            '*': self._mul,
            '/': self._div,
            '%': self._mod,
            '^': self._pow
        }

    @staticmethod
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
            elif char in RIGHT_PARENTHESIS and stack:
                if stack.front() in LEFT_PARENTHESIS:
                    stack.pop()
                else:
                    return False

        return not stack

    def infix_notation_to_onp(self, infix_expresion: str) -> str:
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

        def operator_has_lower_priority(char: str) -> bool:
            return OPERATORS[operators.front()] >= OPERATORS[char]

        def is_left_parenthesis(char: str) -> bool:
            return char in LEFT_PARENTHESIS

        def is_right_parenthesis(char: str) -> bool:
            return char in RIGHT_PARENTHESIS

        def is_an_operator(char: str) -> bool:
            return char in OPERATORS

        def is_comma(char: str) -> bool:
            return char == '.'

        if not self.is_valid_brackets_count(infix_expresion):
            return ''

        infix_expresion = infix_expresion.rstrip()
        operators = Stack()
        out = []
        found_comma = False
        for char in infix_expresion:
            if char.isdecimal():
                if found_comma:  # liczba
                    out[-1] += char
                else:
                    out.append(char)
            elif is_comma(char):
                found_comma = True
                if out:
                    out[-1] += char
                else:
                    out.append('0.')
            elif is_left_parenthesis(char):  # '('
                found_comma = False
                operators.push(char)
            elif is_right_parenthesis(char):  # ')' '}' ']'
                found_comma = False
                while operators:
                    if not is_left_parenthesis(operators.front()):
                        out.append(operators.pop())
                    if is_left_parenthesis(operators.front()):
                        operators.pop()
                        break
            elif is_an_operator(char):  # operator
                found_comma = False
                while operators and operator_has_lower_priority(char):
                    out.append(operators.pop())
                operators.push(char)

        while operators:
            out.append(operators.pop())

        print(out)
        return ' '.join(out)

    @staticmethod
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
            if entry[0].isdecimal():
                counter += 1
            else:
                counter -= 1

        return counter != 0

    @staticmethod
    def _sum(a, b) -> float:
        return a + b

    @staticmethod
    def _mul(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def _div(a: float, b: float) -> [float, str]:
        if b != 0:
            return a / b
        else:
            return 'ZeroDivisionError'

    @staticmethod
    def _mod(a: int, b: int) -> [int, str]:
        if b != 0:
            return a % b
        else:
            return 'ZeroDivisionError'

    @staticmethod
    def _pow(a: float, b: float) -> float:
        return a ** b

    @staticmethod
    def _sub(a: float, b: float) -> float:
        return a - b

    def calc_onp(self, infix_expresion: str) -> [float, str]:
        """

        Args:
            infix_expresion: str - ONP string
        Returns:
            float: the result of the ONP operation
        """

        if self.is_valid_brackets_count(infix_expresion):
            onp_list = self.infix_notation_to_onp(infix_expresion).split(' ')
            stack = Stack()
            for entry in onp_list:
                if entry[0].isdecimal():
                    stack.push(float(entry))
                else:
                    val_1 = float(stack.pop())
                    val_2 = float(stack.pop())
                    result_value = self.operations[entry](val_2, val_1)
                    if result_value != 'ZeroDivisionError':
                        stack.push(result_value)
                    else:
                        return 'ZeroDivisionError'
            return stack.pop()


if __name__ == '__main__':
    s = "(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))"
    calc = CalcBase()
    print(calc.is_valid_brackets_count(s))

    s = "((())]"
    print(calc.is_valid_brackets_count(s))

    print('-' * 40)

    operation = '3 +4*3.2 /0+([2-1)+2}^2'
    result = calc.calc_onp(operation)
    print(f'wynik: calc_onp: {result}  - python: {3 + 4 * 3.2 / ((2 - 1) + 2) ** 2}')

    operation = '3+4*3/(2-1)+2^2'
    result = calc.calc_onp(operation)
    print(f'wynik: calc_onp: {result}  - python: {3 + 4 * 3 / (2 - 1) + 2 ** 2}')
