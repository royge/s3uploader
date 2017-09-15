import sys
import asyncore
import argparse

import pyinotify

from aws import s3_upload

wm = pyinotify.WatchManager()
mask = pyinotify.IN_CREATE
s3_bucket_name = None

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print("Uploading:", event.pathname)
        s3_upload(event.pathname)
        print("Done!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Watch a directory for new files and uploade to S3.'
    )
    parser.add_argument('--dir', help='Directory to watch')

    args = parser.parse_args()

    pyinotify.AsyncNotifier(wm, EventHandler())
    wm.add_watch(args.dir, mask)

    asyncore.loop()
