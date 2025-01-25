from .base_generator import BaseGenerator
import random

class SpotifyGenerator(BaseGenerator):
    def generate(self, count, unclean_types):
        data = []
        for _ in range(count):
            data.append({
                'user_name': self.apply_unclean_options(self.fake.name(), unclean_types),
                'email': self.apply_unclean_options(self.fake.email(), unclean_types),
                'subscription_type': self.apply_unclean_options(random.choice(['Free', 'Premium']), unclean_types),
                'playlist_names': self.apply_unclean_options(self.fake.word(), unclean_types),
                # Add other Spotify-specific fields here
            })
        return data
