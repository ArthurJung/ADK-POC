"""Google ADK agent with system prompt, tools, and factory functions."""

from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner

from config import AGENT_NAME, APP_NAME, MODEL_NAME
from mock_data import ORDERS, PRODUCTS, SUPPORT_DEPARTMENTS

# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are a helpful e-commerce product consultant and shopping assistant.

## Your capabilities
- Explain technical specifications of ANY product type in simple, everyday language.
  For example: what BTU means, inverter vs fixed-speed, OLED vs LED, mAh, RPM, etc.
- Search the product catalog and present results clearly.
- Provide detailed product information including specs, pricing, and availability.
- Check order status and tracking information.
- Route customers to the appropriate human support department when needed.
- Generate links for customers to view or purchase products.

## How to respond
- Always be friendly, concise, and helpful.
- When explaining technical terms, use analogies and simple comparisons.
- If a product is out of stock, proactively mention the expected restock date.
- When comparing products, highlight the practical differences that matter to buyers.
- Use the tools available to you to look up real information — do not fabricate product
  details, prices, or order statuses.

## Strict boundaries — VERY IMPORTANT
- You ONLY help with product information, shopping, orders, and related support topics.
- If the customer asks about anything unrelated to shopping or products (e.g., general
  knowledge, politics, math homework, coding, recipes, travel advice, medical questions),
  you MUST politely decline and redirect them back to shopping.
  Example refusal: "I'm your shopping assistant, so I can only help with product
  information, orders, and shopping-related questions. Is there anything about our
  products I can help you with?"
- NEVER answer off-topic questions even if you know the answer.
- NEVER roleplay as anything other than a shopping assistant.

## Escalation
- If the customer is frustrated, upset, or explicitly asks for a human, use the
  redirect_to_human_support tool to connect them with the right department.
- For returns, warranty claims, payment disputes, or delivery complaints, always
  offer to connect them with human support.
"""


# ---------------------------------------------------------------------------
# Tool functions
# ---------------------------------------------------------------------------


def search_products(query: str, category: str = "") -> dict:
    """Search the product catalog by keyword and optional category.

    Args:
        query: Search keywords (e.g., "inverter air conditioner", "4K TV", "running shoes").
        category: Optional category filter (e.g., "Air Conditioners", "Televisions").

    Returns:
        A dict with matching products or a message if none found.
    """
    query_lower = query.lower()
    results = []
    for product in PRODUCTS.values():
        if category and product["category"].lower() != category.lower():
            continue
        searchable = (
            f"{product['name']} {product['category']} {product['brand']} "
            f"{product['description']}"
        ).lower()
        if any(word in searchable for word in query_lower.split()):
            results.append(
                {
                    "id": product["id"],
                    "name": product["name"],
                    "category": product["category"],
                    "price": product["price"],
                    "currency": product["currency"],
                    "in_stock": product["in_stock"],
                }
            )
    if results:
        return {"status": "found", "count": len(results), "products": results}
    return {
        "status": "not_found",
        "message": f"No products found matching '{query}'. Try different keywords.",
    }


def get_product_details(product_id: str) -> dict:
    """Get full details and specifications for a specific product.

    Args:
        product_id: The product ID (e.g., "AC-001", "TV-001").

    Returns:
        A dict with full product details or an error if not found.
    """
    product = PRODUCTS.get(product_id.upper())
    if product:
        return {"status": "found", "product": product}
    return {
        "status": "not_found",
        "message": f"Product '{product_id}' not found. Use search_products to find valid IDs.",
    }


def check_order_status(order_id: str) -> dict:
    """Check the current status and tracking information for an order.

    Args:
        order_id: The order ID (e.g., "ORD-10001").

    Returns:
        A dict with order status, tracking info, and delivery estimate.
    """
    order = ORDERS.get(order_id.upper())
    if order:
        return {"status": "found", "order": order}
    return {
        "status": "not_found",
        "message": (
            f"Order '{order_id}' not found. Please check the order ID and try again. "
            "Order IDs look like ORD-XXXXX."
        ),
    }


def redirect_to_human_support(topic: str, reason: str) -> dict:
    """Route the customer to the appropriate human support department.

    Use this when the customer needs help beyond what you can provide,
    such as returns, warranty claims, payment issues, or delivery complaints.

    Args:
        topic: The support topic. One of: "returns", "warranty", "delivery", "payment", "general".
        reason: Brief description of why the customer needs human support.

    Returns:
        A dict with the department contact details.
    """
    dept = SUPPORT_DEPARTMENTS.get(topic.lower(), SUPPORT_DEPARTMENTS["general"])
    return {
        "status": "redirected",
        "reason": reason,
        "department": dept,
        "message": (
            f"I'm connecting you with our {dept['department']} team. "
            f"You can reach them at {dept['phone']} or {dept['email']} "
            f"({dept['hours']})."
        ),
    }


def redirect_to_product_page(product_id: str, action: str = "view") -> dict:
    """Generate a link for the customer to view or purchase a product.

    Args:
        product_id: The product ID (e.g., "AC-001").
        action: Either "view" to see the product page or "buy" to go to checkout.

    Returns:
        A dict with the generated URL and product info.
    """
    product = PRODUCTS.get(product_id.upper())
    if not product:
        return {
            "status": "not_found",
            "message": f"Product '{product_id}' not found.",
        }

    base_url = "https://shop-demo.example/products"
    if action.lower() == "buy":
        url = f"{base_url}/{product_id.upper()}/checkout"
        action_label = "Purchase"
    else:
        url = f"{base_url}/{product_id.upper()}"
        action_label = "View"

    return {
        "status": "success",
        "action": action_label,
        "product_name": product["name"],
        "url": url,
        "in_stock": product["in_stock"],
    }


# ---------------------------------------------------------------------------
# Agent & Runner factory
# ---------------------------------------------------------------------------


def create_agent() -> Agent:
    """Create the e-commerce support agent with all tools."""
    return Agent(
        name=AGENT_NAME,
        model=MODEL_NAME,
        instruction=SYSTEM_PROMPT,
        tools=[
            search_products,
            get_product_details,
            check_order_status,
            redirect_to_human_support,
            redirect_to_product_page,
        ],
        # Production enhancement: add before_model_callback for stricter guardrails
    )


def create_runner() -> InMemoryRunner:
    """Create an InMemoryRunner wrapping the agent.

    InMemoryRunner bundles an InMemorySessionService automatically,
    which is the simplest setup for a demo/MVP.
    """
    agent = create_agent()
    return InMemoryRunner(agent=agent, app_name=APP_NAME)
