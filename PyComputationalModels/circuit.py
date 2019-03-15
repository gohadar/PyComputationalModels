from PyComputationalModels.state import State


class Circuit(object):
    def __init__(self, states, transitions):
        self._states = states
        self._transitions = transitions

    def get_states(self):
        """
        Returns:
            list[State]: the states
        """
        return self._states

    def get_transitions(self):
        """
        Returns:
            list[Transition] the transitions
        """
        return self._transitions

    def get_state(self, name):
        """
        Get a state based on it's name

        Args:
            name (str): the states name

        Returns:
            State: the state
        """

        for state in self._states:
            if state.get_name() == name:
                return state

        raise IndexError('No state by the name {name} exists in this circuit'.format(name=name))

    def __str__(self):
        return 'Circuit(states:{states}, transitions:{transitions})'. \
            format(states=self._states, transitions=self._transitions)
