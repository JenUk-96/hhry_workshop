from abc import ABC, abstractmethod


class BaseSaveFile(ABC):
    """ Абстрактный класс инициализации пути до файла, для записи """

    @abstractmethod
    def __init__(self, file_worker):
        self.file_wworker = file_worker


class BaseLoadVacancies(ABC):
    """ Абстрактный класс для создания метода, получение вакансий по ключевому слову """

    @abstractmethod
    def __init__(self, keyword):
        pass
