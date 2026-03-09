# import pandas as pd
# import numpy as np

# def generate_dataset(n=50000):
#     np.random.seed(42)

#     df = pd.DataFrame({
#         "lead_id": range(1, n+1),
#         "company_size": np.random.randint(5, 500, n),
#         "annual_revenue": np.random.randint(50000, 5000000, n),
#         "industry_score": np.random.randint(1, 10, n),
#         "previous_interactions": np.random.randint(0, 10, n),
#         "credit_score": np.random.randint(600, 850, n)
#     })

#     df["conversion_probability"] = (
#         0.3 * (df["credit_score"] / 850) +
#         0.3 * (df["industry_score"] / 10) +
#         0.4 * (df["previous_interactions"] / 10)
#     )

#     df["converted"] = np.where(df["conversion_probability"] > 0.6, 1, 0)

#     df.to_csv("data/prospects.csv", index=False)
#     print("Dataset generated!")

# if __name__ == "__main__":
#     generate_dataset()

import pandas as pd
import numpy as np
from faker import Faker
from src.config import DATA_PATH

fake = Faker()

def generate_data(n=1000):

    data = []

    for _ in range(n):
        visits = np.random.randint(1, 50)
        pages = np.random.randint(1, 20)
        time_spent = np.random.randint(10, 500)
        email_open = np.random.randint(0, 10)
        demo_requested = np.random.choice([0,1], p=[0.8,0.2])

        conversion = 1 if (visits + pages + time_spent + demo_requested*50) > 200 else 0

        data.append({
            "name": fake.name(),
            "company": fake.company(),
            "website_visits": visits,
            "pages_viewed": pages,
            "time_spent": time_spent,
            "email_opens": email_open,
            "demo_requested": demo_requested,
            "converted": conversion
        })

    df = pd.DataFrame(data)

    df.to_csv(DATA_PATH, index=False)

    print("Dataset created:", DATA_PATH)

if __name__ == "__main__":
    generate_data()