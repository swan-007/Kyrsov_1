import Class_vk
import Class_ya
import configparser
config = configparser.ConfigParser()
config.read("settings.ini")
if __name__ == '__main__':
    user_id = input('Введите id пользователя VK или screen_name - ')
    stv = Class_vk.vk(user_id, config["set"]["vk_token"])
    stv.user_ids()
    stv._get_pho()
    yy = Class_ya.yandex(config["set"]["ya_token"])
    yy.check_path_2()
    yy.check_2()
    yy.zag_2()
