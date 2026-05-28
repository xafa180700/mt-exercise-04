import argparse
from sacremoses import MosesTokenizer
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Tokenize parallel corpora for JoeyNMT"
    )

    parser.add_argument("--src", required=True, help="Source language file")
    parser.add_argument("--trg", required=True, help="Target language file")

    parser.add_argument("--out-src", required=True, help="Tokenized source output")
    parser.add_argument("--out-trg", required=True, help="Tokenized target output")

    parser.add_argument("--src-lang", default="en", help="Source language code")
    parser.add_argument("--trg-lang", default="nl", help="Target language code")

    return parser.parse_args()


def tokenize_file(input_path, output_path, lang):
    tokenizer = MosesTokenizer(lang=lang)

    with open(input_path, "r", encoding="utf-8") as infile, \
         open(output_path, "w", encoding="utf-8") as outfile:

        for line in infile:
            line = line.strip()

            if not line:
                outfile.write("\n")
                continue

            tokens = tokenizer.tokenize(
                line,
                return_str=True
            )

            outfile.write(tokens + "\n")


def main():
    args = parse_args()

    # sanity checks
    for path in [args.src, args.trg]:
        if not Path(path).exists():
            raise FileNotFoundError(f"Missing file: {path}")

    print("Tokenizing source corpus...")
    tokenize_file(args.src, args.out_src, args.src_lang)

    print("Tokenizing target corpus...")
    tokenize_file(args.trg, args.out_trg, args.trg_lang)

    print("Done.")


if __name__ == "__main__":
    main()

