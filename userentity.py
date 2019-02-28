class User:
    def __init__(self, user_id,first_name,last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return 'User({})'.format(self.user_id)

    def sort_notcompare():
        users = [User(23,"Jones","Brian"), User(3,"Big","Jones"), User(99,"David","Beazley")]
        print(users)
        print(sorted(users, key=lambda u: u.user_id))
        print(sorted(users, key=attrgetter('user_id')))



from operator import attrgetter
if __name__ == "__main__":
    print(User.__class__)
    print(User.__class__.__base__)
    User.sort_notcompare()