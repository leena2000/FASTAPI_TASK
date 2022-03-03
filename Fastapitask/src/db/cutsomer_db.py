from src.models.customer import Gender

fake_customer_db = [
   {"id": 0, "first_name": "Mohammad", "last_name": "Ahamd", "age": 25, "gender": Gender.male, "adult": True, "address_id": 2,},
   {"id": 1, "first_name": "Ali", "last_name": "Mousa", "age": 17, "gender": Gender.male, "adult": False, "address_id": 0,},
   {"id": 2, "first_name": "Fadwa", "last_name": "Kareem", "age": 22, "gender": Gender.female, "adult": True, "address_id": 3,},
   {"id": 3, "first_name": "Salwa", "last_name": "Belal", "age": 32, "gender": Gender.female, "adult": True, "address_id": 1,},
]
