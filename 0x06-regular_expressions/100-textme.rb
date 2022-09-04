#!/usr/bin/env ruby
if ARGV.length > 0
    res = ARGV[0].scan(/\[from:([^\]]*)\]\s*\[to:\s*([^\]]+)\]\s*\[flags:\s*([^\]]+)/)
    for r in res
	print "%s,%s,%s" % r
    end
    puts
end
