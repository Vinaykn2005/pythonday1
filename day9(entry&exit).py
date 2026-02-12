class DatabaseConnected:
    def __enter__(self):
        print("Database Connected")
        return self  
    def __exit__(self, exit_type, exit_value, traceback):
        print("Database closed")

with DatabaseConnected():
    print("performing Querys...")
    