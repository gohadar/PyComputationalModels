from PyComputationalModels.operators.equals_operator import EqualsOperator as _EqualsOperator
from PyComputationalModels.operators.modulo_operator import ModuloOperator as _ModuloOperator
from PyComputationalModels.operators.non_equals_operator import \
    NonEqualsOperator as _NonEqualsOperator
from PyComputationalModels.operators.operator import Operator, NoSuchOperatorException

OPERATORS = {_ModuloOperator.get_type(): _ModuloOperator(),
             _EqualsOperator.get_type(): _EqualsOperator(),
             _NonEqualsOperator.get_type(): _NonEqualsOperator()}

MODULO_OPERATOR = OPERATORS[_ModuloOperator.get_type()]
EQUALS_OPERATOR = OPERATORS[_EqualsOperator.get_type()]
NON_EQUALS_OPERATOR = OPERATORS[_NonEqualsOperator.get_type()]


def get_operator_based_on_type(sign):
    """
    Get an operator based on the type

    Args:
        sign (str): the sign of the operator

    Returns:
        Operator: the operator
    """

    try:
        return OPERATORS[sign]
    except KeyError as e:
        raise NoSuchOperatorException(e)
