require 'set'

input = File.readlines('input')

result = input
  .lazy
  .flat_map do |word|
    (0...word.length).lazy.map do |i|
      chars = word.chars
      chars[i] = :placeholder
      chars
    end
  end
  .reduce(Set[]) do |seen, chars|
    unless seen.add? chars
      break chars.reject { |x| x == :placeholder }.join
    end
    seen
  end
puts result
