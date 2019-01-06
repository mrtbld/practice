require 'date'

def find_sleepy_guard(raw_input)
  input = raw_input
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
        .map { |fall, wake| [fall[:datetime].minute, wake[:datetime].minute] }
        .reduce(Array.new(60, 0)) do |sleep, (fall, wake)|
          sleep.map.with_index { |times_slept, minute| (fall...wake) === minute and times_slept + 1 or times_slept }
        end
    end
    .max_by { |_, sleep| yield sleep }
    .to_a

  sleepiest_minute = sleep.index(sleep.max)

  [guard_id, sleepiest_minute]
end
