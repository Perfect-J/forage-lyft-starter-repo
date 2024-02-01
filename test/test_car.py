import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class TestCalliope(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()

    def test_battery_should_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        car = Calliope(last_service_date, 0, 0)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 1)
        car = Calliope(last_service_date, 0, 0)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = self.today
        car = Calliope(last_service_date, 30001, 0)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = self.today
        car = Calliope(last_service_date, 30000, 0)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()

    def test_battery_should_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        car = Glissade(last_service_date, 0, 0)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 1)
        car = Glissade(last_service_date, 0, 0)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = self.today
        car = Glissade(last_service_date, 60001, 0)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = self.today
        car = Glissade(last_service_date, 60000, 0)
        self.assertFalse(car.needs_service())


# Repeat the similar structure for other test classes (TestPalindrome, TestRorschach, TestThovex)

if __name__ == '__main__':
    unittest.main()
