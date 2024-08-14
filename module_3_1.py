calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(s):
    count_calls()
    return len(s), s.upper(), s.lower()

def is_contains(string, lst):
    count_calls()
    lower_string = string.lower()
    return lower_string in [item.lower() for item in lst]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)