# Python-Engineering-Core
Python project structure · Classes + OOP for APIs · Typing + Pydantic basics…

# Day 1
Explored Python project structure, created a dummy backend structure to understand the flow. Ran main.py file to see how the trace appears. main.py -> routes.py -> service.py -> models.py
<python -m main.py>

# Day 2
- API routes should stay lightweight. Example: `get_order_delivery_info()` calls `get_order()` service instead of writing business logic directly inside the route.
- Service functions can reuse other services. Example: `get_payment_msg()` internally calls `get_order(order_id)` to fetch order details.
- Learned to handle returned object types correctly. Example: `get_order()` returns an `Order` object, so fields are accessed like `order.name`, while `get_payment_msg()` returns a string directly.
- Practiced testing endpoints in FastAPI. Example: GET endpoint tested with `/?order_id=1`, while POST endpoint `/payment_msg` was tested through Swagger docs at `/docs`.

Ran <uvicorn app.api.routes:app --reload> to see how the trace appears. Can see the end-point locally with the url. <http://127.0.0.1:8000/?order_id=1> has required request param order_id. 