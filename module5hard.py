import hashlib
from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}, {self.age} лет.'

    def user_name(self):
        return self.nickname

    def find(self, username):
        return self.nickname.find(username)

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}, {self.duration} сек.'  + (' (18+)' if self.adult_mode else '')

class UrTube:
    def __init__(self, users = [], videos = []):
        self.users = users
        self.videos = videos
        self.current_user = None

    def add(self, *vidosiki):
        if all([isinstance(o_, Video) for o_ in vidosiki]):
            for v_ in [new_v for new_v in vidosiki if new_v.title not in [exist_v.title for exist_v in self.videos]]:
                print(f'Добавляем на сайт фильм "{v_.title}"')
                self.videos.append(v_)


    def get_videos(self, pattern: str):
        return [str(v_) for v_ in self.videos if v_.title.lower().find(pattern.lower()) >= 0]

    def register(self,username:str, password: str, age: int):
        if username not in [n_.nickname for n_ in self.users]:
            self.current_user = User(username, password, age)
            self.users.append(self.current_user)
            print(f'Приятно познакомиться, {self.current_user.nickname}! ')
        else:
            self.current_user = None
            print(f'Пользователь {username} уже существует')


    def log_in(self, username, password):
        user = [u_ for u_ in self.users if u_.user_name().lower() == username.lower()]
        if len(user) == 1:
            print(f'{user[0].nickname}, это ты?')
            if user[0].password == hash(password):
                print(f'Здравствуй, {user[0].nickname}! Выбирай фильм. Приятного просмотра!')
                self.current_user = user[0]
            else:
                print(f'Что-то ты на себя не похож... Вспоминай пароль!')
                self.current_user = None
        else:
            print(f'{username}, или я тебя не знаю, или ты имя своё забыл. Вспомни имя или зарегистрируйся на UrTube.')


    def log_out(self):
        if self.current_user != None:
            print('А никто и не зарегистрирован!..')
        else:
            print(f'До свидания, {self.current_user.nickname}! Приходи ещё!')
            self.current_user = None

    def watch_video(self,film_name: str):
        video = [v_ for v_ in self.videos if v_.title == film_name]
        if len(video) == 1:
             if not video.adult_mode or self.current_user.age >= 18:
                 print(f'Смотрим фильм {str(video)}')
             else:
                 print(f'{self.current_user.nickname}, тебе рано ещё смореть такие фильмы! '
                       + f'Приходи лет эдак через {18 - self.current_user.age}!')
        else:
            print(f'Фильм "{film_name}" не найден, наверное, ещё не завезли. Попробуй позже.')



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
v3 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v4 = Video('Для чего девушкам парень шахматист?', 10, adult_mode=True)
ur.add(v3, v4)
#
# print([exist_v.title for exist_v in ur.videos])
# print(v3.title not in [exist_v.title for exist_v in ur.videos])
# for v_ in [new_v for new_v in (v3,v4) if new_v.title not in [exist_v.title for exist_v in ur.videos]]:
#     print(str(v_))

# # print(v1.title.lower().find('Лучший'))
#
#
# # print(ur.videos)
# # # print([v_ for v_ in [tv_ for tv_ in ur.videos]])
# # Проверка поиска
# print('поиск')
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
#
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# print(f'Текущий пользователь:  {str(ur.current_user)}')
# # ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# print(f'Текущий пользователь:  {str(ur.current_user)}')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# print(f'Текущий пользователь:  {str(ur.current_user)}')
#
# print('Список пользователей:', [str(u_) for u_ in ur.users])
#
# ur.log_in('vasya_pupkin', 'lolkekcheburek')
# print(f'Текущий пользователь:  {str(ur.current_user)}')
# ur.log_in('vasya_pupkin', 'lolkekbelyash')
# print(f'Текущий пользователь:  {str(ur.current_user)}')
# ur.log_in('vasya_popkin', 'lolkekbelyash')
# print(f'Текущий пользователь:  {str(ur.current_user)}')
#
# # if __name__ == '__main__':
# #     while true
