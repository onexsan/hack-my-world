﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define v = Character('Владос', color="#ffffff")
define r = Character('Владимир Жабовица', color="#ffffff")
define p = Character('Квакица', color="#ffffff")
define b = Character('Баржа', color="#ffffff")
define l = Character('Лягунид', color="#ffffff")
define a = Character('Кварсений', color="#ffffff")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene black

    v ". . ."

    scene bg room with fade

    v "(подскакивает) Ух!... Ох!..."

    v "Я... Вернулся? Я... снова жаба? "

    "Ты встаешь и подбегаешь к зеркалу. Из зеркала на тебя смотрит заспанная лягушка с растрепанными волосами и диким взглядом."

    v "(трогает себя за лицо) Содалв..."

    v "(трогает волосы) Прямо как мои..."

    v "(опускает взгляд вниз)"

    v "(краснеет) Так, всё! Надо разбираться, что тут происходит!"

    "Новых заметок на телефоне ты не находишь. Кажется, единственный верный способ что-то узнать — снова пойти в школу."

    menu room:
        "Пойти в школу":
            jump school

label school:
    scene black

    scene bg classroom full with fade
    "На этот раз ты приходишь в школу чуть раньше."

    "Квакица и Жабовица уже здесь - когда ты входишь в класс, они резко замолкают."

    "Ты чувствуешь, как они осторожно наблюдают за тобой, пока ты идешь к своему месту."

    v "...привет?"
    show rucaweetsa at left
    r "(нарочито расслабленно) Привет, Содалв!"

    v "(шепотом) Я не Содалв."
    show pteetsa at right
    p "(шикает на Жабовицу) Это снова он!"
    v "Что... что случилось в прошлый раз, когда я заснул?"
    r "Ну, ты упал в обморок, а потом очнулся... Будто бы. Мы хотели посидеть с тобой, но ты просто встал и побрёл домой... молча. Мы пробовали остановить тебя, но не смогли."
    v "..."
    p "А потом ты... то есть, Содалв приходил в школу. Но нас как будто не узнал. Он даже не подходил к нам поздороваться."
    r "Мы пробовали проследить за ним после уроков, но каждый раз он просто шел домой..."
    v "Может, стоит поговорить с ним?"
    scene bg classroom full
    "В класс заходит учитель - большая и будто бы вытянутая жаба с лицом, отдаленно напоминающим депутата."
    "Все замолкают."

    show thomas
    "Учитель" "(садясь) Пу-пу-пу... Ну, здравствуйте. Сегодня поговорим..."

    "Кажется, тема этого урока - moba игры?..."
    "Хотя тема тебе и интересна, в какой-то момент тебя все равно начинает клонить в сон."

    "Учитель" "А ответит... хм-хм... Содалв!"

    v "!"

    default menuset = set()

    menu lesson:

        set menuset
        "Как зовут мятежного рыцаря, персонажа популярной игры Dota 2?"

        "Tiny":
            "Учитель" "Хм-хм... неправильно! Мда..."
            jump school2

        "Sven":
            "Учитель" "Хм-хм... правильно!"
            "Учитель" "Хм... мне нравится этот вопрос. Пожалуй, включу его в тест. Так что постарайтесь {i}не забыть ответ{/i}."
            v "(в сторону) Что все это значит? Пожалуй, запишу куда-нибудь..."
            jump school2

        "Pudge":
            "Учитель" "Хм-хм... неправильно! Мда..."
            jump school2

label school2:
    "Звенит звонок."
    "Учитель" "Уффф... Пора бежать! До свидания!"
    hide thomas
    "Ты поворачиваешься к ребятам."
    show thomas
    "Учитель" "А, и кстати, Содалв."
    "Учитель" "Меня просили напомнить, что ты сегодня остаешься после уроков чистить парты от жвачек."
    v "Что? Почему?"
    "Учитель" "(пожимает плечами) Тебе лучше знать. Директор сообщил мне сегодня утром, что ты где-то набедокурил."
    "Учитель" "А любишь бедокурить, кхм-кхм! Как говорится..."
    "Учитель" "...мда..."
    "Учитель" "Мне пора!"
    hide thomas
    "Учитель уходит. Ты снова поворачиваешься к ребятам."
    show rucaweetsa at left
    show pteetsa at right
    v "Где это я... он... набедокурил?"
    r "Не знаю! Говорю, мы же за ним следили! Он сразу после уроков шел домой!"
    p "Он что, решил тебя подставить?"
    v "Да уж... возможно, стоит придумать план, прежде чем говорить с ним."
    hide rucaweetsa
    hide pteetsa
    scene black with fade

label afterschool:
    show bg classroom empty with fade
    "В конце дня ты приходишь отбывать свое наказание в ваш кабинет."
    "Жабовице и Квакице не разрешили остаться тебе помогать, но вместе с тобой в классе остались дежурить двое других твоих одноклассников..."
    $ arseny_complete = False
    $ leonid_complete = False

    menu aftertalk:

        "Поговорить с рыжей жабкой":
            show bg classroom empty with fade
            show leoneed at center
            "Ты решаешь заговорить с рыжей жабкой."
            "Вместо того, чтобы дежурить по классу, он решает судоку."
            "Впрочем, не тебе его судить — ты и сам сейчас не ползаешь под партами на кортах."
            v "...Привет?"
            "'Леонид'" "Привет."
            "Ты понимаешь, что не знаешь, с чего начать. Вывалить на него вот так всё сразу? Начать издалека?"
            v "Слушай, Л... л.."
            "'Леонид'" "...Лягунид?"
            v "Лягунид. Что бы ты сказал, если бы я сообщил тебе, что я из параллельного мира? Где мы все уже взрослые и... и не жабы? И я просто перемещаюсь туда и обратно..."
            l "(отрывая глаза от судоку) Ну, я бы попросил тебя рассказать о твоем мире побольше."
            "Ты вкратце рассказываешь Лягуниду о своем мире."
            v "То есть, тебя бы не смутило, что это... невозможно?"
            l "Ну почему сразу невозможно. Возможно. Мы же не знаем как во вселенной работает всё. Есть куча лазеек. Вот, например, грибы..."
            v "Мне сказали, что я не ел грибы."
            l "Неважно. Наверняка и другие способы бывают. А что, ты из другого мира?"
            v "Вроде того."
            l "Хм. Расскажи..."
            hide leoneed
            menu leoneed_question:
                set menuset
                "Какой мой любимый лесной гриб?"

                "Вешенка":
                    "Лягунид слушает твой рассказ о Леониде и одобрительно кивает. Кажется, к Леониду он относится с уважением."
                    jump leoneed2

                "Мухомор":
                    "Лягунид слушает твой рассказ о Леониде и одобрительно кивает. Кажется, к Леониду он относится с уважением."
                    jump leoneed2

                "Весёлка":
                    "Лягунид слушает твой рассказ о Леониде и одобрительно кивает. Кажется, к Леониду он относится с уважением."
                    jump leoneed2

            label leoneed2:
                show leoneed
                l "Интересно... Я бы хотел узнать побольше."
                v "Так ты поможешь мне?"
                l "Конечно. Я всегда рад помочь."
                "Вы договариваетесь обсудить всю ситуацию подробнее чуть позже. Ты невольно радуешься тому, как ловко у тебя получается налаживать здесь контакты."

                hide leoneed
                $ leonid_complete = True

                if leonid_complete is True and arseny_complete is True:
                    jump end
                else:
                    jump aftertalk

        "Поговорить с кудрявой жабкой":
            scene bg classroom empty with fade
            show arseny

            "Только ты берешься за скребок для отковыривания жвачек, как вспоминаешь, что тебе уже почти 25 и за непослушание тебе ничего не будет. Поэтому ты решаешь поговорить с кудрявой жабкой — он неспешно поливает цветы на подоконнике."
            v "Привет!"
            "'Арсений'" "Здравствуйте!.."
            v "Ни разу не видел, чтобы кто-то поливал цветы в кабинете. Большую работу делаешь!"
            "'Арсений'" "Хех! Спасибо..."
            "Повисает неловкая пауза. Ты все еще не знаешь, как тебе лучше рассказывать о сложившейся ситуации."
            v "Арсений..."
            "'Арсений'" "Кв-арсений."
            v "Прости. Кварсений. В общем... я хотел сказать... (шепотом) Я из другого мира."
            a "Так."
            v "(осторожно) Мы там все дружим... и взрослые... и не жабы... И я не знаю, как я сюда попал..."
            "Ты вкратце рассказываешь Кварсению о своем мире."
            v "...тебе не кажется, что я тебя разыгрываю?"
            a "Я думаю, ты бы не стал меня разыгрывать..."
            v "Так ты поможешь мне?"
            a "Ну... а вдруг ты меня все-таки разыгрываешь... Расскажи мне что-нибудь. О! Расскажи..."
            hide arseny

            menu arseny_question:
                set menuset
                "Расскажи, где я работал?"

                "В столовой":
                    "Ты рассказываешь Кварсению еще немного об Арсении. Хотя немного - это не то слово, которым можно описать жизнь Арсения."
                    jump arseny2

                "На катке":
                    "Ты рассказываешь Кварсению еще немного об Арсении. Хотя немного - это не то слово, которым можно описать жизнь Арсения."
                    jump arseny2

                "В оранжерее":
                    "Ты рассказываешь Кварсению еще немного об Арсении. Хотя немного - это не то слово, которым можно описать жизнь Арсения."
                    jump arseny2

            label arseny2:
                show arseny
                a "Хо!..."
                a "Да, такое нарочно не придумаешь... Ну, давай разбираться..."
                v "Круто! Спасибо!"
                a "Хех..."
                "Вы договариваетесь обсудить сложившуюся ситуацию попозже. Почему-то в компании Кварсения тебе становится совсем спокойно."

                hide arseny
                $ arseny_complete = True

                if arseny_complete is True and leonid_complete is True:
                        jump end
                else:
                    jump aftertalk

label end:
    show bg classroom empty with fade
    show arseny at right
    show leoneed at left
    "Как только Кварсений заканчивает поливать растения, вы собираетесь в кружок вокруг первой парты."
    "Холодный осенний свет пробирается к вам сквозь щели в жалюзях."
    l "То есть, ты иногда просыпаешься здесь? И ничего не помнишь о тех днях, когда тебя тут не было?"
    a "И нечто... некто... оставляет тебе подсказки... о том, где искать подарки?"
    v "Ага."
    l "Хм... будь я на месте Содалва, я не стал бы тебе рассказывать, куда я прячу подарки."
    v "А еще ребята видели, как Содалв каждый день после уроков уходит домой. А меня!... То есть, его... Директор за что-то оставил после занятий."
    a "Постой. Директор?... Ты же знаешь, за что тебя наказали?"
    v "(качает головой)"
    l "Говорят, ты разбил стекло в учительской."
    a "Правда, это был не ты. Не Содалв. Мы свидетели."
    v "!!!"
    l "Позавчера мы возвращались из школы и услышали звон стекла... Вокруг кроме нас никого не было. Почти..."
    a "Мы увидели, как кто-то убегает за угол. Я выхватил телефон... но фотография получилась смазанной. Но сейчас ты сказал про директора... и да... ошибки быть не может!"
    l "Точно! На фотке директор! Та же шляпа и портфель!"
    v "Директор?... Разбил стекло? А потом обвинил Содалва?"
    v "Но зачем?..."
    "Тебе внезапно приходит уведомление на телефон о новой заметке."
    v "Ребят! Заметка!"
    "Ищи свой подарок // в забытом месте // в логическом парадоксе // среди солдатиков."
    a "Чё :)"
    "Ты чувствуешь, как у тебя тяжелеют веки. Неужели опять..."
    l "Но что... Ой! Кварсений! Лови его!!!"
    hide arseny
    hide leoneed
    scene black with fade

    "В голове все начинает путаться. Друзья, которые тебя почти не знают, загадочные подсказки, необоснованные обвинения..."
    "Чушь какая-то. Пусть с этим кто-нибудь другой разбирается. Хочется просто..."
    "Заснуть и забыть это всё."
    "Не то чтобы у тебя был какой-то выбор."
    return