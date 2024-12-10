from supabase import create_client

# Your Supabase configuration
SUPABASE_URL = "https://miwagyoykpqvocoiczvu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1pd2FneW95a3Bxdm9jb2ljenZ1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzM3MDg0MDAsImV4cCI6MjA0OTI4NDQwMH0.B7EXzIlX3FQfxl4HwSFiOuhAUiKOeaG0x5itrF0bIFo"

# Create and export the client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

