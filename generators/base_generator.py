import random
from faker import Faker

class BaseGenerator:
    def __init__(self):
        self.fake = Faker()

    def apply_unclean_options(self, value, unclean_types):
        options = {
            'null': lambda: None,
            'zero': lambda: 0,
            'negative': lambda: -1,
            'empty': lambda: '',
        }
        for unclean_type in unclean_types:
            if unclean_type in options and random.random() < 0.1:
                return options[unclean_type]()
        return value
