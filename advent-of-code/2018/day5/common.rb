def react_polymer(polymer)
  reacted = polymer.dup
  i = 1
  while i < reacted.length
    a = reacted[i-1]
    b = reacted[i]
    if a.swapcase == b
      reacted[i-1..i] = ''
      i -= 1
    else
      i += 1
    end
  end
  reacted
end
