int makeArrayConsecutive2(std::vector<int> statues) {
    auto input_size = statues.size();
    if(input_size == 1) return 0;
    auto result = std::minmax_element(statues.begin(), statues.end());
    return (*result.second) - (*result.first) - input_size + 1;
}
