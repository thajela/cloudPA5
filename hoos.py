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
	sentiment = 0
        if '#HoosforSullivan' or 'good' or 'pleasure' or 'work with' or 'support' or '#Sullivan' in text:
		print '{0}\t{1}'.format(date_object.timetuple().tm_yday,1)
	#elif 'good' or 'pleasure' or 'work with' or 'support' in text:
		#print '{0}\t{1}'.format(date_object.timetuple().tm_yday,1)
	
	 			    
	    
		
        line = ""
