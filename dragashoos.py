#!/usr/bin/env python
import json
import sys

with sys.stdin as f:
    for line in f:
        while True:
            try:
                data = json.loads(line)
                break
            except ValueError:
                # Not yet a complete JSON value
                line += next(f)

        # do something with the tweet

        date = data["created_at"]

        from datetime import datetime
        date_object = datetime.strptime(date,"%a %b %d %H:%M:%S +0000 %Y")

        text = data["text"]

        if 'Dragas' in text:
            print '{0}\t{1}'.format(date_object.timetuple().tm_yday,1)
	    
		
        line = ""
