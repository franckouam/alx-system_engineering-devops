#!/usr/bin/env ruby
if ARGV.length > 0
    for m in ARGV[0].scan(/^\d{10,}/)
	print m
    end
    puts
end
