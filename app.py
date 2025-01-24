from flask import Flask, render_template, request, jsonify
from faker import Faker
import random

app = Flask(__name__)
fake = Faker()

def apply_unclean_options(value, unclean_types):
    # Apply unclean types logic
    if 'null' in unclean_types and random.random() < 0.1:  # 10% chance for null
        return None
    if 'zero' in unclean_types and random.random() < 0.1:  # 10% chance for zero
        return 0
    if 'negative' in unclean_types and random.random() < 0.1:  # 10% chance for negative
        return -1
    if 'empty' in unclean_types and random.random() < 0.1:  # 10% chance for empty string
        return ''
    return value

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_data():
    data = request.json
    domain = data.get('domain')
    count = int(data.get('count'))
    unclean_types = data.get('uncleanTypes', [])
    generated_data = []

    if domain == 'netflix':
        for _ in range(count):
                generated_data.append({
                    'name': apply_unclean_options(fake.name(), unclean_types),
                    'username': apply_unclean_options(fake.user_name(), unclean_types),
                    'email': apply_unclean_options(fake.email(), unclean_types),
                    'subscription_date': apply_unclean_options(fake.date_this_decade(), unclean_types),
                    'payment_method': apply_unclean_options(random.choice(['Credit Card', 'PayPal', 'Debit Card', 'Gift Card']), unclean_types),
                    'subscription_plan': apply_unclean_options(random.choice(['Basic', 'Standard', 'Premium']), unclean_types),
                    'watch_hours': apply_unclean_options(random.randint(20, 150), unclean_types),  # Random watch hours
                    'total_time_watched_today': apply_unclean_options(f"{random.randint(1, 5)} hours", unclean_types),  # Random time today
                    'last_time_watched': apply_unclean_options(fake.date_this_year(), unclean_types),
                    'country': apply_unclean_options(random.choice(['USA', 'India', 'UK', 'Canada', 'Australia']), unclean_types),
                    'language_preference': apply_unclean_options(random.choice(['English', 'Spanish', 'French', 'German']), unclean_types),
                    'monthly_spend': apply_unclean_options(random.choice([9.99, 15.99, 19.99]), unclean_types),
                    'next_billing_date': apply_unclean_options(fake.date_this_month(), unclean_types),
                    'profile_count': apply_unclean_options(random.randint(1, 5), unclean_types),  # Random profile count
                    'watchlist_count': apply_unclean_options(random.randint(1, 20), unclean_types),  # Random watchlist size
                    'last_payment_date': apply_unclean_options(fake.date_this_month(), unclean_types),
                    'device_type': apply_unclean_options(random.choice(['Smartphone', 'Tablet', 'Smart TV', 'Laptop', 'Console']), unclean_types),
                    'ratings_given': apply_unclean_options(f"{random.uniform(1, 5):.1f}/5", unclean_types),
                    'account_status': apply_unclean_options(random.choice(['Active', 'Suspended', 'Canceled']), unclean_types),
                    'preferred_genre': apply_unclean_options(random.choice(['Drama', 'Comedy', 'Action', 'Romance', 'Documentary', 'Sci-Fi', 'Thriller']), unclean_types),
                    'last_watched_title': apply_unclean_options(fake.word().title(), unclean_types),  # Random title for last watched
                    'device_login_history': apply_unclean_options([fake.word().title() for _ in range(random.randint(1, 3))], unclean_types),  # Random devices
                    'watch_history': apply_unclean_options([fake.word().title() for _ in range(random.randint(3, 10))], unclean_types),  # Random watch history
                    'auto_renewal_status': apply_unclean_options(random.choice(['Enabled', 'Disabled']), unclean_types),
                    'content_recommendations': apply_unclean_options([fake.word().title() for _ in range(random.randint(3, 5))], unclean_types),
                    'parental_controls': apply_unclean_options(random.choice(['Enabled (Age 13+)', 'Disabled']), unclean_types),
                    'referral_code_used': apply_unclean_options(fake.bothify(text='????##'), unclean_types),  # Random referral code
                })
    elif domain == 'spotify':
        for _ in range(count):
            generated_data.append({
                'user_name': apply_unclean_options(fake.name(), unclean_types),
                'email': apply_unclean_options(fake.email(), unclean_types),
                'subscription_type': apply_unclean_options(fake.random_element(['Free', 'Premium']), unclean_types),
                'playlist_names': apply_unclean_options(fake.word(), unclean_types),
                'subscription_start_date': apply_unclean_options(fake.date_this_decade(), unclean_types),
                'last_login': apply_unclean_options(fake.date_this_year(), unclean_types),
                'total_playtime': apply_unclean_options(fake.random_int(min=100, max=10000), unclean_types),  # Total playtime in minutes
                'favorite_artist': apply_unclean_options(fake.name(), unclean_types),
                'favorite_genre': apply_unclean_options(fake.word(), unclean_types),
                'device_type': apply_unclean_options(fake.random_element(['Mobile', 'Desktop', 'Tablet']), unclean_types),
                'country': apply_unclean_options(fake.country(), unclean_types),
                'language': apply_unclean_options(fake.language_name(), unclean_types),
                'account_status': apply_unclean_options(fake.random_element(['Active', 'Suspended', 'Expired']), unclean_types),
                'next_billing_date': apply_unclean_options(fake.date_this_year(), unclean_types),
                'auto_renewal_status': apply_unclean_options(fake.random_element(['Enabled', 'Disabled']), unclean_types),
                'last_payment_date': apply_unclean_options(fake.date_this_year(), unclean_types),
                'user_id': apply_unclean_options(fake.uuid4(), unclean_types),
                'device_id': apply_unclean_options(fake.uuid4(), unclean_types),
                'total_songs_listened': apply_unclean_options(fake.random_int(min=1000, max=50000), unclean_types),
                'avg_songs_per_day': apply_unclean_options(fake.random_int(min=10, max=200), unclean_types),
                'premium_user_since': apply_unclean_options(fake.date_this_decade(), unclean_types),
                'email_verified': apply_unclean_options(fake.boolean(), unclean_types),
                'followers_count': apply_unclean_options(fake.random_int(min=100, max=10000), unclean_types)
            })

    elif domain == 'amazon':
        for _ in range(count):
            generated_data.append({
                'user_name': apply_unclean_options(fake.name(), unclean_types),
                'order_id': apply_unclean_options(fake.uuid4(), unclean_types),
                'email': apply_unclean_options(fake.email(), unclean_types),
                'order_date': apply_unclean_options(fake.date_this_year(), unclean_types),
                'product_name': apply_unclean_options(fake.word(), unclean_types),
                'shipping_address': apply_unclean_options(fake.address(), unclean_types),
                'payment_method': apply_unclean_options(fake.random_element(['Credit Card', 'Debit Card', 'PayPal', 'Amazon Pay']), unclean_types),
                'total_amount': apply_unclean_options(fake.random_number(digits=3), unclean_types),  # Total order amount in dollars
                'delivery_status': apply_unclean_options(fake.random_element(['Pending', 'Shipped', 'Delivered', 'Returned']), unclean_types),
                'delivery_date': apply_unclean_options(fake.date_this_year(), unclean_types),
                'order_status': apply_unclean_options(fake.random_element(['Completed', 'Cancelled', 'In Progress']), unclean_types),
                'product_category': apply_unclean_options(fake.word(), unclean_types),
                'product_rating': apply_unclean_options(fake.random_int(min=1, max=5), unclean_types),  # Rating out of 5
                'return_window': apply_unclean_options(fake.random_int(min=1, max=30), unclean_types),  # Return window in days
                'customer_support_contact': apply_unclean_options(fake.phone_number(), unclean_types),
                'coupon_used': apply_unclean_options(fake.boolean(), unclean_types),  # Whether a coupon was used for the order
                'gift_wrap': apply_unclean_options(fake.boolean(), unclean_types),  # Whether the order was gift wrapped
                'order_type': apply_unclean_options(fake.random_element(['One-time', 'Subscription']), unclean_types),
                'delivery_method': apply_unclean_options(fake.random_element(['Standard', 'Express', 'Same-day']), unclean_types),
                'payment_status': apply_unclean_options(fake.random_element(['Paid', 'Pending', 'Failed']), unclean_types),
                'is_prime_member': apply_unclean_options(fake.random_element(['Yes', 'No']), unclean_types),
                'item_quantity': apply_unclean_options(fake.random_int(min=1, max=10), unclean_types),
                'review_submission_date': apply_unclean_options(fake.date_this_year(), unclean_types)
            })

    elif domain == 'apple':
        for _ in range(count):
            generated_data.append({
                'user_name': apply_unclean_options(fake.name(), unclean_types),
                'device_model': apply_unclean_options(fake.random_element(['Iphone 12', 'Iphone 12 Pro', 'Macbook Pro','Ipad pro', 'Watch Ultra 2', 'Iphone 16 Pro Max', 'Iphone 16', 'Ipad Air']), unclean_types),
                'subscription_type': apply_unclean_options(fake.random_element(['Free', 'Premium']), unclean_types),
                'purchase_date': apply_unclean_options(fake.date_this_year(), unclean_types),
                'account_status': apply_unclean_options(fake.random_element(['Active', 'Suspended', 'Expired']), unclean_types),
                'last_login': apply_unclean_options(fake.date_this_year(), unclean_types),
                'total_spend': apply_unclean_options(fake.random_number(digits=3), unclean_types),  # Total spend in dollars
                'device_os': apply_unclean_options(fake.random_element(['iOS', 'macOS', 'tvOS', 'watchOS']), unclean_types),
                'next_billing_date': apply_unclean_options(fake.date_this_year(), unclean_types),
                'auto_renewal_status': apply_unclean_options(fake.random_element(['Enabled', 'Disabled']), unclean_types),
                'payment_method': apply_unclean_options(fake.random_element(['Apple Pay', 'Credit Card', 'Debit Card']), unclean_types),
                'purchase_history': apply_unclean_options(fake.word(), unclean_types),
                'location': apply_unclean_options(fake.city(), unclean_types),
                'subscription_start_date': apply_unclean_options(fake.date_this_year(), unclean_types),
                'family_sharing': apply_unclean_options(fake.boolean(), unclean_types),  # Whether the user shares subscription with family
                'device_type': apply_unclean_options(fake.random_element(['iPhone', 'iPad', 'MacBook', 'Apple Watch']), unclean_types),
                'feedback': apply_unclean_options(fake.sentence(), unclean_types),  # User feedback for the service or device
                'warranty_status': apply_unclean_options(fake.random_element(['Active', 'Expired']), unclean_types),
                'total_apps_downloaded': apply_unclean_options(fake.random_int(min=1, max=500), unclean_types),
                'account_creation_date': apply_unclean_options(fake.date_this_decade(), unclean_types),
                'gift_cards_used': apply_unclean_options(fake.boolean(), unclean_types),
                'device_serial_number': apply_unclean_options(fake.uuid4(), unclean_types)
            })


    return jsonify(generated_data)

if __name__ == '__main__':
    app.run(debug=True)
