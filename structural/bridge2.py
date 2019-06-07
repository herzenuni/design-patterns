class TVBase:
    """Реализация - Абстрактный телевизор"""
    def tune_channel(self, channel):
        raise NotImplementedError()


class SonyTV(TVBase):
    """Конкретная реализация - Телевизор Sony"""
    def tune_channel(self, channel):
        print(f"Sony TV: выбран {channel} канал")


class SharpTV(TVBase):
    """Конкретная реализация - Телевизор Sharp"""
    def tune_channel(self, channel):
        print(f"Sharp TV: выбран {channel} канал")


class RemoteControlBase:
    """Абстракция - Абстрактный пульт управления"""
    def __init__(self):
        self._tv = self.get_tv()

    def get_tv(self):
        raise NotImplementedError()

    def tune_channel(self, channel):
        self._tv.tune_channel(channel)


class RemoteControl(RemoteControlBase):
    """Расширенная абстракция - Пульт управления #1"""
    def __init__(self):
        super().__init__()
        self._channel = 0  # текущий канал

    def get_tv(self):
        return SonyTV()

    def tune_channel(self, channel):
        super().tune_channel(channel)
        self._channel = channel

    def next_channel(self):
        self._channel += 1
        self.tune_channel(self._channel)

    def previous_channel(self):
        self._channel -= 1
        self.tune_channel(self._channel)


if __name__ == '__main__':
    #где-то в клиентском коде
    remote_control = RemoteControl()
    remote_control.tune_channel(5)  # Sharp TV: выбран 5 канал
    remote_control.next_channel() # Sharp TV: выбран 6 канал
