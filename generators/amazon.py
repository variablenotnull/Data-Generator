from .base_generator import BaseGenerator

class AmazonGenerator(BaseGenerator):
    def generate(self, count, unclean_types):
        data = []
        for _ in range(count):
            data.append({
                'user_name': self.apply_unclean_options(self.fake.name(), unclean_types),
                'order_id': self.apply_unclean_options(self.fake.uuid4(), unclean_types),
                'email': self.apply_unclean_options(self.fake.email(), unclean_types),
                'order_date': self.apply_unclean_options(self.fake.date_this_year(), unclean_types),
                'product_name': self.apply_unclean_options(self.fake.word(), unclean_types),
                # Add other Amazon-specific fields here
            })
        return data
