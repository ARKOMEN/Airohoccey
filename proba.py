import cv2 # Импорт модуля OpenCV

           # Видео вывод с веб камеры компьютера, при включенной камере
cap = cv2.VideoCapture("video$.mp4"); # Вывод с видео файла

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Вывод в консоли размера нашего окна.


cap.set(3,1280) # Установление длины окна
cap.set(4,700)  # Ширина окна

print(cap.get(3))
print(cap.get(4))
while(True): # Вывод кадров производится  в цикле
 
  ret, frame = cap.read()
  frame = cv2.rectangle(frame,(384,0),(510,128),(0,0,255),10) # добавление к видео выводу объекта прямоугольника
 
 
  print(frame)  # Вывод массива в консоль
 
  cv2.imshow("frame",frame) # Метод для визуализации массива кадров
 

cap.release()
cv2.destroyAllWindows()
