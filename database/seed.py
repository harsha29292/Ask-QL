import random
from faker import Faker
import psycopg2

fake = Faker()

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="askql_saas",
    user="postgres",
    password="harsha123"
)

cur = conn.cursor()

# -------------------------
# ORGANIZATIONS
# -------------------------

organization_ids = []

for _ in range(20):
    cur.execute(
        """
        INSERT INTO organizations(name, industry)
        VALUES (%s, %s)
        RETURNING id
        """,
        (
            fake.company(),
            random.choice([
                "Technology",
                "Finance",
                "Healthcare",
                "Retail"
            ])
        )
    )

    organization_ids.append(
        cur.fetchone()[0]
    )

print("Organizations seeded")

# -------------------------
# USERS
# -------------------------

user_ids = []

for _ in range(100):

    cur.execute(
        """
        INSERT INTO users(
            organization_id,
            name,
            email
        )
        VALUES (%s,%s,%s)
        RETURNING id
        """,
        (
            random.choice(
                organization_ids
            ),
            fake.name(),
            fake.unique.email()
        )
    )

    user_ids.append(
        cur.fetchone()[0]
    )

print("Users seeded")

# -------------------------
# CUSTOMERS
# -------------------------

customer_ids = []

for _ in range(200):

    cur.execute(
        """
        INSERT INTO customers(
            organization_id,
            name,
            email,
            status
        )
        VALUES (%s,%s,%s,%s)
        RETURNING id
        """,
        (
            random.choice(
                organization_ids
            ),
            fake.company(),
            fake.unique.email(),
            random.choice([
                "active",
                "inactive",
                "trial"
            ])
        )
    )

    customer_ids.append(
        cur.fetchone()[0]
    )

print("Customers seeded")

# -------------------------
# PLANS
# -------------------------

plan_ids = []

plans = [
    ("Starter", 29),
    ("Growth", 99),
    ("Business", 299),
    ("Enterprise", 999),
    ("Ultimate", 1999)
]

for name, price in plans:

    cur.execute(
        """
        INSERT INTO plans(
            name,
            monthly_price
        )
        VALUES (%s,%s)
        RETURNING id
        """,
        (name, price)
    )

    plan_ids.append(
        cur.fetchone()[0]
    )

print("Plans seeded")

# -------------------------
# SUBSCRIPTIONS
# -------------------------

for _ in range(300):

    cur.execute(
        """
        INSERT INTO subscriptions(
            customer_id,
            plan_id,
            status,
            start_date
        )
        VALUES (%s,%s,%s,%s)
        """,
        (
            random.choice(customer_ids),
            random.choice(plan_ids),
            random.choice([
                "active",
                "cancelled",
                "trial"
            ]),
            fake.date_between(
                start_date="-2y",
                end_date="today"
            )
        )
    )

print("Subscriptions seeded")

# -------------------------
# INVOICES
# -------------------------

invoice_ids = []

for _ in range(1000):

    cur.execute(
        """
        INSERT INTO invoices(
            customer_id,
            amount,
            status,
            issued_at
        )
        VALUES (%s,%s,%s,%s)
        RETURNING id
        """,
        (
            random.choice(customer_ids),
            round(
                random.uniform(
                    50,
                    5000
                ),
                2
            ),
            random.choice([
                "paid",
                "pending",
                "overdue"
            ]),
            fake.date_time_between(
                start_date="-2y",
                end_date="now"
            )
        )
    )

    invoice_ids.append(
        cur.fetchone()[0]
    )

print("Invoices seeded")

# -------------------------
# PAYMENTS
# -------------------------

for _ in range(800):

    cur.execute(
        """
        INSERT INTO payments(
            invoice_id,
            amount
        )
        VALUES (%s,%s)
        """,
        (
            random.choice(invoice_ids),
            round(
                random.uniform(
                    50,
                    5000
                ),
                2
            )
        )
    )
print("Payments seeded")
# -------------------------
# TEAMS
# -------------------------

team_ids = []

for _ in range(30):

    cur.execute(
        """
        INSERT INTO teams(
            organization_id,
            name
        )
        VALUES (%s,%s)
        RETURNING id
        """,
        (
            random.choice(
                organization_ids
            ),
            fake.word().title() + " Team"
        )
    )

    team_ids.append(
        cur.fetchone()[0]
    )

print("Teams seeded")
# TEAM MEMBERS

for user_id in user_ids:

    cur.execute(
        """
        INSERT INTO team_members(
            team_id,
            user_id
        )
        VALUES (%s, %s)
        """,
        (
            random.choice(team_ids),
            user_id
        )
    )   
print("Team members seeded")


conn.commit()

cur.close()
conn.close()

print("\nSeeding Complete")