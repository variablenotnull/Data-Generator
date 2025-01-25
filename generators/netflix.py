from .base_generator import BaseGenerator
import random

class NetflixGenerator(BaseGenerator):
    def generate(self, count, unclean_types):
        data = []
        for _ in range(count):
            data.append({
                'name': self.apply_unclean_options(self.fake.name(), unclean_types),
                'username': self.apply_unclean_options(self.fake.user_name(), unclean_types),
                'email': self.apply_unclean_options(self.fake.email(), unclean_types),
                'subscription_date': self.apply_unclean_options(self.fake.date_this_decade(), unclean_types),
                'payment_method': self.apply_unclean_options(random.choice(['Credit Card', 'PayPal', 'Debit Card', 'Gift Card']), unclean_types),
                'subscription_plan': self.apply_unclean_options(random.choice(['Basic', 'Standard', 'Premium']), unclean_types),
                'watch_hours': self.apply_unclean_options(random.randint(20, 150), unclean_types),
                # Add other Netflix-specific fields here
            })
        return data
