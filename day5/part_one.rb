require_relative 'common.rb'

input = File.read('input').strip!

reacted = react_polymer input
puts reacted.length
