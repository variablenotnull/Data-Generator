from flask import Flask, render_template, request, jsonify
from faker import Faker
from multiprocessing import Pool, cpu_count
from generators.netflix import NetflixGenerator
from generators.spotify import SpotifyGenerator
from generators.amazon import AmazonGenerator
from generators.apple import AppleGenerator
app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_data():
    data = request.get_json()
    domain = data.get('domain')
    count = int(data.get('count', 0))
    unclean_types = data.get('uncleanTypes', [])

    generators = {
        'netflix': NetflixGenerator(),
        'spotify': SpotifyGenerator(),
        'amazon': AmazonGenerator(),
        'apple': AppleGenerator(),
    }

    if domain not in generators:
        return jsonify({'error': 'Unsupported domain'}), 400

    generator = generators[domain]
    generated_data = generator.generate(count, unclean_types)

    return jsonify(generated_data)

if __name__ == '__main__':
    app.run(debug=False)
