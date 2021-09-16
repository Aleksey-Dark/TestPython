##task2
Напишите программу, которая находит точки столкновения сферы и прямой линии. Если их нет,
то выводится фраза: «Коллизий не найдено» (кириллицей, будьте внимательны), если есть, то
выводятся координаты точек, ограниченные символом новой строки. Координаты считываются из
файла, который имеет следующий формат:
````
{sphere: {center: [0, 0, 0], radius: 10.67}, line: {[1, 0.5, 15], [43, -14.6, 0.04]}}
````
Примечание: файл не будет содержать синтаксических ошибок, однако объекты и ключи могут
находится в свободной последовательности. Координаты точек – массив [x, y, z].

Дополнительно: верх крутости – рендеринг данной сцены.