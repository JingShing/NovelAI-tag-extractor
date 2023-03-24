try:
    # try to import Pillow
    from PIL import Image
    print("Please enter the file path: ", end='')
    # get file path if file path has ' or " will be deleted
    file_path = input().replace('\'', '').replace('"','')
    try:
        # try to load image
        info = Image.open(file_path).info
        if info:
            # print all info on cmd
            for key in info.keys():
                print(key + ': ' + info[key])
        else:
            print("nothing info in it!")
    except:
        # wrong format or cannot load image
        print("Wrong file format!")
except:
    # you need to get pillow to use this code
    print("You don't have Pillow please install it by this command: pip install Pillow")
