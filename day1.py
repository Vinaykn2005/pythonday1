class Instagram:
    def __init__(self,title, description, creator_name, location):  
        self.title = title
        self.description = description
        self.likes = 0
        self.comment = []
        self.creator_name = creator_name
        self.location = location
    
    def display_title(self):
        print("The title of the reel is ",self.title)
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_likes(self):
        print("The likes of the reel is ",self.likes)
    def liked(self):
        self.likes += 1
    def disliked(self):
        if self.likes > 0:
            self.likes-=1
    def add_comments(self, comment_text):
        self.comment.append(comment_text)
    
    def display_comment(self):
        print("The comment section ")
        for i in self.comment:
            print(i)
    def display_creator_name(self):
        print("The name of the creator ",self.creator_name)
    def display_location(self):
        print("The Location of User ",self.location)


    def remove_comments(self):
        delete1 = self.comment.pop()
        print(delete1)
    


reel1=Instagram("Motivation Video","Consitencey is the key of success","motivators","Bengalore")
reel1.add_comments("we win")
reel1.add_comments("it inspiring")
reel1.remove_comments()

reel1.liked() 
reel1.liked() 

reel1.disliked() 
reel1.display_likes()

reel1.display_location()
reel1.display_creator_name()
reel1.display_comment()


print(id(reel1))

