TABLES = [
    {"id": 1, "seats": 2, "location": "Window"},
    {"id": 2, "seats": 2, "location": "Patio"},
    {"id": 3, "seats": 4, "location": "Main Hall"},
    {"id": 4, "seats": 4, "location": "Main Hall"},
    {"id": 5, "seats": 4, "location": "Patio"},
    {"id": 6, "seats": 6, "location": "Private Room"},
    {"id": 7, "seats": 6, "location": "Main Hall"},
    {"id": 8, "seats": 8, "location": "Private Room"},
    {"id": 9, "seats": 2, "location": "Bar"},
    {"id": 10, "seats": 10, "location": "Banquet Hall"},
]

MENU_ITEMS = [
    # Pizza
    "Margherita Pizza",
    "Pepperoni Pizza",
    "BBQ Chicken Pizza",
    # Salads
    "Caesar Salad",
    "Greek Salad",
    "Nicoise Salad",
    # Seafood
    "Grilled Salmon",
    "Shrimp Scampi",
    "Fish & Chips",
    # Burgers
    "Beef Burger",
    "Mushroom Swiss Burger",
    "Spicy Jalapeño Burger",
    # Pasta
    "Pasta Carbonara",
    "Spaghetti Bolognese",
    "Penne Arrabbiata",
    # Indian
    "Chicken Tikka Masala",
    "Lamb Rogan Josh",
    "Vegetable Biryani",
    # Mexican
    "Tacos Al Pastor",
    "Beef Enchiladas",
    "Chicken Quesadilla",
    # Asian
    "Pad Thai",
    "Kung Pao Chicken",
    "Beef Fried Rice",
    # Risotto
    "Risotto Mushroom",
    "Seafood Risotto",
    "Truffle Risotto",
    # Lamb & Steak
    "Lamb Chops",
    "Ribeye Steak",
    "Rack of Lamb",
]

BEST_ITEMS = ["Chicken Tikka Masala", "Grilled Salmon"]

NUTRITION = {
    # Pizza
    "Margherita Pizza": {
        "calories": 800,
        "protein_g": 32,
        "carbs_g": 90,
        "fat_g": 30,
        "allergens": ["gluten", "dairy"],
    },
    "Pepperoni Pizza": {
        "calories": 950,
        "protein_g": 38,
        "carbs_g": 92,
        "fat_g": 40,
        "allergens": ["gluten", "dairy"],
    },
    "BBQ Chicken Pizza": {
        "calories": 920,
        "protein_g": 42,
        "carbs_g": 95,
        "fat_g": 35,
        "allergens": ["gluten", "dairy"],
    },
    # Salads
    "Caesar Salad": {
        "calories": 350,
        "protein_g": 14,
        "carbs_g": 18,
        "fat_g": 24,
        "allergens": ["dairy", "gluten"],
    },
    "Greek Salad": {
        "calories": 280,
        "protein_g": 8,
        "carbs_g": 15,
        "fat_g": 20,
        "allergens": ["dairy"],
    },
    "Nicoise Salad": {
        "calories": 320,
        "protein_g": 22,
        "carbs_g": 12,
        "fat_g": 18,
        "allergens": ["fish", "eggs"],
    },
    # Seafood
    "Grilled Salmon": {
        "calories": 520,
        "protein_g": 52,
        "carbs_g": 4,
        "fat_g": 30,
        "allergens": ["fish"],
    },
    "Shrimp Scampi": {
        "calories": 480,
        "protein_g": 36,
        "carbs_g": 28,
        "fat_g": 22,
        "allergens": ["shellfish", "gluten"],
    },
    "Fish & Chips": {
        "calories": 860,
        "protein_g": 38,
        "carbs_g": 90,
        "fat_g": 38,
        "allergens": ["fish", "gluten"],
    },
    # Burgers
    "Beef Burger": {
        "calories": 750,
        "protein_g": 40,
        "carbs_g": 50,
        "fat_g": 38,
        "allergens": ["gluten", "dairy"],
    },
    "Mushroom Swiss Burger": {
        "calories": 780,
        "protein_g": 42,
        "carbs_g": 52,
        "fat_g": 40,
        "allergens": ["gluten", "dairy"],
    },
    "Spicy Jalapeño Burger": {
        "calories": 800,
        "protein_g": 41,
        "carbs_g": 52,
        "fat_g": 42,
        "allergens": ["gluten", "dairy"],
    },
    # Pasta
    "Pasta Carbonara": {
        "calories": 720,
        "protein_g": 30,
        "carbs_g": 80,
        "fat_g": 28,
        "allergens": ["gluten", "dairy", "eggs"],
    },
    "Spaghetti Bolognese": {
        "calories": 680,
        "protein_g": 34,
        "carbs_g": 76,
        "fat_g": 22,
        "allergens": ["gluten"],
    },
    "Penne Arrabbiata": {
        "calories": 580,
        "protein_g": 18,
        "carbs_g": 88,
        "fat_g": 14,
        "allergens": ["gluten"],
    },
    # Indian
    "Chicken Tikka Masala": {
        "calories": 620,
        "protein_g": 46,
        "carbs_g": 28,
        "fat_g": 32,
        "allergens": ["dairy"],
    },
    "Lamb Rogan Josh": {
        "calories": 680,
        "protein_g": 48,
        "carbs_g": 18,
        "fat_g": 38,
        "allergens": ["dairy"],
    },
    "Vegetable Biryani": {
        "calories": 480,
        "protein_g": 12,
        "carbs_g": 80,
        "fat_g": 12,
        "allergens": ["gluten"],
    },
    # Mexican
    "Tacos Al Pastor": {
        "calories": 540,
        "protein_g": 30,
        "carbs_g": 52,
        "fat_g": 20,
        "allergens": ["gluten"],
    },
    "Beef Enchiladas": {
        "calories": 680,
        "protein_g": 36,
        "carbs_g": 58,
        "fat_g": 30,
        "allergens": ["gluten", "dairy"],
    },
    "Chicken Quesadilla": {
        "calories": 620,
        "protein_g": 38,
        "carbs_g": 48,
        "fat_g": 26,
        "allergens": ["gluten", "dairy"],
    },
    # Asian
    "Pad Thai": {
        "calories": 580,
        "protein_g": 24,
        "carbs_g": 72,
        "fat_g": 20,
        "allergens": ["peanuts", "shellfish", "gluten"],
    },
    "Kung Pao Chicken": {
        "calories": 560,
        "protein_g": 38,
        "carbs_g": 32,
        "fat_g": 28,
        "allergens": ["peanuts", "gluten"],
    },
    "Beef Fried Rice": {
        "calories": 620,
        "protein_g": 28,
        "carbs_g": 78,
        "fat_g": 20,
        "allergens": ["gluten", "eggs"],
    },
    # Risotto
    "Risotto Mushroom": {
        "calories": 520,
        "protein_g": 14,
        "carbs_g": 72,
        "fat_g": 18,
        "allergens": ["dairy"],
    },
    "Seafood Risotto": {
        "calories": 580,
        "protein_g": 30,
        "carbs_g": 68,
        "fat_g": 20,
        "allergens": ["shellfish", "dairy"],
    },
    "Truffle Risotto": {
        "calories": 640,
        "protein_g": 16,
        "carbs_g": 74,
        "fat_g": 26,
        "allergens": ["dairy"],
    },
    # Lamb & Steak
    "Lamb Chops": {
        "calories": 720,
        "protein_g": 56,
        "carbs_g": 4,
        "fat_g": 48,
        "allergens": [],
    },
    "Ribeye Steak": {
        "calories": 860,
        "protein_g": 64,
        "carbs_g": 2,
        "fat_g": 58,
        "allergens": [],
    },
    "Rack of Lamb": {
        "calories": 780,
        "protein_g": 60,
        "carbs_g": 4,
        "fat_g": 52,
        "allergens": [],
    },
}

MENU_WITH_PRICES = {
    # Pizza
    "Margherita Pizza": 12.99,
    "Pepperoni Pizza": 14.99,
    "BBQ Chicken Pizza": 15.99,
    # Salads
    "Caesar Salad": 9.99,
    "Greek Salad": 10.99,
    "Nicoise Salad": 11.99,
    # Seafood
    "Grilled Salmon": 22.99,
    "Shrimp Scampi": 19.99,
    "Fish & Chips": 14.99,
    # Burgers
    "Beef Burger": 13.99,
    "Mushroom Swiss Burger": 14.99,
    "Spicy Jalapeño Burger": 14.99,
    # Pasta
    "Pasta Carbonara": 15.99,
    "Spaghetti Bolognese": 14.99,
    "Penne Arrabbiata": 13.99,
    # Indian
    "Chicken Tikka Masala": 17.99,
    "Lamb Rogan Josh": 19.99,
    "Vegetable Biryani": 14.99,
    # Mexican
    "Tacos Al Pastor": 12.99,
    "Beef Enchiladas": 13.99,
    "Chicken Quesadilla": 11.99,
    # Asian
    "Pad Thai": 13.99,
    "Kung Pao Chicken": 14.99,
    "Beef Fried Rice": 12.99,
    # Risotto
    "Risotto Mushroom": 16.99,
    "Seafood Risotto": 21.99,
    "Truffle Risotto": 23.99,
    # Lamb & Steak
    "Lamb Chops": 27.99,
    "Ribeye Steak": 32.99,
    "Rack of Lamb": 34.99,
}
