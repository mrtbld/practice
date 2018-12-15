require_relative 'common.rb'

input = File.read('input').strip!

result = input
  .chars.uniq.map(&:downcase).uniq
  .map { |unit| react_polymer(input.gsub(/#{unit}/i, '')).length }
  .min

puts result
