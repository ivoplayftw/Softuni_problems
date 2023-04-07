from project.customer import Customer
from project.dvd import Dvd
from typing import List

class MovieWorld:
    class Customer:
        def __init__(self, name):
            self.name = name
            self.customers: List[Customer] = []
            self.dvds: List[Dvd] = []

    @staticmethod
    def dvd_capacity(capacity=15):
        return capacity

    @staticmethod
    def customer_capacity(capacity=10):
        return capacity

    def add_customer(self, customer)