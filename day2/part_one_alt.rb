input = File.readlines('input')

counts = input
  .flat_map { |id| id.chars.group_by { |x| x }.map { |_, v| v.length }.uniq }
  .group_by { |x| x }
  .map { |k, v| [k, v.length] }
  .to_h

puts counts.fetch(2, 0) * counts.fetch(3, 0)
