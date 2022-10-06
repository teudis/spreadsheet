"""Programming assignment for NORITEX.com software engineering position.

Su tarea es IMPLEMENTAR la función evaluate() a continuación para la especificación
proporcionado en la cadena de documentación.
Si cree que las funciones auxiliares serían útiles, no dude en
escríbelos Puede cambiar cualquier cosa en este archivo, excepto que no está permitido
para alterar el nombre o la firma de la función de evaluación ().

Aunque le proporcionamos algunos casos de prueba, no asuma que estos cubren
todos los casos de esquina, y podemos usar un conjunto diferente de entradas para validar su
solución. Analizaremos su solución tanto para la corrección como para
estilo.

----------------------------------------------

Your task is to implement the function evaluate() below to the specification
provided in the documentation string.
If you feel that auxiliary helper functions would be helpful, feel free to
write them. You may change anything in this file except you are not permitted
to alter the name or function signature of evaluate().

Although we provide you with some test cases, do not assume that these cover
all corner cases, and we may use a different set of inputs to validate your
solution. We will be looking at your solution both for correctness and for
style.

Best of luck!
"""
import string
import re
alpha_list = list(string.ascii_uppercase)

def format_curren_pos(cad: str) -> str:
    """Function for Remove spaces and Upper the String
    :param cad : String to format
    :return: String formatted without being =
    """
    cad = cad.upper()
    cad = cad.replace(" ", "")
    return cad[1:]


def format_cell(cad: str):
    """
    Function convert cell to point in the matrix, for example A1 to 0,0
    :param cad: Strinng to convert
    :return:  two values position the letter and number of string
    """
    letter = cad[0]
    cad = cad.upper()
    cad = cad.replace(" ", "")
    pos_letter = alpha_list.index(letter)
    number = int(cad[1]) - 1
    return number, pos_letter


def operation_cell(first_value: int, second_value: int, operator):
    """
    Function for calculate the operation
    :param first_value:
    :param second_value:
    :param operator:
    :return: total is the result of the operations between first_value and second_value
    """
    if operator == "+":
        total: int = first_value + second_value
        return total
    elif operator == "-":
        total = first_value - second_value
        return total
    elif operator == "*":
        total = first_value * second_value
        return total
    else:
        # validate division zero
        try:
            total = first_value / second_value
            return total
        except ZeroDivisionError:
            raise ZeroDivisionError


def validate_cell(expression: str) -> bool:
    """
    Function for validate expression in cell
    :param expression: String to evaluate expression in cell
    :return: True or False, if expression is correct return True else return False
    """
    exp_formatted = format_curren_pos(expression)
    letters_exp = "[A-Z]{1}[0-9]+"   
    number_exp = "([0-9]+.[0-9]+|[0-9]+)"
    full_number_expr = "-"+number_exp+"|"+number_exp
    itemRegex = " *("+letters_exp+"|"+full_number_expr+")"
    all_exp = re.match("(("+itemRegex+" *[+\\-*/]{1}"+itemRegex+")|"+full_number_expr+")", exp_formatted) 
    if all_exp :
        return True
    else:
         return False


# =============================================================================
#
# Implement this function
#
# =============================================================================

def evaluate(matriz):
    """Evaluate all of the values in the spreadsheet.

    Given a matrix m of "arbitrary" size, evalute all of the cells in the
    spreadsheet and return the matrix with everything computed. We will assume
    that columns are denoted using a letter while rows are denoted by numbers.
    E.g "A1" is equivalent to ``m[0][0]`` while "C23" is ``m[22][2]``. 

    As such, here are some examples, assume we have the matrix:

        1   2
        3   4

    This, obviously, should just return the same matrix. Now, let's add some
    functions:

        1   =A1
        2   =A2 + 1

    This should evalute to:

        1   1
        2   3

    Now, let's take this one step further and add in a second level of
    reference:

        1           =A1 + 1
        =B1 + 1     =A2 + B1

    This should evalute to:

        1   2
        3   5

    If you are given a reference to a cell that has not been defined, you
    should raise a ReferenceError. For example, this should not work:

        1           =A5 + 2
        =B1 + 1     =A2 + 1

    If you find circular references, you should raise a ValueError. For example:

        =B1 + 1     =A1 + 1

    You can assume the following:
        - All "functions" will have = as the first character
        - The only operations that will be peformed are +, -, *, /
        - All input numbers will be integers (you may have some floats as a 
          result of division, however)
        - Each "function" will only be a direct reference or binary operation.
          I.e. It'll either be something like "=A1" or "=A1 + 1" but not
          "=A1 + 1 + 2"
        - Spaces in "functions" are meaningless. I.e. "=A1 + 1" is the same as
          "=A1+1" or "= A1  +   1". However, a negative sign must appear 
          right in front of the number. E.g. "=A1 +   -1" is valid, but
          "=A1 +  -  1" is not
        - There will be no column that goes past "Z" and capitalization in
          column names is ignored. I.e. "A1" is the same as "a1".

    :param matriz: The matrix to be evaluated. Each of the entries in the matrix
              will either be numbers or strings.
    :returns: A matrix of the same dimensions as :attr:`m` with all of the
              functions evaluated. All of the entries in this returned matrix
              should be numeric and not strings.
    :raises:
        :ValueError: If there is a problem parsing any of the input values
        :ReferenceError: If a cell is referenced that has not been defined
        :ValueError: If there is a circular reference
        :ZeroDivisionError: If there is a divide by zero
    
    --------------SPANISH ---------------------
    
    Evaluar todos los valores en la hoja de cálculo.

    Dada una matriz m de tamaño "arbitrario", evalúe todas las celdas en el
    hoja de cálculo y devolver la matriz con todo lo calculado. Asumiremos
    que las columnas se denotan con una letra, mientras que las filas se denotan con números.
    Por ejemplo, "A1" es equivalente a `` m [0] [0] `` mientras que "C23" es `` m [22] [2] ``.

    Como tal, aquí hay algunos ejemplos, supongamos que tenemos la matriz:

        1 2
        3 4

    Esto, obviamente, debería devolver la misma matriz. Ahora, agreguemos algunos
    funciones:

        1 = A1
        2 = A2 + 1

    Esto debería evaluar a:

        1 1
        2 3

    Ahora, vamos un paso más allá y agreguemos un segundo nivel de
    referencia:

        1 = A1 + 1
        = B1 + 1 = A2 + B1

    Esto debería evaluar a:

        1 2
        3 5

    Si se le da una referencia a una celda que no se ha definido, usted
    debería generar un ReferenceError. Por ejemplo, esto no debería funcionar:

        1 = A5 + 2
        = B1 + 1 = A2 + 1

    Si encuentra referencias circulares, debe generar un ValueError. Por ejemplo:

        = B1 + 1 = A1 + 1

    Puede asumir lo siguiente:
        - Todas las "funciones" tendrán = como primer carácter
        - Las únicas operaciones que se realizarán son +, -, *, /
        - Todos los números de entrada serán enteros (puede tener algunos flotantes como
          resultado de la división, sin embargo)
        - Cada "función" solo será una referencia directa o una operación binaria.
          Es decir. Será algo así como "= A1" o "= A1 + 1" pero no
          "= A1 + 1 + 2"
        - Los espacios en "funciones" no tienen sentido. Es decir. "= A1 + 1" es lo mismo que
          "= A1 + 1" o "= A1 + 1". Sin embargo, debe aparecer un signo negativo
          justo en frente del número. P.ej. "= A1 + -1" es válido, pero
          "= A1 + - 1" no es
        - No habrá columna que pase la "Z" y las mayúsculas en
          los nombres de columna se ignoran. Es decir. "A1" es lo mismo que "a1".

    : param m: La matriz a evaluar. Cada una de las entradas en la matriz
              serán números o cadenas.
    : devuelve: Una matriz de las mismas dimensiones que: attr: `m` con todos los
              funciones evaluadas. Todas las entradas en esta matriz devuelta
              debe ser numérico y no cadenas.
    : plantea:
        : ValueError: si hay un problema al analizar cualquiera de los valores de entrada
        : ReferenceError: si se hace referencia a una celda que no se ha definido
        : ValueError: si hay una referencia circular
        : ZeroDivisionError: si hay una división entre cero
    "" "
    """
    for row_matriz in range(len(matriz)):
        for pos in range(len(matriz[row_matriz])):
            current_value = matriz[row_matriz][pos]  
            #Check Value None in cell
            if current_value == None:
                raise ValueError            
            # Check if the cell is a String
            if type(current_value) == str and len(current_value) > 1:
                 
                # Check invalid format in cell             
                #if not validate_cell(current_value):
                #    raise ValueError 
                try:
                    # Check if the operation in the cell first element is a number
                    if current_value[1].isnumeric() or (current_value[1]=="-" and current_value[2].isnumeric()):
                        current_value = format_curren_pos(current_value)
                        if len(current_value.split("+")) > 1:
                            pos_operator = current_value.index("+")
                            first_value = current_value[0:pos_operator]
                            if current_value[pos_operator + 1].isnumeric():
                                second_value = current_value[pos_operator + 1:]
                                total = int(first_value) + int(second_value)
                                matriz[row_matriz][pos] = total
                            else:
                                second_value = current_value[pos_operator + 1:]
                                number, letter = format_cell(second_value)
                                second_value_end = matriz[number][letter]
                                total = int(first_value) + second_value_end
                                matriz[row_matriz][pos] = total
                        elif len(current_value.split("-")) > 1:
                            pos_operator = current_value.index("-")
                            first_value = int(current_value[0:pos_operator])
                            if current_value[pos_operator + 1].isnumeric():
                                second_value = current_value[pos_operator + 1:]
                                total = int(first_value) - int(second_value)
                                matriz[row_matriz][pos] = total
                            else:
                                second_value = current_value[pos_operator + 1:]
                                number, letter = format_cell(second_value)
                                second_value_end = matriz[number][letter]
                                total = int(first_value) - second_value_end
                                matriz[row_matriz][pos] = total
                        elif len(current_value.split("*")) > 1:
                            pos_operator = current_value.index("*")
                            first_value = int(current_value[0:pos_operator])
                            if current_value[pos_operator + 1].isnumeric():
                                second_value = current_value[pos_operator + 1:]
                                total = int(first_value) * int(second_value)
                                matriz[row_matriz][pos] = total
                            else:
                                second_value = current_value[pos_operator + 1:]
                                number, letter = format_cell(second_value)
                                second_value_end = matriz[number][letter]
                                total = int(first_value) * second_value_end
                                matriz[row_matriz][pos] = total
                        else:
                            pos_operator = current_value.index("/")
                            first_value = int(current_value[0:pos_operator])
                            # validate division zero
                            try:
                                if current_value[pos_operator + 1].isnumeric():
                                    second_value = current_value[pos_operator + 1:]
                                    total = int(first_value) / int(second_value)
                                    matriz[row_matriz][pos] = total
                                else:
                                    second_value = current_value[pos_operator + 1:]
                                    number, letter = format_cell(second_value)
                                    second_value_end = matriz[number][letter]
                                    total = int(first_value) / second_value_end
                                    matriz[row_matriz][pos] = total
                            except ZeroDivisionError:
                                raise ZeroDivisionError


                    else: # Check if value in the cell in the format [a-z]*[1-9]{1}
                        current_value = format_curren_pos(current_value)
                        if len(current_value) == 2 :
                            number, pos_letter = format_cell(current_value)
                            matriz[row_matriz][pos] = matriz[number][pos_letter]
                        else:
                            letter = current_value[:2]
                            operator = current_value[2]
                            other_value = current_value[3:]
                            if len(other_value) == 1 or other_value[0]=="-":
                                second_value = int(other_value)
                                number, pos_letter = format_cell(letter)
                                first_value = matriz[number][pos_letter]
                                total = operation_cell(first_value, second_value, operator)
                                matriz[row_matriz][pos] = total
                            else:
                                first_letter = current_value[:2]
                                operator = current_value[2]
                                second_letter = current_value[3:]
                                number_first_letter, first_pos_letter = format_cell(first_letter)
                                first_value = matriz[number_first_letter][first_pos_letter]
                                number_second, pos_letter_second = format_cell(second_letter)
                                second_value = int(matriz[number_second][pos_letter_second])
                                total = operation_cell(first_value, second_value, operator)
                                matriz[row_matriz][pos] = total
                except IndexError:
                    raise ReferenceError
            # Case when the expression in the cell is a number
            else:
                print(current_value)
                current_value = int(current_value)
                matriz[row_matriz][pos] = current_value

    return matriz



# =============================================================================
#
# Some example inputs and solutions to test against
#
# =============================================================================

testcase = []
solution = []


# Case: simple spreadsheet with strings and ints
testcase.append(
    [
        [1, "2"],
        ["3", 4]
    ]
)
solution.append (
    [
        [1, 2],
        [3, 4]
    ]
)

# Case: simple (non-recursive) formulas
testcase.append(
    [
        [1, "=A1+1"],
        [3, "=A2+1"]
    ]
)
solution.append(
    [
        [1, 2],
        [3, 4]
    ]
)

testcase.append(
    [
        [1, "=1-1"],
        [3, "=A2+1"]
    ]
)
solution.append(
    [
        [1, 0],
        [3, 4]
    ]
)


# Case: formulas referencing two cells
testcase.append(
    [
        [1,     "=A1+1", "=A1 + B1"],
        ["=B1", "3",     "=C1 + B2"]
    ]
)
solution.append(
    [
        [1, 2, 3],
        [2, 3, 6]
    ]
)

# Cases: formula referencing cells out of range
testcase.append(
    [
        [1,         "=A5 + 2"],
        ["=B1 + 1", "=A2 + 1"]
    ]
)
solution.append(ReferenceError)

testcase.append([ [1, "=C1"] ])
solution.append(ReferenceError)

# Case: circular dependencies
testcase.append(
    [
        ["=B1 + 1", "=A1 + 1"]
    ]
)
solution.append(ValueError)

# Case: highly recursive spreadsheet, all operations represented
testcase.append(
    [
        [ "=C1+5", "=A3/2", "=c2-1" ],
        [ "=b3+7",       1, "=B1*4" ],
        [ "=B2+5", "=a1/5", "=A2-2" ]
    ]
)
solution.append(
    [
        [ 16,   3,   11   ],
        [ 10.2, 1,   12   ],
        [  6,   3.2,  8.2 ]
    ]
)

# Cases: malformed formulas
testcase.append([ [ 1, "=A1 +" ] ] )
solution.append(ValueError)

testcase.append([ [ 1, "=A1+5+6+7" ] ])
solution.append(ValueError)

testcase.append([ [ 1, "=A1 $ A1" ] ])
solution.append(ValueError)

# Case: division by zero
testcase.append([ [ 1, "=A1 - 1", "=A1 / B1" ] ])
solution.append(ZeroDivisionError)

# Case: negative numbers
testcase.append([ [ 1, "=A1 * -1" ] ])
solution.append([ [ 1, -1 ] ])

testcase.append([ [ -1, "=A1 * -5" ] ])
solution.append([ [ -1, 5 ] ])

testcase.append([ [ 1, "=-2 + a1" ] ])
solution.append([ [ 1, -1 ] ])

testcase.append([ [ 1, "=A1 + -5" ] ])
solution.append([ [ 1, -4 ] ])

testcase.append([ [ 1, "=A-1 + 1" ] ])
solution.append(ValueError)

testcase.append([ [ 1, "=-A1 + 1" ] ])
solution.append([ [ 1, 0 ] ])

# Case: Errors in input
testcase.append([ [ -1, "=A1 + - 5" ] ])
solution.append(ValueError)

testcase.append([ [ "" ] ])
solution.append(ValueError)

testcase.append([ [ None ] ])
solution.append(ValueError)

testcase.append([ [ None, "=A1" ] ])
solution.append(ValueError)

testcase.append([ [ "A1" ] ])
solution.append(ValueError)

def validate(proposed, actual):
    """Check if the proposed solution is the same as the actual solution.

    Feel free to modify this function as we will be testing your code with
    our copy of this function.

    :param proposed: The proposed solution
    :param actual: The actual solution
    :return: True if they are the same. Else, return False.
    """
    if proposed is None:
        print ("Oops! Looks like your proposed result is None.")
        return False
    proposed_items = [item for sublist in proposed for item in sublist]
    actual_items = [item for sublist in actual for item in sublist]
    if len(proposed_items) != len(actual_items):
        print ("Oops! There don't seem to be the same number of elements.")
        return False
    if proposed_items != actual_items:
        print ("Oops! Looks like your proposed solution is not right...")
        return False
    return True


# =============================================================================
#
# A simple main function for you to run. You should be able to test your
# implementation by simply running this module. E.g.
#   python spreadsheet.py
#
# =============================================================================

def print_error(solution, result):
    """Helper to print the error string"""
    print ("    Expected {}({}), got {}({})".format(
        type(solution), solution, type(result), result))

 
if __name__ == '__main__':
    """The main entry point for this module.

    The main entry point for the function that runs a couple tests to validate
    the implementation of evaluate().
    """

    # The number of test cases that are correct
    correct = 0

    for i in range(len(testcase)):

        print ("Test {}.".format(i))
        
        try:
            result = evaluate(testcase[i])
        except Exception as exc:
            result = exc

        # If the result is a matrix, make sure we were expecting a matrix
        if isinstance(result, list):
            if isinstance(solution[i], list):
                if validate(result, solution[i]):
                    print ("    OK.")
                    correct += 1
                else:
                    print ("    Results don't match")
            else:
                print_error(solution[i], result)

        # If the result is an error, make sure we were expecting an error
        else:
            if isinstance(solution[i], list):
                print_error(solution[i], result)
            else:
                if result.__class__ == solution[i]:
                    print ("OK.")
                    correct += 1
                else:
                    print_error(solution[i], result)

    print ("------------------------------------------------------")
    print ("You got {} out of {} correct.".format(correct, len(testcase)))
