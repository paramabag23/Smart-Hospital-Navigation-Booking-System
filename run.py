import os
import sqlite3
import hashlib
import sys

def setup():
    """Initialize the database and create necessary folders"""
    print("="*50)
    print("🏥 LifeLine+ Setup")
    print("="*50)
    
    # Create static folder structure
    if not os.path.exists('static/css'):
        os.makedirs('static/css')
    if not os.path.exists('static/js'):
        os.makedirs('static/js')
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    print("✅ Folders created")
    
    # Initialize database
    import main
    main.init_database()
    
    print("\n✅ Setup complete!")
    print("="*50)
    print("\nTo run the application:")
    print("  python main.py")
    print("\nTest user credentials:")
    print("  Email: test@test.com")
    print("  Password: test123")
    print("="*50)

if __name__ == "__main__":
    setup()


