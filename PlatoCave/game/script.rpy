﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Потерянная душа', color="#c8ffc8")
define r = Character('Рассказчик', color = "#DCD36A")
define l = Character('Люди', color = "#0000ff")

#Музыка и звуки(добавление взяких звуков и музыки на разные сцены, хз как, в интернете поискать надо)
#Звуки и музыку добавлять в папку audio
#define.audio.nameSoundOrMusic = "music/name.mp3(.ogg)"
define FastDissolve= Dissolve(0.5)
define MediumDissolve= Dissolve(1.0)
define SlowDissolve= Dissolve(2.5)
# Игра начинается здесь:
label start: #похоже, лэйбл старт важен, поэтому !!НЕ ПЕРЕИМЕНОВЫВАТЬ!!
    scene bg intro
    "В темной и сырой пещере живут скованные цепями узники. Они с рождения не видят белого света и даже не могут повернуть голову в сторону выхода."
    "Заключенные видят только тени на стенах пещеры и считают, что это и есть реальные предметы. Они верят, что добьются успеха и уважения в обществе, если будут усердно наблюдать за тенями, изучать их и предсказывать появление новых."
    "Но однажды случилось необъяснимое и один из узников, прикованный в другом конце пещеры смог высвободиться из цепей…"
    #проигрывание добавленной музык
    #play music nameSoundOrMusic (добавлять можно в любом месте лэйбла, туда, гда хотите воспроизвести
    scene bg cave with MediumDissolve
    show ch soul at left

label scene_One: #Остальным можно задавать любое значаение
    menu:
        e "Я впервые вижу какое-то свечение, что же мне делать?"
        "Попробовать починить то, что меня удерживало":
            jump scene_Two
        "Пойти на свечение":
            jump scene_Three
        "Рассказать об этом людям":
            jump scene_Four
label scene_Two:
    e "не получилось, видимо это не починить."
    jump scene_One
label scene_Four:
    #добавить толпу
    e "Друзья, я вижу свет! Раньше я его не видел, только посмотрите!"
    l "О чем ты говоришь? Здесь ничего не изменилось!"
    l "Ну и дурак!"
    jump scene_One
label scene_Three:
    #фон пещеры со светом и челом
    e "Мне страшно, но я пойду туда, чтобы узнать, что это такое!"
    e "чем ближе я подхожу, тем сильнее я хочу закрыть свои глаза! Но я не пойду назад, я должен узнать, что это!"
    hide ch
    "Чем ближе подходил человек к свету, тем сильнее у него кружилась голова."
    "Как только он почувствовал, что весь взор его был заполнен ярким светом он упал на землю без сил."
    "Спустя немного времени он очнулся и увидел нечто, что его поразило!"
    return

#надо еще изменить стиль всех кнопок
