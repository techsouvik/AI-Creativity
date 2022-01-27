from ascii.ascii import run
import argparse

def main():
    parser = argparse.ArgumentParser(description='Automatic ASCII art generator')
    parser.add_argument("-n", "--name", required=False, help="name of the user", default='Geeks')
    parser.add_argument("-t", "--token", required=False, help="Search token of the NFT Batch", default='NFT')
    parser.add_argument("-m", "--max", required=False, help="Maximum number of NFTs to be searched", default=3)
    parser.add_argument("-c", "--chars", required=False, help="Characters to be used in the ASCII art", default='AnikArnabDhriteshJagreetSaptarshiSubhajitSurya')
    args = vars(parser.parse_args())
    # display a friendly message to the user
    print('------------------------------------------------------------------------------')
    print("Welcome to the automatic ASCII art generator!")
    print("Hi there {}, it's nice to meet you!".format(args["name"]))
    run(args["token"], int(args["max"]), args["chars"])

if __name__ == "__main__":
    main()