import sys

# 1. 
def loadData(fname):
    lst = []
    with open(fname, "r", encoding="utf8") as f:
        f.readline()    # read and discard 1st line
        # next(f)
        for line in f:
            line = line.strip()
            cols = line.split(",")
            # (rank, equipa, pais, score, scoreA, varRank)
            tup = (int(cols[0]), cols[1], cols[2], \
                   int(cols[3]), int(cols[5]), \
                   int(cols[6] + cols[4]))
            lst.append(tup)
    return lst


def countryTableFile(lst, country, file):
    print("\nEquipas de", country, file=file)
    print("{:<40s} {:>7s} {:>7s}".format("Equipa", "Posicao", "Score"), file=file)
    for tup in lst:
        if tup[2] == country:
            print("{:<40s} {:>7d} {:>7d}".format(tup[1], tup[0], tup[3]), file=file)


def countryTable(lst, country):
   #countryTableFile(lst, country, sys.stdout) 
   countryTableFile(lst, country, None) 


def saveCountryTable(lst, country, fname):
    with open(fname, "w", encoding="utf8") as fout:
        countryTableFile(lst, country, fout) 
        

def countryTeams(lst):
    dic = {}
    for tup in lst:
        rank, equipa, pais, score, scoreA, varRank = tup
        if pais not in dic:
            dic[pais] = []
        dic[pais].append(equipa)
    return dic
    # {"Angola": ["Sporting Cabinda", ...], "Portugal": ["Benfica", ...] }


def main():
    lst = loadData("Soccer_Football_Clubs_Ranking.csv")
    print(lst[-10:])

    countryTable(lst, "Angola")
    saveCountryTable(lst, "Brazil", "Brazil.txt")

    dic = countryTeams(lst)
    print(dic)

if __name__ == "__main__":
    main()


