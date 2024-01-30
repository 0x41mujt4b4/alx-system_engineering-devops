#!/usr/bin/env ruby

def match_school(input)
  match = input.scan(/\[from:(\d+)\].*\[to:(\d+)\].*\[flags:([^\]]+)\]/)
  if match
    puts "#{match.join(",")}"
  end
end

# ARGV[0] will be the first command line argument
match_school(ARGV[0])
