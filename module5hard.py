import hashlib
from time import sleep
import tkinter as tk


# print(help(tkinter))

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
        self.time_now: int = 0

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
                # print(f'Добавляем на сайт фильм "{v_.title}"')
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
        if self.current_user == None:
            print('Сначала войди или зарегистрируйся на сайте!')
        else:
            video = [v_ for v_ in self.videos if v_.title == film_name]
            if len(video) == 1:
                 if not video[0].adult_mode or self.current_user.age >= 18:
                     print(f'Смотрим фильм "{str(video[0])}"')
                     p = Player(video[0])
                 else:
                     print(f'{self.current_user.nickname}, тебе рано ещё смореть такие фильмы! '
                           + f'Приходи лет эдак через {18 - self.current_user.age}!')
            else:
                print(f'Фильм "{film_name}" не найден, наверное, ещё не завезли. Попробуй позже.')

class Player():

    def __init__(self, vidos: Video):

        # window = tk.Tk()
        #
        # window.title(vidos.title)
        # window.geometry('800x450')
        # window.resizable(False, False)
        # text = tk.Label(window, text=f'Смотрим: {vidos.time_now} сек.')
        # text.place(x=350,y=220)
        # while vidos.time_now <= vidos.duration:
        #     sleep(1)
        #     vidos.time_now += 1
        #     text = tk.Label(window, text=f'Смотрим: {vidos.time_now} сек.')
        #     text.place(x=350, y=220)
        # text = tk.Label(window, text='Ребята, а что вы тут делаете, а? Кино-то давно кончилось!')
        # text.place(x=350, y=220)
        # button = tk.Button(window, text='Закрыть плеер', width=40, height=5)
        # window.mainloop()
        print(f'Смотрим: {vidos.time_now} сек.')
        while vidos.time_now < vidos.duration:
            sleep(1)
            vidos.time_now += 1
            print(f'Смотрим: {vidos.time_now} сек.')
        print('\nРебята, а что вы тут делаете, а? Кино-то давно кончилось!\n\n')




if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
    ur.watch_video('Лучший язык программирования 2024 года!')