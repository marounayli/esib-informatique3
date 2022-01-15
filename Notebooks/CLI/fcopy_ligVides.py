# Charbel Farah
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('f1')
parser.add_argument('f2')
parser.add_argument('--empty_line','-el', required=False, type=int)
args = parser.parse_args()
with open(args.f1) as f1:
    with open(args.f2, 'w') as f2:
        if not args.empty_line:
            s=f1.read()
            f2.write(s)
        else:
            for line in f1:
                f2.write(line)
                f2.write('\n' * args.empty_line)
