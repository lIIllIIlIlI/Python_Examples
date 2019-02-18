import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--clean','-c', help = 'clean build folder before compilation', action="store_true", default=False)
parser.add_argument('--instrumentation','-i', help = 'List of instrumentations, multiple instrumentations allowed. Example: --instrumentation Xcp Profiler', choices = build_instrumentations, nargs = '+', required = True)
parser.add_argument('--nocores', '-n', help='Number of vCores available in the system is default.', type = int, required = False)
parser.add_argument('--release','-r', help='Enables deterministic build for release', action="store_true", default=False)

args = parser.parse_args()

print(args.nocores)
