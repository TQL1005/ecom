from supabase import create_client

# Your Supabase configuration
SUPABASE_URL = "https://miwagyoykpqvocoiczvu.supabase.co"
SUPABASE_KEY = "YOUR_KEY"

# Create and export the client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

