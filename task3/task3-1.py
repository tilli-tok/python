T = input("Введите значение температуры воды: ")
while True:
  try:
      T = float(T)
      T = int(T)
      if T < 0:
          print("Озеро замерзло")
      elif 0 <= T < 10:
          print("Ледяная вода")
      elif 10 <= T < 15:
          print("Жуть как холодно")
      elif 15 <= T < 18:
          print("Прохладно, но можно искупаться")
      elif 18 <= T < 24:
          print("Кайф")
      elif 24 <= T < 30:
          print("Полный кайф")
      elif 30 <= T < 36:
          print("Горячая")
      else:
          print("Кипяток")
      break
  except:
      print("Вы ввели не число ")
      T = input("Введите значение температуры воды: ")