"""middleware"""
import time
from fastapi import Request

user_API_details = {}

rate_limiting = {
    "free": (10, 60),
    "freemium": (10, 1200)
}

class CustomMiddleware:
    """"""
    def __init__(self, app, paths: list):
        self.app = app
        self.paths = paths


    async def __call__(self, scope, receive, send):
        """"""
        if scope['path'] in self.paths:
            request = Request(scope, receive)
            user_id = request.headers.get('user_id')
            user_subscription = request.headers.get('user_subscription')
            if not user_id or not user_subscription or user_subscription not in rate_limiting:
                raise Exception("Missing user_id or user_subscription")
            current_time = time.time()
            limit, api_time = rate_limiting[user_subscription]

            user_API_details[user_id] = [timestamp for timestamp in user_API_details.get(user_id, []) if timestamp > current_time - api_time ]
            print(user_API_details)
            if len(user_API_details[user_id]) > limit:
                raise Exception("Too many API calls")
            user_API_details[user_id].append(current_time)
        return await self.app(scope, receive, send)