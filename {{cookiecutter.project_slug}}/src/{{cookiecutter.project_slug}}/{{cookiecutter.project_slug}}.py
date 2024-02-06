def main(args):
    if args is not None:
        args.action(args)
    print(f"Invoked with {args}")
