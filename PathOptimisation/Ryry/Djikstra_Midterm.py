import Djikstra
import argparse

parser = argparse.ArgumentParser(description="Starting Node #")
parser.add_argument('node', metavar='node', type=int, help='starting node # [0,4]')
args = parser.parse_args()

midterm = Djikstra.Djikstra(args.node)

midterm.run()