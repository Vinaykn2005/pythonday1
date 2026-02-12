class Session:
    def __init__(self):
        print("Session Started ")
    def __del__(self):
        print("Session end!...")

del1 = Session()
