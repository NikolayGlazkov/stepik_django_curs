from django.db import models


class Client(models.Model):
    city = models.CharField(
        max_length=50, verbose_name="Город создания договора", blank=True, null=True
    )
    fio = models.CharField(max_length=70, verbose_name="Имя клиента",blank=True, null=True)
    passSeries = models.CharField(max_length=4, verbose_name="Серия паспорта клиента", blank=True, null=True)
    passNum = models.CharField(max_length=6, verbose_name="Номер паспорта клиента", blank=True, null=True)
    passHome = models.CharField(
        max_length=200, verbose_name="Орган выдавший паспорт клиента", blank=True, null=True
    )
    passDate = models.CharField(max_length=12,verbose_name="Дата выдачи паспорта клиента", blank=True, null=True)
    passCode = models.CharField(
        max_length=8, verbose_name="Код подразделения паспорта клиента", blank=True, null=True
    )
    registration = models.CharField(max_length=250, verbose_name="Прописка клиента", blank=True, null=True)
    postIndex = models.CharField(max_length=10, verbose_name="Почтовый индекс", blank=True, null=True)
    inn = models.CharField(max_length=20, verbose_name="ИНН клиента", blank=True, null=True)
    snils = models.CharField(max_length=15, verbose_name="СНИЛС клиента", blank=True, null=True)
    clientMail = models.EmailField(verbose_name="Электронная почта клиента участника", blank=True, null=True)
    clientPhone = models.CharField(
        max_length=20, verbose_name="Номер телефона клиента участника", blank=True, null=True
    )
    bank_rs_num = models.CharField(max_length=20, verbose_name="Р/С номер участника", blank=True, null=True)
    bankName = models.CharField(max_length=50, verbose_name="Название банка участника", blank=True, null=True)
    bankBik = models.CharField(max_length=10, verbose_name="БИК банка участника", blank=True, null=True)
    bank_ks_num = models.CharField(max_length=20, verbose_name="К/С номер участника", blank=True, null=True)
    bankKpp = models.CharField(max_length=10, verbose_name="КПП банка участника", blank=True, null=True)
    bankInn = models.CharField(max_length=10, verbose_name="ИНН банка участника", blank=True, null=True)
    doverenost = models.CharField(
        max_length=15, default="", blank=True, verbose_name="Доверенность"
    )
    the_end_of_dever = models.CharField(max_length=12,
        null=True, blank=True, verbose_name="Дата окончания доверенности"
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"Клиент: {self.fio}"


class AuctionInfo(models.Model):
    url = models.CharField(max_length=150, verbose_name="URL аукциона")
    lotNum = models.CharField(max_length=30, verbose_name="Номер лота")
    docPrice = models.IntegerField(verbose_name="Цена документа")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")

    class Meta:
        verbose_name = "Информация об аукционе"
        verbose_name_plural = "Информация об аукционах"

    def __str__(self):
        return f"Клиент: {self.client.fio}, Аукцион: {self.url}, Цена: {self.docPrice}"
