from src.scrapper import WebScrapper

if __name__ == '__main__':
    newScapper = WebScrapper()
    data = newScapper.get_currencies() #print out loaded currencies

    for i in range(len(data)):
        print("Rank: ", data[i][0])
        print("Name: ", data[i][1])
        print("Symbol: ", data[i][2])
        print("Market Cap: ", data[i][3])
        print("Price: ", data[i][4])
        print("Circulating Supply: ", data[i][5])
        print("---------------------------------")
