require 'set'

input = File.readlines('input')

foo = input.map do |id|
  id.chars.group_by { |x| x }.map { |k, v| v.length }.to_set
end

puts foo.count { |s| s.include? 2 } * foo.count { |s| s.include? 3 }
