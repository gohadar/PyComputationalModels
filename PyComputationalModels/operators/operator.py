import abc


class NoSuchOperatorException(Exception):
    pass


class Operator(object):
    __metaclass__ = abc.ABCMeta

    @staticmethod
    @abc.abstractmethod
    def get_operation(operand, result):
        """
        Get the operation using the operator

        Returns:
            function: the operation
        """

    @staticmethod
    @abc.abstractmethod
    def get_type():
        """
        Get the type of the operator

        Returns:
            str: the operator sign/s
        """

    def __str__(self):
        return self.get_type()

    def __repr__(self):
        return str(self)
