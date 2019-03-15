from PyComputationalModels.operators.operator import Operator


class ModuloOperator(Operator):
    @staticmethod
    def get_operation(operand, result):
        return lambda x: x % operand == result

    @staticmethod
    def get_type():
        return '%'
