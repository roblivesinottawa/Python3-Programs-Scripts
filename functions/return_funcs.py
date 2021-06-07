def greet(name="Captain America"):
    def greettwo():
        return "this is the first function"

    def welcome():
        return "Now you are in the second function"

    if name == "Captain America":
        return greettwo
    else:
        return welcome


result = greet()
print(result())