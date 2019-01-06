require_relative 'common.rb'

input = File.readlines('input')
guard_id, minute = find_sleepy_guard(input, &:max)
puts guard_id * minute
