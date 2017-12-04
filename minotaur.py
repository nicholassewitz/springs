#!/usr/bin/env python

import os
import sys

def run_job(module):
    try:
        module.run()
    except Exception, e:
        print("Job failed with error %s" % e)
        sys.exit(repr(e))

def main():
    args = sys.argv[1:]
    if not len(args):
      print("Specify a job to run")
      return

    if args[0] == 'price-inference':
        from jobs import price_inference
        run_job(price_inference)

    else:
        print("Unknown job %s" % args[0])
        return

if __name__ == '__main__':
    main()
