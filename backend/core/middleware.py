from django.http import JsonResponse
from django.conf import settings
from .supabase import get_supabase_client
import jwt

class SupabaseAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip authentication for certain paths
        if request.path.startswith('/admin/') or request.path.startswith('/api/public/'):
            return self.get_response(request)

        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'No authentication token provided'}, status=401)

        token = auth_header.split(' ')[1]
        try:
            # Verify the JWT token
            supabase = get_supabase_client()
            user = supabase.auth.get_user(token)
            request.user = user
            return self.get_response(request)
        except Exception as e:
            return JsonResponse({'error': 'Invalid authentication token'}, status=401)
