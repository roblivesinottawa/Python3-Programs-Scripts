from typing import AsyncGenerator


# def profile():
#     global name 
#     global age 
#     name = "Rob"
#     age = 35

# profile()
# print(name)
# print(age)


def profile():
    name = "Rob"
    age = 35
    return name, age

profile_name, profile_age = profile()
print(profile_name)
print(profile_age)