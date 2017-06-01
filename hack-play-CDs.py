from bs4 import BeautifulSoup
from urllib import urlopen
import os

path = "musicas/"

url = "http://www.playcds.com.br/musicas/Los-Hermanos/Perfil/"

resp = urlopen(url)

if resp.code == 200:
    command = "mkdir "+path
    print command

    os.system(command)

    html = BeautifulSoup(resp.read(), "html.parser")

    links = html.findAll("a", href=True)

    for link in links:
        if "Parent Directory" in link:
            pass
        else:
            new_url = url+link.string
            new_url = new_url.replace(" ", "")
            get = urlopen(new_url)

            print new_url 

            if get.code == 200:

                path_music = path+link.string
                path_music = path_music.replace(" ", "")

                print path_music

                musica = open(link.string, "wb")

                print "gravando em disco"
                musica.write(get.read())
                musica.close()
else:
    print resp.code