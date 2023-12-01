from args import args_parser


def main() -> any:

    args = args_parser()

    if args.mode == "test":
        print("Testing Mode...")

    else:
        print("Training Mode...")













if __name__ == "__main__":
    main()