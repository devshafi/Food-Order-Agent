import random
from langchain.tools import tool


@tool
def search_menu(query: str) -> str:
    """Search for menu items and return 2 random top food recommendations."""
    menu_items = [
        "Margherita Pizza",
        "Caesar Salad",
        "Grilled Salmon",
        "Beef Burger",
        "Pasta Carbonara",
        "Chicken Tikka Masala",
        "Tacos Al Pastor",
        "Pad Thai",
        "Risotto Mushroom",
        "Lamb Chops",
    ]
    top_2 = random.sample(menu_items, 2)
    return f"Top 2 food recommendations for '{query}': {', '.join(top_2)}"


@tool
def get_weather(location: str) -> str:
    """Get weather information for a location."""
    return f"Weather in {location}: Sunny, 72°F"


@tool
def order_food(food: str, quantity: int) -> str:
    """Place an order for food items with specified quantity."""
    return f"Order confirmed: {quantity}x {food}. Your order is being prepared!"
