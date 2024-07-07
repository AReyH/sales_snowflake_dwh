import pandas as pd
import random
import datetime

first_names = [
    "James", "John", "Robert", "Michael", "William", 
    "David", "Richard", "Joseph", "Charles", "Thomas", 
    "Christopher", "Daniel", "Matthew", "Anthony", "Donald", 
    "Mark", "Paul", "Steven", "Andrew", "Kenneth", 
    "Joshua", "George", "Kevin", "Brian", "Edward", 
    "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan", 
    "Jacob", "Gary", "Nicholas", "Eric", "Stephen", 
    "Jonathan", "Larry", "Justin", "Scott", "Brandon", 
    "Benjamin", "Samuel", "Frank", "Gregory", "Raymond", 
    "Alexander", "Patrick", "Jack", "Dennis", "Jerry", 
    "Tyler", "Aaron", "Jose", "Henry", "Douglas", 
    "Peter", "Adam", "Nathan", "Zachary", "Walter", 
    "Harold", "Kyle", "Carl", "Arthur", "Gerald", 
    "Roger", "Keith", "Jeremy", "Terry", "Lawrence", 
    "Sean", "Christian", "Albert", "Joe", "Ethan", 
    "Austin", "Jesse", "Willie", "Billy", "Bryan", 
    "Bruce", "Jordan", "Ralph", "Roy", "Noah", 
    "Dylan", "Eugene", "Wayne", "Alan", "Juan", 
    "Louis", "Russell", "Gabriel", "Randy", "Philip", 
    "Harry", "Vincent", "Bobby", "Johnny", "Logan",
    "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", 
    "Barbara", "Susan", "Jessica", "Sarah", "Karen", 
    "Nancy", "Lisa", "Margaret", "Betty", "Dorothy", 
    "Sandra", "Ashley", "Kimberly", "Donna", "Emily", 
    "Michelle", "Carol", "Amanda", "Melissa", "Deborah", 
    "Stephanie", "Rebecca", "Laura", "Sharon", "Cynthia", 
    "Kathleen", "Amy", "Shirley", "Angela", "Helen", 
    "Anna", "Brenda", "Pamela", "Nicole", "Emma", 
    "Samantha", "Katherine", "Christine", "Debra", "Rachel", 
    "Carolyn", "Janet", "Ruth", "Maria", "Heather", 
    "Diane", "Virginia", "Julie", "Joyce", "Victoria", 
    "Joan", "Kelly", "Christina", "Lauren", "Frances", 
    "Martha", "Judith", "Cheryl", "Megan", "Andrea"
]


last_names = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", 
    "Davis", "Miller", "Wilson", "Moore", "Taylor", 
    "Anderson", "Thomas", "Jackson", "White", "Harris", 
    "Martin", "Thompson", "Garcia", "Martinez", "Robinson", 
    "Clark", "Rodriguez", "Lewis", "Lee", "Walker", 
    "Hall", "Allen", "Young", "Hernandez", "King", 
    "Wright", "Lopez", "Hill", "Scott", "Green", 
    "Adams", "Baker", "Gonzalez", "Nelson", "Carter", 
    "Mitchell", "Perez", "Roberts", "Turner", "Phillips", 
    "Campbell", "Parker", "Evans", "Edwards", "Collins", 
    "Stewart", "Sanchez", "Morris", "Rogers", "Reed", 
    "Cook", "Morgan", "Bell", "Murphy", "Bailey", 
    "Rivera", "Cooper", "Richardson", "Cox", "Howard", 
    "Ward", "Torres", "Peterson", "Gray", "Ramirez", 
    "James", "Watson", "Brooks", "Kelly", "Sanders", 
    "Price", "Bennett", "Wood", "Barnes", "Ross", 
    "Henderson", "Coleman", "Jenkins", "Perry", "Powell", 
    "Long", "Patterson", "Hughes", "Flores", "Washington", 
    "Butler", "Simmons", "Foster", "Gonzales", "Bryant"
]

def random_date(start_date, end_date):
    return start_date + datetime.timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

data = {
    'sale_id': [],
    'sale_date': [],
    'customer_id': [],
    'product_id': [],
    'store_id': [],
    'quantity': [],
    'total_amount': [],

    'customer_first_name': [],
    'customer_last_name': [],
    'customer_email': [],
    'customer_phone_number': [],
    'customer_date_of_birth': [],
    'customer_gender': [],
    'customer_registration_date': [],
    'customer_street_address': [],
    'customer_city': [],
    'customer_state': [],
    'customer_postal_code': [],
    'customer_country': [],

    'product_name': [],
    'product_category': [],
    'product_brand': [],
    'product_price': [],
    'product_description': [],
    'product_stock_quantity': [],
    'product_date_added': [],

    'store_name': [],
    'store_location': [],
    'store_manager': [],
    'store_opening_date': [],

    'return_id': [],
    'return_date': [],
    'return_quantity': [],
    'return_total_amount': [],

    'date_id': [],
    'date': [],
    'day': [],
    'week': [],
    'month': [],
    'quarter': [],
    'year': [],
}

for sale_id in range(1, 10001):
    sale_date = datetime.date.today() - datetime.timedelta(days=random.randint(0, 730))
    customer_date_of_birth = sale_date - datetime.timedelta(days=random.randint(365*18, 365*70))
    product_date_added = sale_date - datetime.timedelta(days=random.randint(0, 365))
    store_opening_date = sale_date - datetime.timedelta(days=random.randint(365, 3650))

    data['sale_id'].append(sale_id)
    data['sale_date'].append(sale_date)
    data['customer_id'].append(random.randint(1, 100))
    data['product_id'].append(random.randint(1, 50))
    data['store_id'].append(random.randint(1, 10))
    data['quantity'].append(random.randint(1, 10))
    data['total_amount'].append(round(random.uniform(20, 200), 2))

    data['customer_first_name'].append(random.choice(first_names))
    data['customer_last_name'].append(random.choice(last_names))
    data['customer_email'].append(f"customer{random.randint(1, 100000)}@example.com")
    data['customer_phone_number'].append(f"+1-555-{random.randint(100, 999)}-{random.randint(1000, 9999)}")
    data['customer_date_of_birth'].append(customer_date_of_birth)
    data['customer_gender'].append(random.choice(['Male', 'Female', 'Other']))
    data['customer_registration_date'].append(sale_date - datetime.timedelta(days=random.randint(1, 365)))
    data['customer_street_address'].append(f"{random.randint(100, 999)} {random.choice(['Oak', 'Maple', 'Elm'])} St")
    data['customer_city'].append("City" + str(random.randint(1, 10)))
    data['customer_state'].append("State" + str(random.randint(1, 5)))
    data['customer_postal_code'].append(f"ABC{random.randint(100, 999)}")
    data['customer_country'].append("Country" + str(random.randint(1, 3)))

    data['product_name'].append(f"Product{random.randint(1, 50)}")
    data['product_category'].append(random.choice(['Electronics', 'Clothing', 'Books', 'Toys', 'Sports']))
    data['product_brand'].append(f"Brand{random.randint(1, 10)}")
    data['product_price'].append(round(random.uniform(10, 500), 2))
    data['product_description'].append(f"Description for Product{random.randint(1, 50)}")
    data['product_stock_quantity'].append(random.randint(0, 100))
    data['product_date_added'].append(product_date_added)

    data['store_name'].append(f"Store{random.randint(1, 10)}")
    data['store_location'].append(f"{random.randint(100, 999)} {random.choice(['Main', 'High', 'Park'])} St")
    data['store_manager'].append(f"Manager{random.randint(1, 10)}")
    data['store_opening_date'].append(store_opening_date)

    if random.random() < 0.2:  # 20% chance of return
        return_id = sale_id
        return_date = sale_date + datetime.timedelta(days=random.randint(1, 30))
        return_quantity = random.randint(1, 5)
        return_total_amount = round(random.uniform(10, 100), 2)

        data['return_id'].append(return_id)
        data['return_date'].append(return_date)
        data['return_quantity'].append(return_quantity)
        data['return_total_amount'].append(return_total_amount)
    else:
        data['return_id'].append(None)
        data['return_date'].append(None)
        data['return_quantity'].append(None)
        data['return_total_amount'].append(None)

    data['date_id'].append(sale_date.strftime('%Y%m%d'))
    data['date'].append(sale_date)
    data['day'].append(sale_date.day)
    data['week'].append(sale_date.isocalendar()[1])
    data['month'].append(sale_date.month)
    data['quarter'].append((sale_date.month - 1) // 3 + 1)
    data['year'].append(sale_date.year)


df = pd.DataFrame(data)

df.to_csv('..data/sales.csv')