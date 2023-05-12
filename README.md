# pograncontrol
Research of the russian tg chat about crossing the border on unsuccessful cases of crossing the border

Исследование про чат "Пограничный контроль" - российского телеграмм-чата про пересечения границы на неудачные случаи пересеения границы
______
Всем привет. Это мой проект исследования случаев пересечения россиянами российской границы с начала мобилизации. Предварительные результаты исследования можно посмотреть в моей статье на [VC.ru] (https://vc.ru/migrate/614458-v-preddverii-poslaniya-federalnomu-sobraniyu-i-v-chest-nastupayushchego-prazdnika-rasskazyvayu-kogo-ne-vypustili-zagranicu): 
>*Все наработки из этого проекта доступны для свободного использования в рамках лицензий используемых фреймоворков. Можете еще и меня упомянуть, если будете где-то это использовать, хотя я сильно в этом сомневаюсь*
## На данный момент в репозитории:
### Приложение для разметки pograncotrol.py
Десктопное приложение для разметки. Необходимо для разметки сообщений с случаями пересечения границы. Сообщения берет из БД.
### Приложение для сепарации сообщений pograncotrol.py
Десктопное приложение для сепарции сообщений. В некоторых сообщениях из чата содержится несколько случаев разделенных разделителем, состоящим из нижних подчеркиваний. Приложение берет сообщения из БД и записывает разделенные части в БД.
### Скрипт chatreader.py
Предназначен для сбора сообщений из чата телеграм и записи их в БД.
### Папка pograncontrol
Содержит в себе описание UI для десктопных приложений
### Папка site
Сайт на django c двумя сервисами: razmetka - сервис для разметки случаев, аналог декстопного приложения pograncotrol.py и pogran_visualisation - будущий сервис с визуализацией данных.
### Файл case_list.csv
Так как разметка продолжается, ценного в этом файле мало.

Содержит размеченые сообщения с случаями пересечения границы по следующим полям
* `id` - уникальный номер случая
* `msg_id` - уникальный номер сообщения, по которому размечен этот случай
* `case_mes_id` - уникальный номер части сообщения, по которой размечен этот случай
* `case_type` - тип случая: `success` - удачный, `fail` - неудачный, `return` - возврат
* `age` - возраст пересекающего границу
* `sex` - пол пересекающего границу
* `cause` - причина отказа в пересечении
* `army_relations` - отношение к воинской службе пересекающего
* `vus` - военно-учетная специальность пересекающего границу.
* `army_type` - вид войск, к которому относится пересекающий.
* `army_sec_type` - род войск (в том числе и отдельные рода войск), к которому относится пересекающий.
* `army_other` - другая информация о военной службе, предоставленная пересекающим.
* `country` - страна въезда
* `kpp` - контрольно-пропускной пункт выезда
* `yService` - годы службы, если человек их указал
* `voenk_region` - региональный (в т. ч. и ГФЗ)военкомат прописки, если человек его указал
* `voenk_city` - городской военкомат прописки, если человек его указал
* `voenk_district` - районный военкомат прописки, если человек его указал
* `kategory_h` - категория здоровья человека
* `kategory_z` - категория запаса человека
* `date` - дата сообщения или пересечения границы

### Файл mes_list.csv

Содержит размеченые сообщения из чата с 20.09.2022 по 12.04.2023 с уникальным номером и датой публикации

### Файл сase_text_list.csv

Содержит разделенные случаи из сообщений из чата с 20.09.2022 по 12.04.2023
* `id` - уникальный номер части сообщения
* `msg_id` - уникальный номер сообщения, из которого получена эта часть
* `text` - текст
* `tag` - метка части: `marked` - размечена, `busy` - занята пользователем, `delete` - к удалению, `pass` - пропушена пользователем, `manual` - требует ручной разметки
* `author` - автор разметки

## В планах:
* Разметить все сообщения, написать красивую страницу с визуализацией результатов
* При разметке достаточного количества сообщений прикрутить нейронную сеть для категоризации
Помочь разметить сообщения вы можете по адресу: <http://194.87.94.250:8000/razmetka/>. Логин и пароль запросите у меня по адресу aasmr@ya.ru, в теме письма укажите: "Разметка. Погранконтроль"
