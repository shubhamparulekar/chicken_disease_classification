from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        prepare_base_model_config = ConfigurationManager().get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == '__main__':
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
