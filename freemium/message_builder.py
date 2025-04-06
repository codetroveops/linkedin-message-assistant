import csv

def generate_message(name, role, company):
    message = (
        f"Hi {name}, I came across your profile and noticed your work at {company} as a {role}. "
        "I’d love to connect and learn more about your journey. Cheers!"
    )
    return message

def generate_from_csv(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                role = row['role']
                company = row['company']
                print(f"\n📩 Message for {name}:\n{generate_message(name, role, company)}\n")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🔗 LinkedIn Message Assistant (Freemium Version)\n")
    csv_path = "freemium/sample_input.csv"
    generate_from_csv(csv_path)