class NewsPublisher:
    def __init__(self):
        self._observers = []
        self._latest_news = None

    def register(self, observer):
        self._observers.append(observer)

    def unregister(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._latest_news)

    def add_news(self, news):
        self._latest_news = news
        print(f"Noticia nueva publicada: {news}")
        self.notify_observers()


class NewsSubscriber:
    def __init__(self, name):
        self.name = name

    def update(self, latest_news):
        print(f"{self.name} recibió la noticia: {latest_news}")


if __name__ == "__main__":
    news_publisher = NewsPublisher()

    app1 = NewsSubscriber("App de Noticias 1")
    app2 = NewsSubscriber("App de Noticias 2")
    app3 = NewsSubscriber("App de Noticias 3")

    news_publisher.register(app1)
    news_publisher.register(app2)
    news_publisher.register(app3)

    news_publisher.add_news("Se aprueba nueva ley")

