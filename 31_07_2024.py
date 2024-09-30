
user_role = 'manager'  # Можно менять на 'admin' или другие роли для тестирования

def role_required(role: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user_role == role:
                return func(*args, **kwargs)
            else:
                return 'Permission denied'
        return wrapper
    return decorator

@role_required('admin')
def secret_resource() -> str:
    return 'Permission accepted'

# Примеры использования
print(secret_resource())  # Выведет 'Permission denied', так как роль 'manager'
user_role = 'admin'
print(secret_resource())
2
RU_TO_EN = {
    'привет': 'hello',
    'мир': 'world',
    'еда': 'food',
}

RU_TO_LT = {
    'привет': 'sveiki',
    'мир': 'pasaulis',
    'еда': 'maistas',
}

def translate_to(lang: str):
    def decorator(func):
        def wrapper(word: str) -> str:
            translation = word
            if lang == 'EN':
                translation = RU_TO_EN.get(word, word)
            elif lang == 'LT':
                translation = RU_TO_LT.get(word, word)
            return translation
        return wrapper
    return decorator

@translate_to('EN')
def say(word: str) -> str:
    return word

# Примеры использования
print(say('привет'))  #
print(say('мир'))


@translate_to('LT')
def say_lithuanian(word: str) -> str:
    return word

print(say_lithuanian('привет'))
print(say_lithuanian('мир'))
