import ricky.params
from ricky.utils import data_from_image
from pybrain.datasets import SupervisedDataSet


# while subclassing this works, we should try to detect the length of params
# and build a new data set for each type of params set...
# therefore, an instance of SupervisedDataSet could actually be
# accessed through the params instance...simplified one-to-one mapping

# we are limited to only one classifier per params instance as well
# however this is sort of a good thing, because built into the params
# class can be a method that randomizes params, and then evaluates

# we might be able to get this done through multiple inheritance
# keep all dataset related stuff in a separate class to make it better organized

# we need
# .evaluate
# .generate_liked_image
# .train_from_url_list
# .reset


class DataSet(SupervisedDataSet):

    @staticmethod
    def _file_into_list(self, filepath):
        f = open(filepath, "r")
        return f.read().split("\n")

    def _load_url_list(self, url_list, liked=False):
        target = 0
        if liked:
            target = 1
        data_list = [data_from_image(image) for image in url_list if image]
        for data in data_list:
            for params_class in ricky.params.Params.__subclasses__():
                if data['module'] == params_class.__name__:
                    params_instance = params_class()
                    params_instance.from_dict(data['params'])
                    self.addSample(
                        params_instance.as_normalized(),
                        target
                    )
