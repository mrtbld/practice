input = File
  .readlines('input')
  .map { |s| s.match(/#\d+ @ (?<left>\d+),(?<top>\d+): (?<width>\d+)x(?<height>\d+)/) }
  .map { |m| [m[:left], m[:top], m[:width], m[:height]].map(&:to_i) }

fabric = Array.new(1000) { Array.new(1000, 0) }

input.each do |(l, t, w, h)|
  (l...(l+w)).each do |x|
    (t...(t+h)).each do |y|
      fabric[x][y] += 1
    end
  end
end

puts fabric.flatten.count { |i| i > 1 }
