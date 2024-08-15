import hashlib
from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = 0
        self.adult_mode = adult_mode

    def find(self, search_str: str):
        return self.title.find(search_str)


class UrTube:
    def __init__(self, users = [], videos = []):
        self.users = users
        self.videos = videos
        self.current_user = None

    def add(self, *other):
        if all([isinstance(o_, Video) for o_ in other]):
            for v_ in other:
                self.videos.append(v_)

    def get_videos(self, pattern: str):
        return [v_ for v_ in [tv_ for tv_ in self.videos] if str(v_.title).find(pattern) != None]


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
# print(ur.videos)
# print([v_ for v_ in [tv_ for tv_ in ur.videos]])
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))


# if __name__ == '__main__':
#     while true
