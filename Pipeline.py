class Pipeline:
    """
    Pipeline data through multiple steps
    Register handlers and events that manipulate data in different ways
    """

    def __init__(self, pipeline = []):
        self.pipeline = pipeline

    def pipe(self, fn):
        """
        Returns a new pipeline with a new step
        :param fn: The function to apply to data, should take data and return new data
        :return: New pipeline with the new step
        """
        return Pipeline(self.pipeline + [fn])

    def split(self, check, fn_if_true, fn_if_false):
        """
        Returns a new pipeline with a new conditional step
        :param check: The conditional to check the data with
        :param fn_if_true: The function to apply to data if check returns true, should take data and return new data
        :param fn_if_false: The function to apply to data if check returns false, should take data and return new data
        :return: New pipeline with the new step
        """
        return Pipeline(self.pipeline + [lambda x: fn_if_true if check(x) else fn_if_false])

    def apply(self, data):
        """
        Apply the pipeline to the given data, step by step as specified
        :param data: the data to apply the pipeline to
        :return: result The result of applying the steps to data
        """
        for step_fn in self.pipeline:
            data = step_fn(data)
        return data
