input = File
  .readlines('input')
  .map { |s| s.match(/#(?<id>\d+) @ (?<left>\d+),(?<top>\d+): (?<width>\d+)x(?<height>\d+)/) }
  .map { |m| [m[:id], m[:left], m[:top], m[:width], m[:height]].map(&:to_i) }

result = input
  .reject do |(ia, la, ta, wa, ha)|
    input.any? do |(ib, lb, tb, wb, hb)|
      ia != ib and (la + wa) > lb and la < (lb + wb) and (ta + ha) > tb and ta < (tb + hb)
    end
  end
  .dig 0, 0

puts result
