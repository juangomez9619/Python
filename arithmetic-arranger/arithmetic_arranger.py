from pythonlangutil.overload import Overload, signature


def arithmetic_arranger(problems, solve=None):

    if solve is None:  # first case
        if len(problems) > 5:
            return 'Error: Too many problems.'
        else:
            for strings in problems:
                operands = strings.split()
                if operands[1] != '+' and operands[1] != '-':
                    return "Error: Operator must be '+' or '-'."
                else:
                    try:
                        int(operands[0])
                        int(operands[2])
                    except:
                        return "Error: Numbers must only contain digits."
                    return 'valid data'

















    else:
        print('second')


