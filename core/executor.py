from abc import ABC, abstractmethod
from core.helper import is_holiday, is_morning


class WorkTimeLogExecutor(ABC):

    def start(self):
        if not is_holiday():
            self.workday_log_message()
            self.load_login_page()
            self.login()
            self.timer_action()
            self.logout()
        else:
            self.holiday_log_message()

    @abstractmethod
    def workday_log_message(self):
        pass

    @abstractmethod
    def holiday_log_message(self):
        pass

    @abstractmethod
    def load_login_page(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    def timer_action(self):
        if is_morning():
            self.start_day()
        else:
            self.end_day()

    @abstractmethod
    def start_day(self):
        pass

    @abstractmethod
    def end_day(self):
        pass
