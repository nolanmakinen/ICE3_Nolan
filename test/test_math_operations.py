import unittest
from ICE3.src.temperature_sensor import process_temperatures

class TestTemperatureSensor(unittest.TestCase):

    def test_boundary_values(self):
        self.assertEqual(process_temperatures([-50]), "Min: -50.0°C, Max: -50.0°C, Avg: -50.0°C")
        self.assertEqual(process_temperatures([150]), "Min: 150.0°C, Max: 150.0°C, Avg: 150.0°C")
        self.assertEqual(process_temperatures([-49, 149]), "Min: -49.0°C, Max: 149.0°C, Avg: 50.0°C")

    def test_robustness(self):
        self.assertEqual(process_temperatures([-60, 20, 160]), "Out-of-bound value detected.")
        self.assertEqual(process_temperatures([20, "abc", 30]), "Invalid input detected.")
        self.assertEqual(process_temperatures([10, "@", -40]), "Invalid input detected.")

    def test_special_cases(self):
        self.assertEqual(process_temperatures([2**3 - 1, -2**31]), "Out-of-bound value detected.")
        self.assertEqual(process_temperatures([50, 50, 50]), "Min: 50.0°C, Max: 50.0°C, Avg: 50.0°C")
        self.assertEqual(process_temperatures([]), "No input provided.")

    def test_unsorted_valid_temperatures(self):
        self.assertEqual(process_temperatures([30, 20, 10]),"Min: 10.0°C, Max: 30.0°C, Avg: 20.0°C")
