import os
import contextlib
import sys

# print(os.system('curl --head http://www.example.com'))

# HTTP/1.1 200 OK
# Content-Encoding: gzip
# Accept-Ranges: bytes
# Age: 359729
# Cache-Control: max-age=604800
# Content-Type: text/html; charset=UTF-8
# Date: Mon, 24 Oct 2022 07:41:07 GMT
# Etag: "3147526947"
# Expires: Mon, 31 Oct 2022 07:41:07 GMT
# Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT
# Server: ECS (bsa/EB18)
# X-Cache: HIT
# Content-Length: 648

# print(os.system('curl -X POST -d "a=1&b=2" http://www.example.com'))
# print(os.system('curl -X POST -d "@data.txt" http://www.example.com'))
# print(os.system("""curl -X POST -d "{'a': 1, 'b': 2}" -H "Content-Type: application/json" http://www.example.com"""))


