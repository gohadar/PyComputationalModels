from PyComputationalModels.operators.operator import Operator


class EqualsOperator(Operator):
    @staticmethod
    def get_operation(operand, result):
        return lambda x: x == result

    @staticmethod
    def get_type():
        return '=='
