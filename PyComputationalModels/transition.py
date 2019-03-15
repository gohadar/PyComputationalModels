from PyComputationalModels.state import State


class Transition(object):
    def __init__(self, start, end, bi_directional):
        """
        Args:
            start (State): the start state of the transition
            end (State): the end state of the transition
            bi_directional (bool): is bi-directional
        """

        self._start = start
        self._end = end
        self._bi_directional = bi_directional

    def get_start_state(self):
        """
        Returns:
            State: the start state
        """
        return self._start

    def get_end_state(self):
        """
        Returns:
            State: the end state
        """
        return self._end

    def is_bi_directional(self):
        """
        Returns:
            bool: is the transition bi-directional
        """
        return self._bi_directional

    def __str__(self):
        return 'Transition(start:{start}, end:{end}, bi-directional:{bi_directional})'. \
            format(start=self._start, end=self._end, bi_directional=self._bi_directional)

    def __repr__(self):
        return str(self)
