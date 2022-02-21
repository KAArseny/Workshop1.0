#! / usr / bin / env python3
# Импортируем библиотеку vk_api
import vk_api
import wikipedia

wikipedia.set_lang("RU")
# Достаём из неё longpoll
from vk_api.longpoll import VkLongPoll, VkEventType

# Создаём переменную для удобства в которой хранится наш токен от группы
token = "f2cca1ade558b8d7bb39ef0b15771f226010d84f640436bb85c4b099b134eaef8ddc78f411420e06c5458"  # В ковычки вставляем аккуратно наш ранее взятый из группы токен.

# Подключаем токен и longpoll
bh = vk_api.VkApi(token=token)
give = bh.get_api()
longpoll = VkLongPoll(bh)


# Создадим функцию для ответа на сообщения в лс группы
def blasthack(id, text):
    bh.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})

# Слушаем longpoll(Сообщения)
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        # Чтобы наш бот не слышал и не отвечал на самого себя
        if event.to_me:

            # Получаем id пользователя
            id = event.chat_id

            if event.text == 'Привет' or event.text == 'привет' or event.text == 'ку' or event.text == 'Ку':
                blasthack(id, 'Ку!')
            elif event.text == 'Учёбы много' or event.text == 'Учебы много' or event.text == 'учёбы много' or event.text == 'учебы много':
                bh.method("messages.send", {"peer_id": 2000000000 + id, "attachment": "photo-210448461_457239018", "random_id": 0})

            elif event.text == 'Пока' or event.text == 'пока':
                blasthack(id, 'Покеда)')

            elif event.text == 'Смотри':
                bh.method("messages.send", {"peer_id": 2000000000+id, "attachment": "photo-210448461_457239020", "random_id": 0})

            elif event.text == 'Спокойной ночи' or event.text == 'спокойной ночи':
                bh.method("messages.send", {"peer_id": 2000000000+id, "attachment": "photo-210448461_457239024", "random_id": 0})

            elif event.text == 'В чём смысл жизни?' or event.text == 'в чем смысл жизни?' or event.text == 'В чем смысл жизни?' or event.text == 'в чём смысл жизни?':
                bh.method("messages.send", {"peer_id": 2000000000 + id, "attachment": "photo-210448461_457239025", "random_id": 0})
            elif event.text == "Вики" or event.text == 'вики' or event.text == 'Википедия':
                blasthack(id,"Что ищем?)")
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW:
                        if event.to_me:
                            blasthack(id, "Держи ссылку\n" + str(wikipedia.page(event.text).url) + '\n' + 'И инфу\n' + str(wikipedia.summary(event.text, sentences=7)))
                            break
                continue
            elif event.text == 'Как дела?':
                blasthack(id, "Жду Судного дня)))")

















