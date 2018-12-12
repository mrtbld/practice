require 'set'

input = File.readlines('input')

seen = Set[]
catch :found do 
  input.each do |word|
    (0...word.length).each do |i|
      chars = word.chars
      chars[i] = :placeholder
      unless seen.add? chars
        puts chars.reject { |x| x == :placeholder }.join
        throw :found
      end
    end
  end
end
