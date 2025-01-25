from .base_generator import BaseGenerator
import random

class AppleGenerator(BaseGenerator):
    def generate(self, count, unclean_types):
        data = []
        for _ in range(count):
            data.append({
                'user_name': self.apply_unclean_options(self.fake.name(), unclean_types),
                'device_model': self.apply_unclean_options(random.choice(['iPhone 12', 'MacBook Pro', 'iPad Pro']), unclean_types),
                'subscription_type': self.apply_unclean_options(random.choice(['Free', 'Premium']), unclean_types),
                'purchase_date': self.apply_unclean_options(self.fake.date_this_year(), unclean_types),
                # Add other Apple-specific fields here
            })
        return data
