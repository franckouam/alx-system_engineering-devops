#!/usr/bin/env ruby
if ARGV.length > 0
    for m in ARGV[0].scan(/School/)
	print m
	STDOUT.flush
    end
    puts 
end
