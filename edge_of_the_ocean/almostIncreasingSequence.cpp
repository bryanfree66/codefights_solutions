template <typename Iterator>
bool almost_strictly_increasing( Iterator first, Iterator last )
{
  if (std::distance( first, last ) < 3) return true;

  auto u = std::adjacent_find( first, last, std::greater_equal <decltype(*first)> () );
  if (u == last) return true;

  auto v = std::adjacent_find( u + 1, last, std::greater_equal <decltype(*first)> () );
  if (v != last) return false;
    
  auto a = (  u ==  first) or (u[-1] < u[1]);
  auto b = (++u == --last) or (u[-1] < u[1]);

  return a or b;
}

template <typename T>
bool almostIncreasingSequence(std::vector<T> sequence) {
    return almost_strictly_increasing( sequence.begin(), sequence.end() );
}
