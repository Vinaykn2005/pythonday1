class instagramAccountSystem:
    def __init__(self, account_name, password):
        self.account_name = account_name
        self.__password = password
        self._private_reel = []
        self.__archieved_reel = []

    def add_private_reel(self, private_reel):
        self._private_reel.append(private_reel)
        print("The reel is uploaded!",private_reel)

    def display_private_reel(self, is_follwer):
        if is_follwer:
            print("The reels are:")
            for i in self._private_reel:
                print(i)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archieved_reel(self, archived_reel):
        self.__archieved_reel.append(archived_reel)

    def display_archieved_reel(self, password):
        print("The archieved reel are:")
        if password == self.__password:
            for i in self.__archieved_reel:
                print(i)
        else:
            print("Access Denied! Only followers can view private reels")

    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully")
        else:
            print("Incorrect old password")

InstagramAccount = instagramAccountSystem("Vinaygowda", "1234")
InstagramAccount.add_private_reel("Singing")
InstagramAccount.add_private_reel("Dancing")
InstagramAccount.add_private_reel("playing")
InstagramAccount.display_private_reel(True)
InstagramAccount.add_archieved_reel("Daily bloog")
InstagramAccount.add_archieved_reel("playing cricket with friends")
InstagramAccount.add_archieved_reel("Mini Bloog")
InstagramAccount.display_archieved_reel("123")
InstagramAccount.set_password("1234","2313")