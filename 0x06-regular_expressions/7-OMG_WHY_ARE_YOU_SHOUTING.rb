#!/usr/bin/env ruby
if ARGV.length > 0
    for m in ARGV[0].scan(/[A-Z]/)
	print m
    end
    puts
end
