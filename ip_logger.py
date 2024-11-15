import random
import string

def generate_link():
    # Generate a random string of letters and digits for the short URL
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f'https://example.com/{random_string}'

# Example usage
if __name__ == "__main__":
    print(generate_link())
