#!/usr/bin/env ruby

def match_school(input)
  match = input.scan(/hbt{1,4}n/)
  if match
    puts "#{match.join("")}"
  end
end

# ARGV[0] will be the first command line argument
match_school(ARGV[0])
