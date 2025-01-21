def compareFiles(aFile, bFile):
    while True:
        aChunk = aFile.read(CHUNK_SIZE)
        bChunk = bFile.read(CHUNK_SIZE)

        if len(aChunk) != len(bChunk):
            return False

        if len(aChunk) == 0:
            break

        if aChunk != bChunk:
            return False
    return True