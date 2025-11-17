import argparse
import os
import sys

import pandas as pd

def parse_args():
	parser = argparse.ArgumentParser(
		description="Convert CSV to Markdown table."
	)
	parser.add_argument(
		"--input", "-i",
		required=True,
		help="Input CSV file path (or '-' for stdin)."
	)
	parser.add_argument(
		"--output", "-o",
		required=True,
		help="Output file (or '-' / 'stdout' for stdout)."
	)
	return parser.parse_args()

def read_csv(path):
	if path == "-" or path.lower() == "stdin":
		return pd.read_csv(sys.stdin)
	return pd.read_csv(path)

def write_output(path, content : str):
	if path == "-" or path.lower() == "stdout":
		sys.stdout.write(content)
	else:
		with open(path, "w", encoding="utf-8") as f:
			f.write(content)

if __name__ == "__main__":
	args = parse_args()
	df = read_csv(args.input)
	md = df.to_markdown(index=False) + "\n"
	write_output(args.output, md)
