# async_test/views.py

from django.http import JsonResponse
import asyncio

async def async_view(request):
    # Simulate some async work (e.g., waiting for a response)
    await asyncio.sleep(2)  # Simulate a delay (e.g., database query, external API call)
    
    # Return a JSON response
    return JsonResponse({"message": "Async operation completed successfully!"})

