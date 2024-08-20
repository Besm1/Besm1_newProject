from time import sleep
# import tkinter as tk
"""
Полностью инкапсулированные классы.
"""

# print(help(tkinter))

class User:
    def __init__(self, nickname:str, password:str, age:int):
        self.__nickname = nickname
        self.__password = hash(password)
        self.__age = age

    def __str__(self):
        return f'{self.__nickname}, {self.__age} лет.'

    def get_nick(self) -> str:
        return self.__nickname

    def get_hashed_pwd(self) -> int:
        return self.__password

    def get_age(self) -> int:
        return self.__age


class Video:
    def __init__(self, title:str, duration:int, adult_mode=False):
        self.__title = title
        self.__duration = duration
        self.__adult_mode = adult_mode
        self.__time_now: int = 0

    def __str__(self):
        return f'{self.__title}, {self.__duration} сек.' + (' (18+)' if self.__adult_mode else '')

    def get_title(self) -> str:
        return self.__title

    def get_duration(self) -> int:
        return self.__duration

    def get_adult_mode(self) -> bool:
        return self.__adult_mode

    def get_time_now(self) -> int:
        return self.__time_now

    def set_time_now(self, time: int):
        if time <= self.__duration:
            self.__time_now = time


class UrTube:
    def __init__(self):
        self.__users = []
        self.__videos = []
        self.__current_user = None

    def add(self, *vidosiki):
        for v_ in [new_v for new_v in vidosiki if isinstance(new_v, Video)  # добавляем только объекты класса Video
                                                                            # которых ещё нет на сайте
                                                  and new_v.get_title() not in [exist_v.get_title()
                                                                                for exist_v in self.__videos]]:
            print(f'* Добавляем на сайт фильм "{v_.get_title()}"')
            self.__videos.append(v_)

    def get_videos(self, pattern: str):
        print(f'* Подбираем фильмы, в названии которых есть строка "{pattern}"')
        return [str(v_) for v_ in self.__videos if v_.get_title().lower().find(pattern.lower()) >= 0]

    def register(self, username: str, password: str, age: int):
        print(f'* Попытка регистрации пользователя {username}')
        if username not in [n_.get_nick() for n_ in self.__users]:
            self.__current_user = User(username, password, age)
            self.__users.append(self.__current_user)
            print(f'  Приятно познакомиться, {self.__current_user.get_nick()}! ')
        else:
            self.__current_user = None
            print(f'  Пользователь {username} уже зарегистрирован.')

    def log_in(self, username, password):
        print(f'* Попытка входа пользователя {username}.')
        user = [u_ for u_ in self.__users if u_.get_nick().lower() == username.lower()]
        if len(user) == 1:  # Существует такой пользователь! И он ровно один.
            print(f'  {user[0].get_nick()}, это ты?')
            if user[0].get_hashed_pwd() == hash(password):
                print(f'  Здравствуй, {user[0].get_nick()}! Выбирай фильм. Приятного просмотра!')
                self.__current_user = user[0]
            else:
                print(f'  Что-то ты на себя не похож... Вспоминай пароль!')
                self.__current_user = None
        else:
            print(f'  {username}, или я тебя не знаю, или ты имя своё забыл. Вспомни имя или зарегистрируйся на UrTube.')

    def log_out(self):
        print('* Попытка выхода')
        if self.__current_user is None:
            print('  А никто и не входил!..')
        else:
            print(f'  До свидания, {self.__current_user.get_nick()}! Приходи ещё!')
            self.__current_user = None

    def watch_video(self, film_name: str):
        print(f'* Пользователь {self.__current_user} хочет посмотреть фильм "{film_name}".')
        if self.__current_user is None:
            print('  Сначала войди или зарегистрируйся на сайте!')
        else:
            video = [v_ for v_ in self.__videos if v_.get_title() == film_name]
            if len(video) == 1: # Такой фильм есть! И он один.
                if not video[0].get_adult_mode() or self.__current_user.get_age() >= 18:
                    Player(video[0])
                else:
                    print(f'  {self.__current_user.get_nick()}, тебе рано ещё смореть такие фильмы! '
                          + f'Приходи лет эдак через {18 - self.__current_user.get_age()}!')
            else:
                print(f'  Фильм "{film_name}" не найден, наверное, ещё не завезли. Попробуй позже.')


class Player:

    def __init__(self, vidos: Video):

        # window = tk.Tk()
        #
        # window.title(vidos.title)
        # window.geometry('800x450')
        # window.resizable(False, False)
        # text = tk.Entry(window, width=60)
        # text.place(x=200, y=220)
        # text.insert(0, f'Смотрим: {vidos.time_now} сек.')
        # while vidos.time_now < vidos.duration:
        #     sleep(1)
        #     vidos.time_now += 1
        #     text.delete(0, 'end')
        #     text.insert(0, f'Смотрим: {vidos.time_now} сек.')
        # text.insert(0, 'Ребята, а что вы тут делаете, а? Кино-то давно кончилось!')
        # window.mainloop()
        # button = tk.Button(window, text='Закрыть плеер', width=40, height=5)

        print(f'  Смотрим фильм "{str(vidos)}"')
        while vidos.get_time_now() < vidos.get_duration():
            sleep(1)
            vidos.set_time_now(vidos.get_time_now() + 1)
            print(f'  {vidos.get_time_now()}', end = '')
        print('  Ребята, а что вы тут делаете, а? Кино-то давно кончилось!')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(f"  {ur.get_videos('лучший')}")
    print(f"  {ur.get_videos('ПРОГ')}")

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.log_out()
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

    # Попытка воспроизведения несуществующего видео
    ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
    ur.watch_video('Лучший язык программирования 2024 года!')
    ur.log_out()
