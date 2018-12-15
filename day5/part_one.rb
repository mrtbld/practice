input = File.read('input').strip!

i = 1
while i < input.length
  a = input[i-1]
  b = input[i]
  if a.downcase == b.downcase and a != b
    input[i-1..i] = ''
    i -= 1
  else
    i += 1
  end
end

puts input.length
