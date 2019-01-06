require 'set'

input = File.readlines('input').map(&:to_i)

seen = Set[]
input.cycle.reduce do |r, i|
  cumul = r + i
  unless seen.add? cumul
    puts cumul
    break
  end
  cumul
end
