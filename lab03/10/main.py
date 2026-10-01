def check_string_truthiness(text: str) -> None:
    if text:
        print(f"{text!r} -> True")
    else:
        print(f"{text!r} -> False")

test_strings = [
    "",
    "Hello world!",
    " ",
    "False",
    "0",
]

for s in test_strings:
    check_string_truthiness(s)

user_input = ""
default_name = "Гость"

active_user = user_input or default_name
print(f"\nИмя пользователя: {active_user!r}")