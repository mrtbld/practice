require 'date'

input = File.readlines('input')
  .map do |l|
    m = l.match /^\[(?<datetime>.+?)\] (?:Guard #(?<guard_id>\d+) )?((?<action>.+?))$/
    {
      datetime: DateTime.parse(m[:datetime]),
      guard_id: m[:guard_id] && m[:guard_id].to_i,
      action: m[:action],
    }
  end
  .sort_by(&:first)

input.each_cons(2) { |a, b| b[:guard_id] ||= a[:guard_id] }

guard_id, sleep = input
  .reject { |i| i[:action] == 'begins shift' }
  .group_by { |i| i[:guard_id] }
  .transform_values do |events|
    events
      .each_slice(2)
      .map { |a, b| [a[:datetime].minute, b[:datetime].minute] }
      .reduce(Array.new(60, 0)) { |r, (a, b)| r.map.with_index { |n, i| (a...b) === i and n + 1 or n } }
  end
  .max_by { |k, v| v.sum }
  .to_a

sleepiest_minute = sleep.index(sleep.max)

puts guard_id * sleepiest_minute
