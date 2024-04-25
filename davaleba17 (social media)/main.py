class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comment_likes = 0

    def add_like(self):
        self.comment_likes += 1

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        self.likes = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self, user):
        self.likes.append(user)

class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.friend_list = []

    def add_friend(self, friend):
        self.friend_list.append(friend)
        friend.friend_list.append(self)

    def create_post(self, content):
        post = Post(content, self.username)
        self.posts.append(post)
        return post

    def comment_on_post(self, post, content):
        comment = Comment(content, self.username)
        post.add_comment(comment)

    def like_post(self, post):
        post.add_like(self.username)

    def like_comment(self, comment):
        comment.add_like()

    def display_posts(self):
        if self.posts:
            print(f"Posts by {self.username}:")
            for i, post in enumerate(self.posts, 1):
                print(f"Post {i}: {post.content} - Likes: {len(post.likes)}")
                if post.comments:
                    print("Comments:")
                    for comment in post.comments:
                        print(f"- {comment.content} by {comment.author}. Likes: {comment.comment_likes}")
                else:
                    print("No comments")
        else:
            print(f"No posts by {self.username}")


user1 = User("User1")
user2 = User("User2")

user1.add_friend(user2)

post1 = user1.create_post("Hello world!")

user2.comment_on_post(post1, "Nice post!")

comment = post1.comments[0]
user2.like_comment(comment)

user1.like_post(post1)

post2 = user2.create_post("Another message")

user2.like_post(post2)

user1.display_posts()
user2.display_posts()
