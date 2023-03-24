try:
    from PIL import Image
    print("Please enter the file path: ", end='')
    file_path = input().replace('\'', '').replace('"','')
    try:
        info = Image.open(file_path).info
        if info:
            for key in info.keys():
                print(key + ': ' + info[key])
        else:
            print("nothing info in it!")
    except:
        print("Wrong file format!")
except:
    print("You don't have Pillow please install it by this command: pip install Pillow")