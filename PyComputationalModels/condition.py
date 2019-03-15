from PyComputationalModels.operators.operator import Operator


class Condition(object):
    def __init__(self, arg, operator, operand, result):
        """
        Create a condition

        Args:
            arg (str): the char that the condition applies to
            operator (Operator): the operator of the condition
            operand (int | None): the operand of the condition, None if there is no operand
            result (int): the result of the condition
        """
        self._arg = arg
        self._operator = operator
        self._operand = operand
        self._result = result

        self._operation = self._operator.get_operation(self._operand, self._result)

    def get_operation(self):
        """
        Returns:
            function: the operation of the condition
        """
        return self._operation

    def get_arg(self):
        """
        Returns:
            str: the arg
        """
        return self._arg

    def get_result(self):
        """
        Returns:
            int: the result
        """
        return self._result

    def __str__(self):
        return 'Condition(arg:{arg}, operator:{operator}, operand:{operand}, result:{result})'. \
            format(arg=self._arg, operator=self._operator, operand=self._operand,
                   result=self._result)

    def __repr__(self):
        return str(self)
