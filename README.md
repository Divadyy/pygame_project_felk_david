1. a. Name: Shattered Dungeon
   b. button.py: 34 строки
      classes.py: 23 строки
      config.py: 38 строк
      functions2.py: 386 строк
      main.py: 5 строк
      menu.py: 358 строк
      Всего: 844 строки
2. pip install pygame
3. Запускается main.py и запускается main_menu() from menu.py, выбираются настройки, настройки передаются в game_cycle() from functions2.py при помощи global переменных, new_game() from menu.py запускает game_cycle() from functions2.py со всеми настройками, загружается уровень с .txt файла при помощи load_from_file() from functions2.py. Каждый ход рендерится при помощи render() from functions2.py, process_enemy_moves() осуществляет ход существ (кроме игрока)
4. Запускается главное меню с выбором настроек, при нажатии кнопки 'начать новую игру' начинается игра со всеми выбранными настройками
