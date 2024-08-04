import json
import logging
import os

import webview


class FileApi:
    def scan_directory(self):
        ret = []
        for dir, _, files in os.walk('./comment'):
            for file in files:
                with open(os.path.join(dir, file), 'r') as f:
                    ret.append(json.load(f))
        return ret


if __name__ == '__main__':
    api = FileApi()
    webview.create_window('Code Inspector', 'dist/index.html', js_api=api)
    webview.start(ssl=True, debug=True)
