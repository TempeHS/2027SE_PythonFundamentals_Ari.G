userfile = input("Enter a file name: ")
extension = userfile.lower().split(".")[-1]

match extension:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
