import sys
from Crypto.Hash import SHA256

file = sys.argv[1]

if (len(sys.argv) > 2):
    chunksize = int(sys.argv[2])
else:
    chunksize = 1024

def generateHashFromBytes(chunksOfFile = []):
    # gera um array de bytes
    hashGenerated = bytearray()

    # enquanto ainda tiver chunks para pegar
    while chunksOfFile:
        # pega sempre do final com pop()
        chunk = chunksOfFile.pop()
        # soma com a parte da hash atual
        chunk += hashGenerated
        # gera proxima parte da hash baseada no chunk atual
        hashGenerated = SHA256.new(chunk).digest()

    # retorna hash
    return hashGenerated.hex()

def getBytesFromFile(file, chunksize):
    # armazena todos chunks aqui
    chunksOfFile = []
    # abre video
    video = open(file, 'rb')
 
    # pega primeiro chunk
    chunk = video.read(chunksize)

    # enquanto ainda temos chunks para pegar
    while chunk:
        # salvva chunk
        chunksOfFile.append(chunk)
        # pega proximo chunk
        chunk = video.read(chunksize)

    # retorna todos chunks
    return chunksOfFile

print(generateHashFromBytes(getBytesFromFile(file, chunksize)))

