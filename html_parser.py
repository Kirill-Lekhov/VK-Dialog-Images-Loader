import os
import sys
from urllib.request import urlretrieve


def download_target_photo(photo_path, url):
    photo_name = photo_path + '.png'
    urlretrieve(url, photo_name)


def process(path):
	files = list(
        reversed(
            sorted(
                map(
                    lambda x: int(x.strip("messages").strip(".html")), os.listdir(path))
                    )
                )
            )

	number_of_images = 0
	href = []
	images = []

	None if 'photos' in os.listdir('.') else os.mkdir('photos')  # check photo folder

	for file_name in files:
	    with open(path + '//' + "messages" + str(file_name) + ".html") as file:
	        lines = file.readlines()

	        for line in lines:
	            if "href" in line:
	                href.append(line)

	                if 'jpg' in line or 'jpeg' in line or 'gif' in line:
	                    line = line.split("href=")[1][1:]
	                    line = line.split("'>")[0]
	                    images.append(line)
	                    download_target_photo('photos/' + str(number_of_images), line)
	                    print("Фото {} успешно загружено".format(number_of_images))
	                    number_of_images += 1

	print("Работа завершена. Кол-во изображений:", number_of_images)


if __name__ == "__main__":
	if len(sys.argv) > 1:
		path = sys.argv[1]
		
	else:
		print('Не указан путь до папки')
		path = input('Введите путь: ')

	process(path)
