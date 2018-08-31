from PyComputationalModels.condition import Condition


class State(object):
    def __init__(self, name, conditions):
        """
        Args:
            name (str): the name of the state
            conditions (list[Condition]): the list of the conditions that represent the state
        """

        self._name = name
        self._conditions = conditions

    def get_name(self):
        """
        Returns:
            str: the name of the state
        """
        return self._name

    def get_conditions(self):
        """
        Returns:
            list[Condition]: the list of the conditions
        """
        return self._conditions

    def get_args_values(self):
        """
        Get the args values at the state

        Returns:
            dict[str: int]: the args values
        """
        return {condition.get_arg(): condition.get_result() for condition in self._conditions}

    def __str__(self):
        return 'State(name:{name}, conditions:{conditions})'.format(name=self._name,
                                                                    conditions=self._conditions)

    def __repr__(self):
        return str(self)
