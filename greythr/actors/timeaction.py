import logging
import time
from core.actor import Actor
from greythr.actors.scripts import FINDER_CLASS
from greythr.actors.scripts import SIGN_OUT_EXISTS, SIGN_OUT_CLICK
from greythr.actors.scripts import SIGN_IN_EXISTS, SIGN_IN_CLICK


class SignInActor(Actor):
    def act(self, driver):
        result: bool = False
        for i in range(3):
            result = driver.execute_script(FINDER_CLASS + SIGN_IN_EXISTS)
            if not result:
                logging.info("start day button not found")
                time.sleep(5.0)
            else:
                logging.info("start day button loaded")
                break
        driver.execute_script(FINDER_CLASS + SIGN_IN_CLICK)


class SignOutActor(Actor):
    def act(self, driver):
        result: bool = False
        for i in range(3):
            result = driver.execute_script(FINDER_CLASS + SIGN_OUT_EXISTS)
            if not result:
                logging.info("end day button not found")
                time.sleep(5.0)
            else:
                logging.info("end day button loaded")
                break
        driver.execute_script(FINDER_CLASS + SIGN_OUT_CLICK)
