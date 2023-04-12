# SX3_downloader
Software per descarregar contingut de sx3.cat

Requeriments:
S.O. preferiblement linux (tot i que a Windows hauria de funcionar)
python3
selenium - pip install selenium
seleniumwire - pip install seleniumwire
youtube-dl (important afegir-lo al path)
ffmpeg

Ús: 
    - Crear un fitxer de text amb les urls dels capítols a descarregar
    - Executar amb $python SX3_downloader.py urlsFile

PD: De moment funciona perquè hi ha un fitxer sprite.vtt amb la mateixa url que el link .mpd que
necessita el youtube-dl per obtenir el vídeo. Esperem que no ho canvïin en el futur