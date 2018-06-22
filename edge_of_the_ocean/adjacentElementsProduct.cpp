int adjacentElementsProduct(std::vector<int> inputArray) {

    auto num_elements = inputArray.size();
    std::vector<int> result_vector;
    for (size_t i = 1; i < num_elements; ++i) {
       result_vector.push_back(inputArray[i-1] * inputArray[i]);
    }
    auto max = *max_element(result_vector.begin(), result_vector.end());
    return max;
}
