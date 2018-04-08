def get_country_codes(prices):
    words = prices.split()
    init = ""
    for name in words:
        init += name[0]
        init += name[1] + ", "
    return init[:-2]


def main():

    print(get_country_codes("NZ$300, KR$1200, DK$5"), "NZ, KR, DK")
    print(get_country_codes("US$40, AU$89, JP$200"), "US, AU, JP")
    print(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"), "AU, NG, MX, BG, ES")
    print(get_country_codes("CA$40"), "CA")

if __name__ == "__main__":
    main()

