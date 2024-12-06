from supabase import create_client
from django.conf import settings
import os
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')

supabase = create_client(supabase_url, supabase_key)

def get_supabase_client():
    """
    Returns a Supabase client instance
    """
    return supabase
