"""
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight:
    color = ""

    def running(self):
        while True:
            TrafficLight.color = "red"
            print(f"\033[31m{TrafficLight.color}")
            time.sleep(7)
            TrafficLight.color = "yellow"
            print(f"\033[33m{TrafficLight.color}")
            time.sleep(2)
            TrafficLight.color = "green"
            print(f"\033[32m{TrafficLight.color}")
            time.sleep(5)
            TrafficLight.color = "yellow"
            print(f"\033[33m{TrafficLight.color}")
            time.sleep(2)


new_TL = TrafficLight()
new_TL.running()
