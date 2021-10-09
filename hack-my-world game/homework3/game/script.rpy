﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define v = Character('Владос', color="#ffffff")
define r = Character('Владимир Жабовица', color="#ffffff")
define p = Character('Квакица', color="#ffffff")
define b = Character('Баржа', color="#ffffff")
define l = Character('Лягунид', color="#ffffff")
define a = Character('Кварсений', color="#ffffff")
define w = Character('Квакуля', color="#ffffff")
define i = Character('Яна (лягушка)', color="#ffffff")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    scene black
    "Ты просыпаешься из-за солнца, бьющего тебе прямо в глаза."
    scene bg room with fade
    v "Уф..."
    v "О... Я снова здесь..."
    "К твоему удивлению, вокруг царит большой беспорядок, которого ты не замечал здесь раньше."
    v "..."
    "Ты пробуешь осмотреться, но не находишь ничего интересного."
    v "Это что, опять в школу идти..."
    "Прежде чем выйти, ты на пару секунд останавливаешься перед тостером. Ооо, сделай это, шепчут слева. Ты опаздываешь, шепчут справа. Позволь себе это, король. Виабушник. Ты не пожалеешь. Ты пожалеешь."

    menu toast:
        "Побежать в школу":
            "Ты покидаешь квартиру, не позавтракав. Ты сэкономил время - но также тебя не покидает ощущение, что ты сэкономил на самом себе."
            jump school
        "Сделать тост и побежать в школу":
            "Все равно никто не увидит, думаешь ты. Тост выскакивает тебе прямо в руку, ты впиваешься в него зубами. Вот ты уже стоишь на пороге, натягивая кроссовок. Вот уже бежишь вниз по ступенькам."
            "Вот это жизнь."
            jump school

label school:
    scene bg classroom full with fade
    "Ты забегаешь в кабинет за пару минут до звонка. Ты уже представляешь, как весело поздороваешься со своими друзьями - однако они встречают тебя удивленными и даже испуганными взглядами."
    show rucaweetsa at left
    r "(громко) Привет, Содалв!"
    v "Это я..."
    show pteetsa at right
    p "Говорила же, что скоро придёт нормальный Содалв!"
    hide rucaweetsa
    show leoneed at left
    l "Мы уже беспокоиться начали!"
    hide pteetsa
    show arseny at right
    a "Содалв тут совсем в школу ходить перестал..."
    hide arseny
    hide leoneed
    "Ребята рассказывают тебе, что история повторилась - Содалв (то есть, тогда ещё ты) внезапно потерял сознание, очнулся, а потом побрёл домой, ничего не замечая вокруг. После этого он больше в школе не появлялся."
    "Ты хочешь расспросить друзей подробнее, но тут раздаётся звонок."
    show brusneeka
    "Дверь открывается, и в кабинет входит небольшая аккуратная жаба в светлом платье. Повисает тишина."
    "Жаба садится за учительский стол, складывает руки и начинает разглядывать стену напротив. Ты невольно думаешь, что она похожа на 'девочку с персиками' - только без персиков. И не девочку."
    "Учительница" "(отрывая взгляд от стены, громко) Ну, начнем!"
    "Учительница" "..."
    "Все ученики заметно напрягаются. Ты тоже. Учительница тоже. Она молчит."
    "Учительница" "(резко) Тема урока!..."
    "Темой урока оказывается... радиотехника!? Ты был бы и рад заснуть, но из-за странного темпа речи учительницы не можешь. Но следить за материалом тоже не получается..."
    "Учительница" "...Содалв!"
    v "!"

    default menuset = set()
    
    menu lesson:

        set menuset
        "Как называется деталь, которую можно использовать для усиления, генерирования, и преобразования электрических сигналов?"

        "Саморез":
            "Учительница" ". . ."
            "Учительница" "...нет."
            jump school2

        "Транзистор":
            "Учительница" "...верно."
            "Учительница" "{i}Запишите.{/i} Полезно."
            jump school2

        "Конденсатор":
            "Учительница" ". . ."
            "Учительница" "...нет."
            jump school2

label school2:
    "Звенит звонок. Учительница сидит. Все продолжают сидеть."
    "Учительница" "...Содалв."
    v "?"
    "Учительница" "...останься."
    "Все остальные встают из-за своих парт и разбегаются кто куда. Ты подходишь к учительскому столу."
    "Учительница" "...нужно... нагонять материал."
    v "Хорошо, я позанимаюсь..."
    "Учительница" "...нужно... сегодня... останься..."
    "Не доведя предложение до логического конца, учительница быстро собирает вещи и выскакивает в коридор."
    hide brusneeka
    "Голос" "Ты не переживай так."
    "Второй голос" "Мы тебе поможем."
    show weeka at left
    show iana at right
    "Ты оборачиваешься. Перед тобой стоят... длинноволосая жабка и жабка с челкой. Это же..."
    v "!?"
    jump afterschool

label afterschool:
    scene bg classroom empty with fade
    show weeka at left
    show iana at right
    "В классе висит неловкая тишина. Остальных твоих друзей из кабинета выгоняет учительница - чтобы не мешали вам заниматься. Две оставшиеся жабки, впрочем, не спешат помогать тебе и занимаются своими делами."
    hide weeka
    hide iana

    $ weeka_complete = False
    $ iana_complete = False
    
    menu aftertalk:
        
        "Поговорить с жабкой с чёлкой":
            scene bg classroom empty with fade
            show iana
            "Жабка с модной чёлкой, кажется, вовсе не обращает на тебя внимания. Ты невольно удивляешься тому, как обе твои надзирательницы потеряли к тебе интерес, как только вы остались наедине."
            v "...привет?"
            "'Яна'" "(поднимает глаза от книги) Привет!"
            v "...я думал, вы должны... помогать мне с учебой?"
            "'Яна'" "А ты хочешь?"
            "Ты начинаешь ерзать на стуле - это же твоя возможность поговорить с Яной о чем-то умном!"
            v "Было бы круто!"
            "'Яна'" "А с чем тебе нужно помочь?"
            v "Э... ну, может... с философией?"
            "'Яна'" "С чего ты взял, что я ее знаю?"
            v "(вздыхает)"
            v "А ты представь, что в параллельном мире ты ее преподаешь. И у нас там... много друзей. И мы давно не школьники..."
            "Ты вкратце рассказываешь 'Яне' о своем мире."
            "'Яна'" "Ого! А что я еще там делаю?"

            menu iana_question:
                set menuset
                "Музыку в каком жанре я писала в юности?"

                "shoegaze":
                    "'Яна' внимательно выслушивает твой рассказ о человеческой Яне. Больше всего ее взволновало наличие у человеческой Яны кота Томаса."
                    jump iana2

                "trip-hop":
                    "'Яна' внимательно выслушивает твой рассказ о человеческой Яне. Больше всего ее взволновало наличие у человеческой Яны кота Томаса."
                    jump iana2

                "8-bit":
                    "'Яна' внимательно выслушивает твой рассказ о человеческой Яне. Больше всего ее взволновало наличие у человеческой Яны кота Томаса."
                    jump iana2

            label iana2:

                "'Яна'" "Ничего себе! Звучит мощно..."
                "'Яна'" "Ладно, я помогу тебе. Может, не с философией, но с чем смогу..."
                v "Круто, спасибо! Но как к тебе обращаться?"
                "'Яна'" "Яна."
                v "...просто Яна?"
                i "Лягушка."
                v "Окей..."
                "Вы договариваетесь обсудить все подробнее чуть позже. Когда Яна (лягушка) откладывает свою книгу в сторону, ты видишь надпись на обложке - '100 рецептов для микроволновой печи'."

                $ iana_complete = True
                hide iana

                if iana_complete is True and weeka_complete is True:
                    jump end
                else:
                    jump aftertalk

        "Поговорить с длинноволосой жабкой":
            scene bg classroom empty with fade
            show weeka
            "Жабка с длинными прямыми волосами и аккуратными стрелками заполняет дневник, кажется, уже на третью неделю вперед. Сомнений нет - перед тобой сидит Вика."
            v "(шепотом) Псс."
            "Тебе в голову приходит глупая идея."
            v "Вика, это я."
            "'Вика'" "(неуверенно) Ага. Что?"
            v "Вика, это я, Владос."
            "'Вика'" "(осторожно) Владос...?"
            "'Вика'" "Привет, Владос!"
            v "...подожди, ты что, узнаешь меня?"
            "'Вика'" "Конечно."
            v "Тогда расскажи обо мне что-нибудь, что знаю только я!"
            "'Вика'" "(задумчиво) Ты... Владос... пёс..."
            v ". . ."
            "'Вика'" "(с досадой) Нет, я тебя не узнаю. О чем ты вообще?"
            v "Сорри. Но я и правда не отсюда. Я... из другого мира, где мы все люди, а не жабы... Честно!"
            "Ты вкратце рассказываешь 'Вике' о своем мире."
            "'Вика'" "(озадаченно) Честно?... А расскажи еще что-нибудь..."

            menu weeka_question:
                set menuset
                "Расскажи, на каких текстовых ролевых я играла?"

                "По Королю Льву":
                    "Ты рассказываешь 'Вике' ещё немного о человеческой Вике. 'Вику' очень интересует, какие та знает аниме-тайтлы."
                    jump weeka2

                "По Сверхъестественному":
                    "Ты рассказываешь 'Вике' ещё немного о человеческой Вике. 'Вику' очень интересует, какие та знает аниме-тайтлы."
                    jump weeka2

                "По Эльфийской песне":
                    "Ты рассказываешь 'Вике' ещё немного о человеческой Вике. 'Вику' очень интересует, какие та знает аниме-тайтлы."
                    jump weeka2

            label weeka2:
                "'Вика'" "О..."
                "'Вика'" "Окей! Звучит как правда! Квакуля в деле!"
                v "Квакуля?"
                w "Ага. Да не ссы, разберемся!"
                "Вы договариваетесь обсудить все подробнее чуть позже. Ты замечаешь, что хоть и подразумевалось, что ты будешь нагонять материал, за этот разговор ты вовсе не стал умнее."

                $ weeka_complete = True
                hide weeka

                if iana_complete is True and weeka_complete is True:
                    jump end
                else:
                    jump aftertalk
    
label end:
    show bg classroom empty with fade
    show weeka at left
    show iana at right
    "Вы втроем усаживаетесь вокруг последней парты. По столу разбросаны учебники, тетради и ручки, к которым никто из вас так и не прикоснулся."
    w "Итак, рекап: ты, Владос-человек, меняешься телами с нашим одноклассником Содалвом."
    i "При этом Содалв портит жизнь тебе, пока находится в твоем теле, и прячет твои подарки."
    w "А здесь тебе портят жизнь, оставляя после уроков..."
    v "И как выяснилось, ни за что."
    i "Погодите. Ты же ничего не знаешь про оценки Содалва, да?"
    v "Не знаю. А вы?"
    w "Мы тоже не знаем... Нас просто попросили помочь тебе с учебой. Мы думали, на месте разберемся, с какой... Мы просто отличницы."
    i "Может, мы можем проверить его оценки?"
    w "Точно! У меня же с собой журнал!"
    "Квакуля достает из рюкзака классный журнал."
    v "Откуда он у тебя?"
    w "Я же староста. Меня попросили его занести после последнего урока в учительскую, а я задержалась..."
    v "(листая журнал) Но... у Содалва вроде бы всё в порядке..."
    i "Стой! Это что..."
    w "Ничего себе! Сплошные двойки!"
    v "По... информатике? У парня, который ходит в компьютерный клуб?... Неужели все так плохо?"
    i "Подождите. Содалва же не было последние несколько дней, так?"
    w "Так... а оценки все равно стоят! И... и в другие дни тоже! Там, где должна стоять 'н' - стоит двойка!"
    i "Главное, наверное, даже не это. А кто ведет этот предмет."
    w "(шокированно) Директор!!!"
    i "И он же оставлял Содалва после уроков... Но зачем ему это нужно..."
    v "Ребята! Мне новая заметка пришла!"
    hide weeka
    hide iana
    "Лишённое движения // неуклюжее железное тело // прячет подарок // в седой траве. // Ищи его в точке // 59.86892, 30.29979."
    v "(про себя) {i}59.86892, 30.29979{/i}... Надо бы записать..."
    show weeka at left
    show iana at right
    i "Хм..."
    v "А ещё я, сейчас, кажется, отрублюсь. До этого всегда отрубался."
    w "Зато ты сейчас хотя бы сидишь!"

    scene black with fade
    "Ты снова чувствуешь, как всё остается позади. Загадочные планы директора... неизвестно куда пропавший Содалв... нестёртое с доски сегодняшнее число..."
    "Ты чувствуешь, что это всё происходит с тобой не в последний раз."
    "Ты глубоко вздыхаешь."
    return
