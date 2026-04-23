from langchain.tools import tool

import random

from tools.db import BEST_ITEMS, MENU_ITEMS, MENU_WITH_PRICES, NUTRITION, TABLES

@tool
def search_menu(query: str) -> str:
    """Search the menu for items matching the query and return any matches found."""
    query_lower = query.lower()
    matches = [item for item in MENU_ITEMS if query_lower in item.lower()]
    if matches:
        return f"Found menu items matching '{query}': {', '.join(matches)}"
    return f"No menu items found matching '{query}'."


@tool
def get_best_items() -> str:
    """Return the 2 best-selling menu items."""
    return f"Our 2 best items are: {', '.join(BEST_ITEMS)}"


@tool
def get_menu_with_prices(category: str = "") -> str:
    """Return menu items with prices, optionally filtered by category (e.g. 'pizza', 'salads', 'burgers')."""
    if category:
        filtered = {k: v for k, v in MENU_WITH_PRICES.items() if category.lower() in k.lower()}
    else:
        filtered = MENU_WITH_PRICES
    if not filtered:
        return f"No items found for category '{category}'."
    lines = [f"{item}: ${price:.2f}" for item, price in filtered.items()]
    return "\n".join(lines)


@tool
def get_nutritional_info(item: str) -> str:
    """Get nutritional information (calories, protein, carbs, fat, allergens) for a specific menu item."""
    match = next((k for k in NUTRITION if item.lower() in k.lower()), None)
    if not match:
        return f"No nutritional info found for '{item}'."
    n = NUTRITION[match]
    allergens = ", ".join(n["allergens"]) if n["allergens"] else "none"
    return (
        f"{match} — Calories: {n['calories']} kcal | "
        f"Protein: {n['protein_g']}g | Carbs: {n['carbs_g']}g | "
        f"Fat: {n['fat_g']}g | Allergens: {allergens}"
    )


@tool
def check_table_availability(party_size: int = 0) -> str:
    """Check available tables. Pass party_size to find tables that fit your group, or omit for a general overview."""
    available = random.sample(TABLES, random.randint(2, 3))
    if party_size:
        matches = [t for t in available if t["seats"] >= party_size]
        if not matches:
            return f"No available tables for a party of {party_size}. Try a smaller group or check back later."
        lines = [f"Table {t['id']} — {t['seats']} seats, {t['location']}" for t in matches]
        return f"Available tables for {party_size} guests:\n" + "\n".join(lines)
    lines = [f"Table {t['id']} — {t['seats']} seats, {t['location']}" for t in available]
    return "Available tables:\n" + "\n".join(lines)


@tool
def order_food(food: str, quantity: int) -> str:
    """Place an order for food items with specified quantity."""
    return f"Order confirmed: {quantity}x {food}. Your order is being prepared!"
