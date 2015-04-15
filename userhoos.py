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

        if '#HoosForSullivan' and 'RT' in text:
            try:
		RT = data["retweeted_status"]
	    	user = RT["user"]
	    	name = user["name"]
            	print '{0}\t{1}\t{2}'.format(date_object.timetuple().tm_yday,name,1)
	    except:
		pass
        line = ""
