#Your task is to create a function that does four basic mathematical operations.
#The function should take three arguments - operation(string/char), value1(number), value2(number).
#The function should return result of numbers after applying the chosen operation.
#Examples(Operator, value1, value2) --> output
#('+', 4, 7) --> 11
#('-', 15, 18) --> -3
#('*', 5, 5) --> 25
#('/', 49, 7) --> 7
# Given code 
#def basic_op(operator, value1, value2):
def basic_op(operator, value1, value2):
    #your code here
        if operator == '+':
            return (value1 + value2)
        elif operator == '-':
            return (value1 - value2)
        elif operator == '*':
            return (value1 * value2)
        else:
            return (value1 / value2)
        
#import codewars_test as test
#from solution import basic_op

#@test.describe("Fixed Tests")
#def fixed_tests():
#    @test.it('Basic Test Cases')
#    def basic_test_cases():
#        test.assert_equals(basic_op('+', 4, 7), 11)
#        test.assert_equals(basic_op('-', 15, 18), -3)
#        test.assert_equals(basic_op('*', 5, 5), 25)
#        test.assert_equals(basic_op('/', 49, 7), 7)
#ДРУГИЕ ВАРКИ
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))

def basic_op(o, a, b):
    return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)

def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')

def basic_op(operator, value1, value2):
    ops = {'+': lambda a, b: a + b, 
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}
    return ops[operator](value1, value2)

from operator import add, div, mul, sub


def basic_op(op, a, b):
    return {'+': add, '/': div, '*': mul, '-': sub}[op](a, b)

def basic_op(op, v1, v2):
    return v1+v2 if op == "+" else v1-v2 if op == "-" else  v1*v2 if op == "*" else  v1/v2

def basic_op(operator, value1, value2):
    op = {
        '+' : (value1 + value2),
        '-' : (value1 - value2),
        '*' : (value1 * value2),
        '/' : (value1 / value2),
    }
    
    return op[operator]

import operator as op

OPERATIONS = {
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': op.div,
}

def basic_op(operator, value1, value2):
    return OPERATIONS[operator](value1, value2)

basic_op = lambda o, v1, v2: __import__("operator").__dict__[{"+":"add","-":"sub", "*":"mul", "/":"truediv"}[o]](v1,v2)

basic_op = lambda o, v1, v2: eval("{}{}{}".format(v1,o,v2))

def basic_op(*sheeps):
    hungry_wolf_eats = eval
    sheeps_in_order = '{1}{0}{2}'.format(*sheeps)
    return hungry_wolf_eats(sheeps_in_order)

import operator

def basic_op(operatorchar, value1, value2):
    return {'+':operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '%' : operator.mod,
        '^' : operator.xor
        }[operatorchar](value1,value2)
    
#САМОЕ ВЕРНОЕ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def basic_op(operator, value1, value2):
    try:
        return {
            '+': value1 + value2,
            '-': value1 - value2,
            '*': value1 * value2,
            '/': value1 / value2
        }.get(operator)
    except ZeroDivisionError:
        return None
#ИСКЛЮЧАЕТ ДЕЛЕНИЕ НА НОЛЬ