def main(args):
    if args.action is not None:
        args.action(args)
    print(f"Invoked with {args}")
