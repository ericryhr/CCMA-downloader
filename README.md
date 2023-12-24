# CCMA Downloader
Software per descarregar contingut de sx3.cat i 3cat.cat

Requeriments:
S.O. preferiblement linux (o Windows amb wsl)
python3
selenium - pip install selenium
seleniumwire - pip install seleniumwire
sudo apt install chromium-chromedriver
youtube-dl (important afegir-lo al path)
ffmpeg

Ús: 
    - Crear un fitxer de text amb les urls dels capítols a descarregar (1 per línia)
    - Executar amb $python SX3_downloader.py urlsFile

PD: De moment funciona perquè hi ha un fitxer sprite.vtt amb la mateixa url que el link .mpd que
necessita el youtube-dl per obtenir el vídeo. Esperem que no ho canvïin en el futur